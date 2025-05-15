import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email):
    # Cấu hình Gmail
    from_email = "alertsystem019@gmail.com"  # Thay bằng email của bạn
    app_password = "jncv eiqm csbd xmwq"      # Dán mật khẩu ứng dụng vào đây

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)
        server.quit()
        print("✅ Email đã gửi thành công.")
    except Exception as e:
        print("❌ Lỗi khi gửi email:", str(e))
