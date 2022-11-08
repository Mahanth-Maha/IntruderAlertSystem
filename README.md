# IntruderAlertSystem
This hardware can be used to detect Intruder who violates security.... or to capture any rare events by any trigger in environments such as wild photography...


## Version 1 -  Arduino

To Detect the movement, I tried to intergrate a fairly simple hardware HCSR-04 i.e, Ultra Sonic sensor to detect distance of an obstacle.

the entire project not required more than these 
* Arduino UNO    x 1
* HCSR04 sensor  x 1

* an 20amp LED
* Breadboard     x 1
* Some Jumper Wires

Code : [Arduino Src Code](/ID_V1/Arduino_Intruder_Detection.Cpp)

#### The Connection works as

![Arduino Setup](/img/Arduino_intruder_detection.jpeg)

It worked fine and can be used to send email to client a message stating the intruder has entered, but as a end user one cannot figure what or who entered, so it's pretty less powered so to power it up to make it capable to atleast send a picture to mail, may be a whole video... 

The Idea is good but the arduino is limited in nature so, it's time to upgrade

```
sudo apt upgrade
```

just kidding not this, i have upgraded the project to RasberryPi which has a native support for Camera to record a snap or video.


## Version 2 - RasberryPi

#### Requirements :

* Rasberry Pi (RPI) Board
* RPI Camera
* PIR (Proximity Infra Red) Sensor 
* RPI Power Adapter / Cable
* Micro SD Card

Debug Purpose :
* breadboard
* jumper wires
* LEDs and Resistors
* Push Buttons

- Libraries used 
  * gpiozero
  * picamera
  * email
  * smtplib

- install requirements with cmd

```
pip install -r ./ID_V2_pi/requirements.txt
```



