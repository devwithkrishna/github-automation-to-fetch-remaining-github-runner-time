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
def send_email_with_sendgrid():
    """
    send email using sendgrid.
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
    html_content = template.render(repo_name=repo_name, org_name=org_name, username=username, date=date)
    message = Mail(
        from_email='krishnadhas@devwithkrishna.in',
        to_emails='krishnadhasnk1997@gmail.com',
        subject=f'{ org_name } & { username } billing details ',
        html_content= Content("text/html", html_content)
    )
    file_path = 'org_billing_details.json'
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/json')
    attachment.file_name = FileName('org_billing_details.json')
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
        print(e)

def main():
    """ To test the script"""
    send_email_with_sendgrid()

if __name__ == '__main__':
    main()