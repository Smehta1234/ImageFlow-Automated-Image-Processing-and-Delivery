import smtplib
import os
import argparse
from email.message import EmailMessage
from email.utils import formataddr
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass


def send_email_with_attachment(sender_email, receiver_email, subject, body, file_path, smtp_server, smtp_port):
    # Create the email message
    msg = EmailMessage()
    msg['From'] = formataddr(('Your Name', sender_email))
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Convert to multipart to allow attachments
    msg.make_mixed()

    # Attach the file
    with open(file_path, 'rb') as f:
        mime = MIMEBase('application', 'octet-stream')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        mime.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
        msg.attach(mime)

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        password = getpass(f"Enter the password for {sender_email}: ")
        server.login(sender_email, password)
        server.send_message(msg)
        print(f"Email sent successfully to {receiver_email} with attachment {file_path}")


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Send a ZIP file to an email address')

    # Add arguments
    parser.add_argument('file_path', type=str, help='Path to the ZIP file to send')
    parser.add_argument('receiver_email', type=str, help='Receiver email address')

    # Parse the arguments
    args = parser.parse_args()

    # Email details
    sender_email = "smehta2_be22@thapar.edu"  # Replace with your email address
    subject = "Here is your ZIP file"
    body = "Please find the attached ZIP file."
    smtp_server = "smtp.gmail.com"  # SMTP server for Gmail
    smtp_port = 587  # Port for TLS/STARTTLS

    # Call the send email function
    send_email_with_attachment(sender_email, args.receiver_email, subject, body, args.file_path, smtp_server, smtp_port)
