import tensorflow as tf

# Load mô hình .h5
model = tf.keras.models.load_model('/home/NOISE/ai_agent_mpu6050/notebooks/models/lstm_model.h5')

# ✅ Export ra định dạng SavedModel (chính xác cú pháp cho Keras 3+)
model.export('/tmp/model_for_tflite')

# Khởi tạo converter
converter = tf.lite.TFLiteConverter.from_saved_model('/tmp/model_for_tflite')

# ✅ Cho phép sử dụng các ops mở rộng (cần thiết cho LSTM)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS
]

# ✅ Bắt buộc phải tắt lowering tensor list ops để tránh lỗi tf.TensorListReserve
converter._experimental_lower_tensor_list_ops = False

# Convert
tflite_model = converter.convert()

# Lưu mô hình TFLite
with open("../models/lstm_model.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ Convert thành công! Đã lưu: models/lstm_model.tflite")
