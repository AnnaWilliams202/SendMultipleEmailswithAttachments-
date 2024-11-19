import yagmail
import dotenv
import os



dotenv.load_dotenv()
password = os.getenv("GMAIL_PASSWORD")
sender = os.getenv("GMAIL_SENDER")

body = """
hi
        this is a test
        multiline text 3 quotes
        yagmail library
        .env hides password 
        create .env file and store password etc there 

Regards
Anna
"""
yag = yagmail.SMTP(sender, password)
with open("receivers.text", "r") as f:
    receivers = f.readlines()
for receiver in receivers:
    yag.send(to = receiver,
            contents = body,
            subject = 'test email',
             attachments = ['sample1.txt', 'sample2.txt'])

print(f'Emails sent successfully to {receivers}')