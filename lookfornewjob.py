#!/usr/bin/env python3                                
#Just a simple script to automate my job application

import smtplib
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#parse
parser = argparse.ArgumentParser(description='Simple script to automate my job application.')
parser.add_argument('--recruitment_email', required=True, help='Recruitment email')
parser.add_argument('--sender_email', required=True, help='Sender email')
parser.add_argument('--recruiter_name', required=True, help='Recruitment name')
parser.add_argument('--company_name', required=True, help='Company name')
parser.add_argument('--role', required=True, help='Job role')
parser.add_argument('--password', required=True, help='Email password')
parser.add_argument('--skills_1', required=True, help='Skills set 1')
parser.add_argument('--skills_2', required=True, help='Skills set 2')
parser.add_argument('--skills_3', required=True, help='Skills set 3')
args = parser.parse_args()

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
message['From'] = args.sender_email
message['To'] = args.recruitment_email
message['Subject'] = 'A job application for {}'.format(args.role)

message.attach(MIMEText(mail_content, 'plain'))

#attach resume
attach_file_name = '/root/Desktop/robert-john-canare-cv.pdf'
attach_file = open(attach_file_name, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)

payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(args.sender_email, args.password)
text = message.as_string()
session.sendmail(args.sender_email, args.recruitment_email, text)
session.quit()

print('Mail Sent')