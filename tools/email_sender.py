import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject, body_html, to_email):
    from_email = "mytest23052001@gmail.com"     # ✅ Replace with your Gmail
    APP_PASSWORD = os.getenv("AGENT_TASKFORCE_APP_PASSWORD")
     

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    msg.attach(MIMEText(body_html, "html"))

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(from_email, APP_PASSWORD)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", str(e))
