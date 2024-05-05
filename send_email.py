import base64
import os
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from sendgrid import SendGridAPIClient
from dotenv import load_dotenv

repo_name = "github-automation-to-fetch-remaining-github-runner-time"
org_name = 'devwithkrishna'
username = 'githubofkrishnadhas'
message = Mail(
    from_email='krishnadhas@devwithkrishna.in',
    to_emails='krishnadhasnk1997@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    plain_text_content="Please check your weekly runner details",
    html_content='<strong> 123 and easy to do anywhere, even with Python 321</strong>'
)
file_path = 'org_billing_details.json'
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('application/json')
attachment.disposition = Disposition('attachment')
message.attachment = attachment
try:
    load_dotenv()
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID-API-KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))
