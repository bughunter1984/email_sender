import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "mallotest.python@outlook.com"
email["to"] = "mallofrench05@gmail.com"
email["subject"] = "Hello"

email.set_content(html.substitute(name="Tom"), "html")

with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mallotest.python@outlook.com", "MalloTest.Pyth0n")
    smtp.send_message(email)
    print("Your message has been sent")
