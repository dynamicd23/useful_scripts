from bottle import route, run, template, request
import time
import subprocess
import re


#global variables
IP_ADDRESS=subprocess.check_output("ifconfig | grep 192 | awk '{split($2,a,\":\"); print a[2]}'", shell=True)
IP_ADDRESS=IP_ADDRESS.strip() #get IP address of the PI

now = time.strftime("%d/%m/%Y-%H:%M:%S")

#print(now)


@route('/')
def hello():
    return template('/home/pi/bottle/home.tpl')


@route('/startMotion', method='POST')
def startMotion():
    print('Trying to start the motion subprocess')
    subprocess.call(["sudo", "/usr/bin/motion", "start"])
    subprocess.call(["/home/pi/my_scripts/manage_dropbox_upload.sh", "start"])
    return '<h1>Motion started ' + now + '</h1>'


@route('/stopMotion', method='POST')
def stopMotion():
    print('Trying to stop the motion subprocess')
    subprocess.call(["sudo", "service", "motion", "stop"])
    subprocess.call(["/home/pi/my_scripts/manage_dropbox_upload.sh", "stop"], shell=False)
    return '<h1>Motion Stopped '+ now + '</h1>'


@route('/motionStatus', method='POST')
def motionStatus():
    print('Trying to get Motion Status')
    #p = subprocess.Popen(["ps", "-ef"], stdout=subprocess.PIPE)
    #(output, err) = p.communicate()
    #status = ' '
    #for line in re.split('\n', output):
    #if re.search("motion", ouput):
    #    status = output + '<br />'
    output=subprocess.check_output("ps -ef | grep motion", shell=True)
    return '<h1>' + now + '<br />' + output + '</h1>'


@route('/snapAndTweet', method='POST')
def snapAndTweet():
    print('Trying to take a snap and post a tweet')
    subprocess.call('/home/pi/my_scripts/snapAndTweet.sh')
    return '<h1>Check Twitter ' + now + '</h1>'

@route('/recordVideo', method='POST')
def recordVideo():
    print('Trying to record a 10 sec video')
    subprocess.call('/home/pi/my_scripts/recordVid.sh')
    return 'Check the video directory ' + now + '</h1>'

@route('/logTemp', method='POST')
def logTemp():
    print('Trying to log temperature of the PI')
    subprocess.call('/home/pi/my_scripts/heatTemperature.sh')
    return '<h1>Check the heat log ' + now + '</h1>'


try:
    print('Bottle Opened')
    run(host=IP_ADDRESS, port=80)
finally:
    print('Bottle Closed')
