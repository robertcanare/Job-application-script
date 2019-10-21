#!/usr/bin/env python3                                
#Just a simple script to automate my job application


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_address = 'sender@gmail.com'
sender_pass = 'password'
receiver_address = 'receive@gmail.com'

possition = 'SOC analyst'

mail_content = '''body,

body1

        body2
        
        body3
        
body4
'''

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A job application for {}'.format(possition)

message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'robert-john-canare-cv.pdf'
attach_file = open(attach_file_name, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)

payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()

print('Mail Sent')
