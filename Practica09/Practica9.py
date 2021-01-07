from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import sys

#Archivo que se usara para el envio de documentos

m=[]
data = {}
with open('data.json') as f:
        data = json.load(f)
msg = MIMEMultipart()

msg['From']= data['user']
msg['Subject']= str(sys.argv[1])
message= str(sys.argv[2])

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.office365.com:587')

server.starttls()

server.login(data['user'], data['pass'])

g= open('Mails.txt','r')
for line in g:
    to=line
    m.append(to)
g.close

for element in m:
    print(element)
    msg['To']= element
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("successfully sent email to %s:" % (msg['To']))
server.quit()
