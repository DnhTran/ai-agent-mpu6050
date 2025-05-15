import os
import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    import smtplib
    from email.mime.text import MIMEText
    import os

    sender = os.getenv("EMAIL_SENDER")
    receiver = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")

    print(f"DEBUG: sender={sender}, receiver={receiver}, password_len={len(password) if password else 0}")

    if not sender or not receiver or not password:
        print("❌ ERROR: Missing email credentials!")
        return

    msg = MIMEText(message)
    msg['Subject'] = 'AI Agent Alert'
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, msg.as_string())
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
