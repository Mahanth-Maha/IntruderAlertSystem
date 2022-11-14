import os
import smtplib
import datetime
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Changed this code for secuirty purposes
Pi_MAddr = 'rasberrypi.jntua@gmail.com'
Pi_MPswd = 'JNTUA@500'
Client_Maddr = 'pics.general.backup.maha@gmail.com'


def SendMail():
    mail = MIMEMultipart()
    mail['Subject'] = 'COMMANDER WE HAVE AN INTRUDER !'
    mail['From'] = Pi_MAddr
    mail['To'] = Client_Maddr

    text = MIMEText(
        "Sir,\n\n\tWe have an Intruder, please take a look ! here are pictures...\n\n\n Happy Hunting...John Wick")
    mail.attach(text)

    # for ImgFileName in images:
    #     with open(ImgFileName, 'rb') as f:
    #         img_data = f.read()
    #     image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    #     mail.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(Pi_MAddr, Pi_MPswd)
    s.sendmail(Pi_MAddr, Client_Maddr, mail.as_string())
    s.quit()



# print("Movement Detected ! Clicking a Pictures...")
# tm = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
# images = []
# taken = 0
# for taken in range(No_of_Pictures):
    # print("Picture "+str(taken) + "... And Smile...", end=' ')
    # RPI_Camera.resolution = (1024, 768)
    # store_at = './out_img/image' + str(tm) + str(taken) + '.jpg'
    # images.append(store_at)
    # RPI_Camera.capture(store_at)
    # if (taken != No_of_Pictures):
    #     print("nice one ! One More...Stay Still")
    #     sleep(No_of_Pictures/2)
    # else:
        # print("Great Pictures...!")
print("Sending Mail...", end=' ')
SendMail()
print("Affrimative !")

# Not to capture immediately
# sleep(10)
