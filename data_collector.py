import csv
from agent_core.sensor_reader import read_sensor
import time

filename = "data/sensor_data_labeled.csv"
LABEL = input("Nhập nhãn dữ liệu (STRONG VIBRATION / DANGEROUS TIPPING / STABLE): ")

with open(filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'label'])

    print(f"[LOGGING STARTED] Ghi dữ liệu cho nhãn: {LABEL}")
    try:
        while True:
            data = read_sensor()
            writer.writerow([
                data['timestamp'],
                data['accel_x'],
                data['accel_y'],
                data['accel_z'],
                data['gyro_x'],
                data['gyro_y'],
                data['gyro_z'],
                LABEL
            ])
            time.sleep(0.05)  # 20Hz sampling
    except KeyboardInterrupt:
        print("\n[LOGGING STOPPED]")
