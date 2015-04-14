import RPi.GPIO as GPIO
import time
import subprocess

now = time.strftime("%d/%m/%Y-%H:%M:%S")
#print("start" + now)

#vcc connected to 5V, GND to ground and 
# out connected to logical PIN 14 will use BCM board
sensor = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
current_state = False

while True:
    time.sleep(0.1)
    #print("done sleep check now")
    current_state = GPIO.input(sensor)
    if current_state:
        subprocess.call(["sudo", "/usr/bin/motion", "start"])
        subprocess.call(["/home/pi/my_scripts/manage_dropbox_upload.sh", "start"])
        time.sleep(900)
        current_state = False
        subprocess.call(["sudo", "service", "motion", "stop"])
        subprocess.call(["/home/pi/my_scripts/manage_dropbox_upload.sh", "stop"], shell=False)
	#print("Done inside loop")
    #print("done outside loop")
