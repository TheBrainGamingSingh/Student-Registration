def send_email(receiver_email, filename):
    import os
    import email, smtplib, ssl
    import datetime as dt
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = "Student Registration Slip"
    body = "This is an automated email. For any queries contact: itsmanpreetsinghjuneja@gmail.com"

    sender_email = os.environ['EMAIL_USER']
    password = os.environ['EMAIL_PASS']

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

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
        print('{} sent to {} at time {}'.format(filename,receiver_email,dt.datetime.now().strftime("%D %I:%M:%S %p")))
