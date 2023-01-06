import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.functions import data_for_email_sender, send_emails


def main():
    """Send an email with the top 5 posts of each subreddit from the past week.
    The email is sent through a Gmail account. The email address and password of the account are read
    from environment variables 'GMAIL_EMAIL' and 'GMAIL_PASSWORD', respectively.
    """
    # Get email body
    email_body = data_for_email_sender()
    # Get email and password from env variables
    GMAIL_EMAIL = os.environ.get('GMAIL_EMAIL')
    GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')
    # Connect to smtp and login
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(GMAIL_EMAIL, GMAIL_PASSWORD)
    # Prepare message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Reddit top posts from last week"
    msg_body = MIMEText(email_body, 'html')
    msg.attach(msg_body)
    # Send email to every recipient
    send_emails(server, msg)
    # Break connection
    server.quit()


if __name__ == '__main__':
    main()
