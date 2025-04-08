from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv()

email_address = os.getenv('EMAIL_USER')
email_password = os.getenv('EMAIL_PASS')
receiver = 'furkanercin@hacettepe.edu.tr'


msg = MIMEText('This is a test message. I hope it finds you well.')
msg['Subject'] = 'Test email using MIMEText'
msg['From'] = email_address
msg['To'] = receiver

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(email_address, email_password)
    server.send_message(msg)