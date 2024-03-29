"""
    https://www.atlassian.com/git/tutorials/git-hooks
"""


import smtplib
from email.mime.text import MIMEText
from subprocess import check_output


# Get the git log --stat entry of the new commit
log = check_output(['git', 'log', '-1', '--stat', 'HEAD'])

# Create a plaintext email message
msg = MIMEText("Look, I'm actually doing some work:\n\n%s" % log)

msg['Subject'] = 'Commit info'
msg['From'] = 'jurek@example.com'
msg['To'] = 'jurek.kiedrowski@gmail.com'

# Send the message
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
session.ehlo()
session.starttls()
session.ehlo()
session.login(msg['From'], 'secretPassword')

session.sendmail(msg['From'], msg['To'], msg.as_string())
session.quit()