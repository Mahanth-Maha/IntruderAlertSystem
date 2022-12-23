#!/usr/bin/env python
"""
Example command-line app

This is a simple command-line app that accepts arguments and options,
performs some action, and outputs the results.

Usage:
  main.py [options] -m <mode> -c <client-id> [-g <gap>]

Arguments:
  <client-id> 
  <mode>
  <gap>

Options:
  -c --client   to specify the client address to send mail to 
  -g --gap      to specify the time for sucessive motion capture
  -m --mode     image : captures 4 images and sends them to mail\nvideo : send video to mail
  -h --help     Show this screen.
  -v --verbose  Enable verbose mode.
"""

from Google import Create_Service
import base64
import os
import smtplib
from subprocess import call
import subprocess
import datetime
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from gpiozero import MotionSensor
from picamera import PiCamera
from docopt import docopt
from email_validator import validate_email, EmailNotValidError
# pip install -upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
# Set up the LED
GPIO.setup(24, GPIO.OUT)

RPI_Camera = PiCamera()
# pinSense = 21
# pinSense = 18
# PIR_Sensor = MotionSensor(pinSense)

No_of_Pictures = 4

# Auth2 Google API setup
CLIENT_SECRET_FILE = 'secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
CLIENT_EMAIL_ID = None
GAP_TIME = 10 * 60


def SendMail_Img(images):
    emailMsg = 'Sir,\n\n\tWe have an Intruder, please take a look ! here are pictures...\n\nHappy Hunting...John Wick\n\n\nRegards,\nPi Bot'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = CLIENT_EMAIL_ID
    mimeMessage['subject'] = "COMMANDER WE HAVE AN INTRUDER !"
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    for ImgFileName in images:
        with open(ImgFileName, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        mimeMessage.attach(image)
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(
        userId='me', body={'raw': raw_string}).execute()
    print(message)


def SendMail_video(Captured):
    emailMsg = 'Sir,\n\n\tWe have an Intruder, please take a look at the Video...\n\nHappy Hunting...John Wick\n\n\nRegards,\nPi Bot'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = CLIENT_EMAIL_ID
    mimeMessage['subject'] = "COMMANDER WE HAVE AN INTRUDER !"
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))

    fp = open(Captured, 'rb')
    att = MIMEApplication(fp.read(), _subtype=".mp4")
    fp.close()
    att.add_header('Content-Disposition', 'attachment', filename=Captured)
    mimeMessage.attach(att)
    print("attach successful")

    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(
        userId='me', body={'raw': raw_string}).execute()
    print(message)


def CaptureImg():
    try:
        # if PIR_Sensor.motion_detected:
        if GPIO.input(18):
            GPIO.output(24, GPIO.HIGH)
            print("Motion detected!")
            sleep(1)
            print("Movement Detected ! Clicking a Pictures...")
            tm = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
            images = []
            taken = 0
            for taken in range(No_of_Pictures):
                print("Picture "+str(taken) + "... And Smile...", end=' ')
                RPI_Camera.resolution = (1024, 768)
                store_at = './out_img/image_' + str(tm) + str(taken) + '.jpg'
                images.append(store_at)
                RPI_Camera.capture(store_at)
                if (taken != No_of_Pictures):
                    print("nice one ! One More...Stay Still")
                    sleep(No_of_Pictures/2)
                else:
                    print("Great Pictures...!")
            print("Sending Mail...", end=' ')
            SendMail_Img(images)
            print("Affrimative !")

            # Not to capture immediately
            GPIO.output(24, GPIO.LOW)
            sleep(GAP_TIME)
        else:
            # Turn off the LED
            GPIO.output(24, GPIO.LOW)
            sleep(0.1)
    except KeyboardInterrupt:
        # Clean up the GPIO pins before exiting
        GPIO.cleanup()



def CaptureVid():
    try:
        # if PIR_Sensor.motion_detected:
        if GPIO.input(18):
            GPIO.output(24, GPIO.HIGH)
            print("Motion detected!")
            sleep(1)
            print("Movement Detected ! RECORDING Video...")
            tm = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
            # Video record
            RPI_Camera.resolution = (640, 480)
            RPI_Camera.rotation = 180
            Captured = './out_img/video_' + str(tm) + '.h264'
            mp4_file = './out_img/video_' + str(tm) + '.mp4'
            file_name = './out_img/video_' + str(tm)
            RPI_Camera.start_recording(Captured)
            RPI_Camera.wait_recording(30)
            RPI_Camera.stop_recording()
            # coverting video from .h264 to .mp4
            # command = f"MP4Box -add {file_name}.h264 {file_name}.mp4"
            # call([command], shell=True)
            subprocess.run(['ffmpeg', '-i', Captured, '-c:v', 'copy', '-c:a', 'copy', mp4_file])
            print("video converted")

            print("Sending Mail...", end=' ')
            SendMail_video(file_name+'.mp4')
            print("Affrimative !")
            os.remove(Captured)
            
            # Not to capture immediately
            GPIO.output(24, GPIO.LOW)
            sleep(GAP_TIME)
        else:
            # Turn off the LED
            GPIO.output(24, GPIO.LOW)
            sleep(0.1)
    except KeyboardInterrupt:
        # Clean up the GPIO pins before exiting
        GPIO.cleanup()

def CaptureImg_main():
    while True:
        print("Running capture")
        CaptureImg()
        sleep(1)


def CaptureVid_main():
    while True:
        print("Running capture")
        CaptureVid()
        sleep(30)


def main(verbose, mode, mode_id):
    if verbose:
        print("Verbose mode enabled defaultly")
    if mode:
        if mode_id == 'image':
            print('img mode')
            CaptureImg_main()
        elif mode_id == 'video':
            print('vid mode')
            CaptureVid_main()


def email_validate_with_err(mail_id):
    try:
        # Validate the email address
        valid = validate_email(mail_id)
        # Print the result
        if valid:
            print("The email address is valid")
            return True
        else:
            print("The email address is not valid")
            return False

    except EmailNotValidError as e:
        # The email address is not valid
        print("The email address is not valid: {}".format(str(e)))
        return False


if __name__ == '__main__':
    args = docopt(__doc__)
    verbose = args['--verbose']
    mode = args['--mode']
    mode_id = args['<mode>']
    client = args['--client']
    CLIENT_EMAIL_ID = args['<client-id>']
    gap = args['--gap']
    if gap:
        GAP_TIME = int(float(args['<gap>']))
    print(args)
    # Call the main function
    if mode and mode_id in ('image', 'video') and email_validate_with_err(CLIENT_EMAIL_ID):
        print(type(GAP_TIME),GAP_TIME)
        main(verbose, mode, mode_id)
