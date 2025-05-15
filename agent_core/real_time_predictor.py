import numpy as np
from tflite_runtime.interpreter import Interpreter
import smbus2 as smbus
import tensorflow as tf

class RealTimePredictor:
    I2C_ADDR = 0x68
    PWR_MGMT_1 = 0x6B
    ACCEL_XOUT_H = 0x3B
    GYRO_XOUT_H = 0x43

    WINDOW_SIZE = 20
    LABELS = np.array(['DANGEROUS TIPPING', 'STABLE', 'STRONG VIBRATION'])

    min_values = np.array([-2.0, -2.0, -2.0, -250.0, -250.0, -250.0])
    max_values = np.array([2.0, 2.0, 2.0, 250.0, 250.0, 250.0])

    def __init__(self, model_path, delegate=None):
        self.bus = smbus.SMBus(1)
        self.bus.write_byte_data(self.I2C_ADDR, self.PWR_MGMT_1, 0)

        if delegate:
            self.interpreter = Interpreter(model_path=model_path, experimental_delegates=[delegate])
        else:
            self.interpreter = Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.sensor_buffer = []


    def load_flex_delegate(self):
        try:
            return tf.lite.experimental.load_delegate('libtensorflowlite_flex.so')
        except Exception as e:
            print(f"⚠️ Không tải được Flex delegate: {e}")
            return None

    def read_raw_data(self, addr):
        high = self.bus.read_byte_data(self.I2C_ADDR, addr)
        low = self.bus.read_byte_data(self.I2C_ADDR, addr + 1)
        value = (high << 8) | low
        if value > 32767:
            value -= 65536
        return value

    def get_sensor_data(self):
        accel_x = self.read_raw_data(self.ACCEL_XOUT_H)
        accel_y = self.read_raw_data(self.ACCEL_XOUT_H + 2)
        accel_z = self.read_raw_data(self.ACCEL_XOUT_H + 4)
        gyro_x = self.read_raw_data(self.GYRO_XOUT_H)
        gyro_y = self.read_raw_data(self.GYRO_XOUT_H + 2)
        gyro_z = self.read_raw_data(self.GYRO_XOUT_H + 4)

        ax = accel_x / 16384.0
        ay = accel_y / 16384.0
        az = accel_z / 16384.0
        gx = gyro_x / 131.0
        gy = gyro_y / 131.0
        gz = gyro_z / 131.0

        return [ax, ay, az, gx, gy, gz]

    def predict(self):
        data = self.get_sensor_data()
        self.sensor_buffer.append(data)

        if len(self.sensor_buffer) < self.WINDOW_SIZE:
            return None, None  # Chưa đủ dữ liệu để dự đoán

        window = np.array([self.sensor_buffer[-self.WINDOW_SIZE:]], dtype=np.float32)
        normalized = (window - self.min_values) / (self.max_values - self.min_values + 1e-8)
        normalized = normalized.astype(np.float32)

        self.interpreter.set_tensor(self.input_details[0]['index'], normalized)
        self.interpreter.invoke()
        output = self.interpreter.get_tensor(self.output_details[0]['index'])

        idx = np.argmax(output)
        state = self.LABELS[idx]
        confidence = output[0][idx]

        self.sensor_buffer.pop(0)
        return state, confidence

    def close(self):
        self.bus.close()
