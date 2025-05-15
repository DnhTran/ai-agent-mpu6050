# AI Agent MPU6050 - Real-time State Monitoring and Alert System

---
**Author**  
- Trần Cao Quốc Định 

📍 **University**: HCMC University of Technology and Education – HCMUTE  
📅 **Created**: *05/2025*

# 🤖 AI Agent MPU6050  
> **Real-time Motion State Monitoring & Alert System**

## 📌 Project Description
This project builds an AI Agent on Raspberry Pi to:
- 📈 Read motion data from MPU6050 sensor (via I2C)
- 🧠 Predict states ( *STABLE*, *DANGEROUS TIPPING*, *STRONG VIBRATION*) using a pre-trained **LSTM model (.tflite)**
- 📧 Send email alerts when dangerous states persist
- 🌐 Provide RESTful **Web API** for real-time state monitoring

---


**Project Structure:**
```
/ai_agent_mpu6050
│
├── agent_core/ # Core AI logic, status reasoning, email sender
├── models/ # LSTM .tflite model and dependencies
├── web_api.py # Flask API for real-time HTTP data access
├── main.py # Main script to launch the AI Agent
├── requirements.txt # Python dependencies
└── README.md # This guide
---
```
## ⚙️ Requirements

| Component        | Description                      |
|------------------|----------------------------------|
| Hardware         | Raspberry Pi 3/4/5 with Raspbian |
| Sensor           | MPU6050 via I2C                  |
| Python Version   | Python 3.7+                      |
| Required libs    | `numpy`, `tflite_runtime`, `flask`, `smtplib` |

---

## 🚀 Setup & Run

### 1. Create virtual environment and install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Configure email environment variables
```bash

export EMAIL_SENDER="your_email@gmail.com"
export EMAIL_PASSWORD="your_email_password"
export EMAIL_RECEIVER="receiver_email@gmail.com"
```
3. Run the AI Agent
```
python main.py
```
4. Run the API Server (optional)
```bash
python web_api.py
```
5. Access real-time status via API
```perl

http://<RaspberryPi_IP>:5000/state
```
✅ Main Features
Real-time state prediction from MPU6050

Logs status with timestamp and confidence

Sends email alert on dangerous state persistence

RESTful API to fetch live motion status

📝 Notes
The LSTM model is stored at models/lstm_model.tflite

Use tflite_runtime instead of full TensorFlow on Raspberry Pi for lightweight inference

The API currently has no frontend UI (use Postman or browser)

d.


