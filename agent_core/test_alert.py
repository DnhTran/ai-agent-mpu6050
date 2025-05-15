# agent_core/test_alert.py
from agent_core.explainer import explain_state

if __name__ == "__main__":
    test_inputs = [
        "STRONG VIBRATION",
        "DANGEROUS TIPPING",
        "STABLE"
    ]

    for label in test_inputs:
        explanation = explain_state(label)
        print(f"[{label}] ➜ {explanation}")
from agent_core.email_sender import send_email

# Gửi khi cảnh báo
send_email("Cảnh báo rung mạnh", "Thiết bị đang rung mạnh bất thường!", "nguoi_dung@example.com")
