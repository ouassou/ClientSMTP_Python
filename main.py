
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import re

# we can use any server like smtp.google.com

server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
# log to our account
# server.login("mail@mail.com","password123") # or
# we should encrypt our password in a file txt!! it's recommended

with open("password", "r") as file:
    password = file.read()

server.login("rihamouassou@gmail.com", password)

#start creating the message, we will create a message/mail

message = MIMEMultipart()
while True:
    print("entrez votre nom :")
    name = input()
    if any(char.isdigit() for char in name):
        print (" Try without numbers")
    else:
        message['From'] = name
        break

while True:
    print("a qui vous envoyez ?")
    mail = input()

    if re.match(r"[^@]+@[^@]+\.[^@]+", mail):
        print("address is valid")
        message['To'] = mail
        break
    else:
        print("not valid")
        print("Try Again")


print("Sujet de votre mail")
message['Subject'] = input()

with open('message', 'r') as mess:
    my_message = mess.read()

# This how we add a header and test to object
message.attach(MIMEText(my_message, 'plain'))

# This how to attach an image to our message
filename = "koala.jpg"
attachment = open(filename, 'rb') #rb = reading byte because we're reading an image

#creat a payload object

pl = MIMEBase('application', 'octet-stream')
pl.set_payload(attachment.read())

encoders.encode_base64(pl)
pl.add_header('Content-Disposition', f'attachment; filename={filename}')
message.attach(pl)

text = message.as_string()
server.sendmail('rihamouassou@gmail.com', 'ri-ha-m@hotmail.fr', text)

