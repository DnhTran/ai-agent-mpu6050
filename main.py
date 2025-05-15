import time
from datetime import datetime
from agent_core.real_time_predictor import RealTimePredictor
from agent_core.explainer import explain_state
from agent_core.logger import log_state
from agent_core.notifier import send_alert
from tflite_runtime.interpreter import load_delegate
from web_api import app, update_status

import os

print("EMAIL_SENDER:", os.getenv("EMAIL_SENDER"))
print("EMAIL_RECEIVER:", os.getenv("EMAIL_RECEIVER"))
print("EMAIL_PASSWORD:", os.getenv("EMAIL_PASSWORD"))

MODEL_PATH = '/home/NOISE/ai_agent_mpu6050/models/lstm_model.tflite'
ALERT_THRESHOLD = 5

def main():
    # Thử tải flex delegate (nếu model dùng ops đặc biệt)
    try:
        flex_delegate = load_delegate('libtensorflowlite_flex.so')
        print("✅ Flex delegate loaded.")
    except OSError:
        print("⚠️ Không tải được Flex delegate, sử dụng interpreter mặc định.")
        flex_delegate = None

    # Khởi tạo RealTimePredictor với delegate (nếu có)
    predictor = RealTimePredictor(model_path=MODEL_PATH, delegate=flex_delegate)

    error_count = 0

    try:
        print("🚀 AI Agent bắt đầu chạy...")

        while True:
            state, confidence = predictor.predict()
            print(f"DEBUG: state={state}, confidence={confidence}, error_count={error_count}")

            if state is None:
                time.sleep(0.05)
                continue

            message = explain_state(state)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_state(timestamp, state, confidence, message)

            print(f"[{timestamp}] Trạng thái: {state} - Độ tin cậy: {confidence:.2f} - {message}")

            if state in ['DANGEROUS TIPPING', 'STRONG VIBRATION']:
                error_count += 1
                if error_count >= ALERT_THRESHOLD:
                    alert_msg = (
                        f"Cảnh báo: Trạng thái '{state}' xuất hiện liên tiếp {error_count} lần.\n"
                        f"Chi tiết: {message}"
                    )
                    print("⚠️ Đã đạt ngưỡng cảnh báo! Chuẩn bị gửi email...")
                    send_alert(alert_msg)
                    print("📧 Đã gửi email cảnh báo.")
                    error_count = 0
            else:
                error_count = 0

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\n⏹️ AI Agent dừng lại.")
    finally:
        predictor.close()

if __name__ == '__main__':
    main()
