import argparse
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass

def email():
    email_user = input("Introduce tu correo: ")
    email_password = getpass.getpass("Introduce tu contraseña: ")
    email_send = input("Email receptor: ")
    subject = input("Asunto: ")
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    body = input("Ingresa el cuerpo del correo: ")
    msg.attach(MIMEText(body,'plain'))
    filename= input("Introduce el nombre archivo a enviar: ")
    attachment  =open(filename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()
    print("Correo enviado a "+ email_send)
email()