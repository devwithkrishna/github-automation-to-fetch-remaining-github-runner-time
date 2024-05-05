import base64
import os
from datetime import datetime
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName, Content,
    FileType, Disposition, ContentId)
from sendgrid import SendGridAPIClient
from dotenv import load_dotenv
from jinja2 import Environment,FileSystemLoader

def formatted_datetime():
    # Get current date and time
    now = datetime.now()

    # Format date and time as dd:mm:yyyy hh:minur
    formatted_date_time = now.strftime("%d-%m-%Y %H:%M")
    return formatted_date_time

def build_attachments(filepath:str):
    attachments = []
    json_files = []
    for filename in os.listdir(filepath):
        if filename.endswith(".json"):
            full_filepath = os.path.join(filepath, filename)
            with open(full_filepath, 'rb') as f:
                data = f.read()
            encoded = base64.b64encode(data).decode()
            attachment = Attachment()
            attachment.file_content = FileContent(encoded)
            attachment.file_type = FileType('application/json')
            attachment.file_name = FileName(filename)
            attachments.append(attachment)
            json_files.append(filename)

    return attachments, json_files

def send_email_with_sendgrid(attachments: None, json_files=None):
    """
    send email using sendgrid.
    json_files --> list of all json files generated
    :return:
    """
    # Variables for template
    repo_name = "github-automation-to-fetch-remaining-github-runner-time"
    org_name = 'devwithkrishna'
    username = 'githubofkrishnadhas'
    date = formatted_datetime()
    # Load the template file
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('email_template.html')

    # Render the template with dynamic data
    html_content = template.render(repo_name=repo_name, org_name=org_name, username=username, date=date, json_files=json_files)
    message = Mail(
        from_email='krishnadhas@devwithkrishna.in',
        to_emails='krishnadhasnk1997@gmail.com',
        subject=f'{ org_name } & { username } billing details - {date} ',
        html_content= Content("text/html", html_content)
    )
    if attachments:
        for attachment in attachments:
            message.add_attachment(attachment)

    try:
        load_dotenv()
        sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sendgrid_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

def main():
    """ To test the script"""
    attachments, json_files = build_attachments(filepath='.')
    send_email_with_sendgrid(attachments=attachments, json_files=json_files)

if __name__ == '__main__':
    main()