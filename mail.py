import smtplib, ssl
import configparser

def send_mail():

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "mjan72771@gmail.com"
    receiver_email = "mjan72771@gmail.com"

    config = configparser.ConfigParser()

    with open('mail.cfg') as f:
        config.read_file(f)

    port = config['email']['port']
    smtp_server = config['email']['smtp']
    sender_email = config['email']['sender']
    receiver_email = config['email']['receiver']

    # password = input("Type your password and press enter:")
    with open('gmail_password.txt') as f:  
        password = f.read()
    message = """Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    send_mail()