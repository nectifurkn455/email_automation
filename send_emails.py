import psycopg
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage


load_dotenv()

# Connect the postgresql database
conn = psycopg.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)
# Get the names and email addresses from the contacts table
cursor = conn.cursor()
cursor.execute('SELECT name, email FROM contacts')
recipients = cursor.fetchall()

# Email address that will send the messages
email_address = os.getenv('EMAIL_USER')
email_password = os.getenv('EMAIL_PASS')
# For each recipient send a mail and print a confirmation message
for name, email in recipients:
    msg = EmailMessage()
    msg.set_content(f'Hello {name}. This is your personalized test mail.')
    msg['Subject'] = 'Hello from Python'
    msg['From'] = email_address
    msg['To'] = email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_address, email_password)
        server.send_message(msg)
    print(f'Mail has been sent to {name}')