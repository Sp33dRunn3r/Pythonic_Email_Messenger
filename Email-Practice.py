#Using Python for Emails:
import smtplib
from email.message import EmailMessage
from string import Template

email = EmailMessage()
email['from'] = 'First Last'
email['to'] = 'Example_Email@email.com'
email['subject'] = 'You won... a really nice module!'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('python3email@email.com', 'password')
    smtp.send_message(email)
    print('all good boss!')
