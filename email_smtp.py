import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Hello from Network Suite")
msg["Subject"] = "Test Mail"
msg["From"] = "you@gmail.com"
msg["To"] = "friend@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("you@gmail.com", "APP_PASSWORD")
    server.send_message(msg)
