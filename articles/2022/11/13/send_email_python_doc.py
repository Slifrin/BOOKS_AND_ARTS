"""
    https://docs.python.org/3/library/email.examples.html
"""

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
from pathlib import Path


my_dir: Path = Path(__file__).parent
textfile = my_dir / "say_hello.txt"

textfile_v2 = Path("say_hello.txt")

# Open the plain text file whose name is in textfile for reading.
with textfile.open() as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

print(msg)
print(textfile_v2.read_text())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = 'blabla@tmp.com'
msg['To'] = 'bla.bla@gmail.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()