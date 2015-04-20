import subprocess
import re

print("Checking up on the processes")

p = subprocess.Popen(["ps", "-ef"], stdout=subprocess.PIPE)
(output, err) = p.communicate()

appProcess = []

for line in re.split('\n', output):
    if re.search("startGPIOMotionSensor.py", line):
        appProcess = line.split();
        print "Killing process " + appProcess[1]
        pid = appProcess[1]
	subprocess.call(["sudo", "kill", "-9", pid])

subprocess.call(["sudo", "service", "motion", "stop"])
subprocess.call(["/home/pi/my_scripts/manage_dropbox_upload.sh", "stop"], shell=False)

