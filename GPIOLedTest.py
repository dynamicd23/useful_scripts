import RPi.GPIO
import time
import sys


RPi.GPIO.setwarnings(False)

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(16, RPi.GPIO.OUT)
RPi.GPIO.setup(6, RPi.GPIO.OUT)

print 'Running ..' + sys.argv[0]
print 'Repeat >' + sys.argv[1]

def test_alternate (gpio1st, gpio2nd, sleepTime):
	
	repeat = int(sys.argv[1])

	while repeat >= 0:
		RPi.GPIO.output(gpio1st, True)
		RPi.GPIO.output(gpio2nd, False)
		time.sleep(sleepTime)
		RPi.GPIO.output(gpio1st, RPi.GPIO.LOW)
		RPi.GPIO.output(gpio2nd, RPi.GPIO.HIGH)
		time.sleep(sleepTime)
		repeat = repeat - 1

test_alternate(16, 6, 1)
RPi.GPIO.output(6, RPi.GPIO.LOW)
