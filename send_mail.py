import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "COVID - 19"
body = "This is an email with attachment sent from your own COVID Tracker"
body += f'\n\nTotal Cases in India as of {india.name} are \nConfirmed = {india[0]} \nActive Cases = {india[3]} \nDeaths = {india[1]} \nRecoveries = {india[2]} \n\n'
india = i
body += f'Your predictions as of {dt.datetime.now().strftime("%b %d, %Y")} are \nConfirmed = {india[0]} \nActive Cases = {india[3]} \nDeaths = {india[1]} \nRecoveries = {india[2]} \n\n'

sender_email = os.environ['EMAIL_USER']
receiver_email = "itsmanpreetsinghjuneja@gmail.com"
password = os.environ['EMAIL_PASS']

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

filename = "results.xlsx"

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
