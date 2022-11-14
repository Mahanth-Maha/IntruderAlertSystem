import datetime
from time import sleep
from picamera import PiCamera

RPI_Camera = PiCamera()

No_of_Pictures = 4

sleep(1)

print("Movement Detected ! Clicking a Pictures...")
tm = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
images = []
taken = 0
for taken in range(No_of_Pictures):
    print("Picture "+str(taken) + "... And Smile...", end=' ')
    RPI_Camera.resolution = (1024, 768)
    store_at = './out_img/image' + str(tm) + str(taken) + '.jpg'
    # images.append(store_at)
    RPI_Camera.capture(store_at)
    if (taken != No_of_Pictures):
        print("nice one ! One More...Stay Still")
        sleep(No_of_Pictures/2)
    else:
        print("Great Pictures...!")
print("Sending Mail...", end=' ')
# SendMail(images)
print("Affrimative !")

# Not to capture immediately
# sleep(10)
