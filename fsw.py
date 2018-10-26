import os
i=1
while(i<=5):
    os.system("fswebcam -F 4 --fps 20 -r 1200*800 /home/pi/kishore/"+str(i)+".jpg")
    i=i+1
    print("picture captured")
