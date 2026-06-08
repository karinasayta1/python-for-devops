import psutil
import smtplib, ssl
from email.message import EmailMessage

def get_health(cpu,mem,disk):
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage= psutil.virtual_memory().percent
    disk_usage= psutil.disk_usage('/').percent

    msg_body = {"CPU Usage" : f"{cpu_usage}%  LOWER THAN THRESHOLD({cpu}%)",
                 "Memory Usage" : f"{mem_usage}%  LOWER THAN THRESHOLD({mem}%)",
                 "Disk Usage" : f"{disk_usage}%  LOWER THAN THRESHOLD({disk}%)"}
    if cpu_usage > cpu:
        msg_body["CPU Usage"] = f"{cpu_usage}%  HIGHER THAN THRESHOLD({cpu}%)"
    if mem_usage > mem:
        msg_body["Memory Usage"] = f"{mem_usage}%  HIGHER THAN THRESHOLD({mem}%)"
    if disk_usage > disk:
        msg_body["Disk Usage"] = f"{disk_usage}%  HIGHER THAN THRESHOLD({disk}%)"

    sender_email = "afsk1997@gmail.com"  
    receiver_email = "afsk1997@gmail.com"  
    app_password = "**** **** **** ****"  # Replace with your App Password

    # Create the email message
    msg = EmailMessage()
    msg.set_content("\n".join([f"{k} : {v}" for k,v in msg_body.items()]))
    msg['Subject'] = "Alert Notification"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Gmail SMTP server settings
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()


    if any("HIGHER" in v for v in msg_body.values()):
        try:
        # Connect to the server and send the email
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, app_password)
                server.send_message(msg)
                print("Email sent successfully!")
        except smtplib.SMTPAuthenticationError:
            print("Authentication error: Check your email/app password.")
        except Exception as e:
            print(f"An error occurred: {e}")
    return msg_body

#print(get_health(50,1,50))