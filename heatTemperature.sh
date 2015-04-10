#!/bin/bash

timestamp=`date +%F-%H%M`
threshold=50

temp=`vcgencmd measure_temp`
temp=${temp:5:16}
echo $timestamp"->"$temp >> /home/pi/tempLog/measureTemplog.txt

temp2=${temp:0:2}

if [ $temp2 -gt $threshold ] 
then 

echo "Threshold Crossed shutting down the PI" >> /home/pi/tempLog/measureTemplog.txt

`more /home/pi/email_content/email_temp_threshold_exceeded.txt | mail -t`

sleep 10

sudo shutdown -r now

fi

exit;
