from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

def read_sensor():
    accel = sensor.get_accel_data()
    gyro = sensor.get_gyro_data()
    return {
        'timestamp': time.time(),
        'accel_x': accel['x'],
        'accel_y': accel['y'],
        'accel_z': accel['z'],
        'gyro_x': gyro['x'],
        'gyro_y': gyro['y'],
        'gyro_z': gyro['z']
    }
