# test_email.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent_core.notifier import send_alert

send_alert("🔔 Đây là email test từ hệ thống AI Agent.")
