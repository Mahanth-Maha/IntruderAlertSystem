from Google import Create_Service
import base64
# from gpiozero import MotionSensor
from picamera import PiCamera
import os
import smtplib
import datetime
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime. multipart import MIMEMultipart

RPI_Camera = PiCamera()

No_of_Pictures = 4

# Auth2 Google API setup
CLIENT_SECRET_FILE = 'secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

def SendMail(images):
    emailMsg = 'Sir,\n\n\tWe have an Intruder, please take a look ! here are pictures...\n\n\n Happy Hunting...John Wick\n'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] ='pics.general.backup.maha@gmail.com'
    mimeMessage['subject'] = "COMMANDER WE HAVE AN INTRUDER !"
    # text = MIMEText(emailMsg)
    # mimeMessage.attach(text)
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    for ImgFileName in images:
        with open(ImgFileName, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        mimeMessage.attach(image)
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)

# pip install -upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib