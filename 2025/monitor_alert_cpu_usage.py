import psutil
import shutil
from datetime import datetime
import smtplib
import platfrom
from email.mime.text import MIMEText
total, used, free = shutil.disk_usage("c:/")
used_in_percentage = (used / total) * 100
print(round(used_in_percentage))
cpu_usage = psutil.cpu_percent(interval=1)
print(round(cpu_usage))
memory_usage = psutil.virtual_memory()
print(memory_usage)
sender_email= "psiba73@gmail.com"
sender_passwd = "Pass@123"
alert_email= "sibaprasadbisoi08@gmail.com" 
smtp_server = "smtp.gmail.com"
smtp_port = 587
def send_alert_mail(subject, body):
    msg = MIMEText(body)
    msg['from']= sender_email
    msg['to']= alert_email
    msg['subject']= subject
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_passwd)
            smtp.send_message(msg)
    except Exception as e:
        print(f"failed to send email: {e}")