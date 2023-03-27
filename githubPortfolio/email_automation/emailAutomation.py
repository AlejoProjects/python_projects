import os
import ssl
import smtplib
import pandas as pd
from email.message import EmailMessage
'''
This script takes a .csv file with different emails, then sends and email to each one of those emails, where the content is in  a readed .txt fiile
'''
def getMessage():
    '''
    abre el file contenido.txt y guarda todas las lineas del archivo
    '''
    with open("contenido.txt") as f:
        lines = f.readlines()
    text = ''
    for i in range(0,len(lines)):
        text += lines[i]
    return text
def getEmails():
        '''
        Guarda los emails encontrados en la primera columna del csv y luego lo convierte en una lista
        '''
        emails = pd.read_csv('emailsHoja 1.csv')
        emails = list(emails['emails'])
        return emails
def sendEMail():
        emails = getEmails()
        print(emails)
        email_sender = 'EMAIL_ACCOUNT'
        email_password = os.environ.get("INCLUDE PASSWORD")
        email_receiver = emails
        subject = "this is a test"
        body = getMessage()
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = ", ".join(email_receiver)
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender,email_receiver, em.as_string())
              
sendEMail()