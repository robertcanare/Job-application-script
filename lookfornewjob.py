#!/usr/bin/env python3                                
# Just a simple script to automate my job application

import argparse
import base64
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# get user input
parser = argparse.ArgumentParser(description='Simple script to automate my job application.')
parser.add_argument('--recruitment_email', required=True, help='Recruitment email')
# parser.add_argument('--sender_email', required=True, help='Sender email')
parser.add_argument('--recruiter_name', required=True, help='Recruitment name')
parser.add_argument('--company_name', required=True, help='Company name')
parser.add_argument('--role', required=True, help='Job role')
# parser.add_argument('--password', required=True, help='Email password')
parser.add_argument('--skills_1', required=True, help='Skills set 1')
parser.add_argument('--skills_2', required=True, help='Skills set 2')
parser.add_argument('--skills_3', required=True, help='Skills set 3')
args = parser.parse_args()

################################################################
# Encode password first
# data = "password"
#
# # Standard Base64 Encoding
# encodedBytes = base64.b64encode(data.encode("utf-8"))
# encodedStr = str(encodedBytes, "utf-8")
#
# print(encodedStr)
###############################################################

# credentials
email = 'email'
encoded_password = "encoded_password"

# Decode password, yeah it's pretty easy to decode it.
decodedBytes = base64.b64decode(encoded_password)
decodedStr = str(decodedBytes, "utf-8")
password = decodedStr

mail_content = '''Dear {},

This letter is to express my interest in your job post for {} position, I have extensive experience on operations of business system relevant to your organization’s niche, and I think the skills I’ve amassed
through this experience make me a great fit for {}. I am confident I will be an asset to your organization for those very reasons.    
    
Here are the skills and qualifications I think make me the optimal candidate:
{}
{}
{}

I’ve attached a copy of my resume that details my experience, I look forward to speaking with you about this employment opportunity.

Best Regards,

Robert John Canare
Applicant
'''.format(args.recruiter_name, args.role, args.company_name, args.skills_1, args.skills_2, args.skills_3)

message = MIMEMultipart()
message['From'] = email
message['To'] = args.recruitment_email
message['Subject'] = 'A job application for {}'.format(args.role)
message.attach(MIMEText(mail_content, 'plain'))

# attach resume
attach_file_name = 'robert-john-canare-cv.pdf'
attach_file = open(attach_file_name, 'rb')
payload = MIMEBase('application', 'pdf', Name='robert_john_cv')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(email, password)
text = message.as_string()
session.sendmail(email, args.recruitment_email, text)
session.quit()

print('Mail Sent')
