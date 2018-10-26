import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pirPin=6
GPIO.setup(pirPin,GPIO.IN)
counter=1
time.sleep(4)
while counter<=4:
    if GPIO.input(pirPin):
        print("Motion Detected")
        os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/kishore/"+str(counter)+".jpg")
        print("pic captured")
        time.sleep(1)
        counter = counter + 1
print("Testing")
exit()
