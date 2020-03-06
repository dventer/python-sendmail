import smtplib, ssl
import socks

#socks.setdefaultproxy(TYPE, ADDR, PORT)
socks.setdefaultproxy(socks.HTTP, '10.1.1.1', 8081)
socks.wrapmodule(smtplib)
smtp_server = "smtp.office365.com"
port = 587  # For starttls
sender = "sender@example.com"
password = 'Password'
mssg = """\
Subject: Hi there

This message is sent from Python."""
recipient= 'recipient@example.com'
# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender, password)
    server.sendmail(sender, recipient, mssg)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()