import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

class Mail:
    def __init__(self, to_mail, content):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.host = "smtp.gmail.com"
        self.port = 587
        self.to_mail = to_mail
        self.content = content

    def send_mail(self):
        with smtplib.SMTP(self.host, port=self.port) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=f"Subject:New Message\n\n{self.content}"
            )