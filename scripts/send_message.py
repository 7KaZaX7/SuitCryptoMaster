import smtplib
from email.mime.text import MIMEText


EMAIL_SENDER = "dashaerevanlogican@gmail.com"
EMAIL_RECEIVER = "tanya123456789225@gmail.com"
EMAIL_PASSWORD = "wmjf oejo terx zywe"


def send(message_data: str, subject_data: str):
    # Connect to the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login to the email sender's account
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)

    # Create an email message with the subject and message
    msg = MIMEText(message_data)
    msg["Subject"] = f"{subject_data}"

    # Send the email
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
