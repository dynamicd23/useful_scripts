#!/bin/bash

fileList=(`ls /home/pi/piCamPics/`)

noOfFiles=${#fileList[@]}

for i in "${fileList[@]}"
do
	/home/pi/dropbox/dropbox_uploader.sh upload /home/pi/piCamPics/$i /
	sudo rm -rf /home/pi/piCamPics/$i
done


if [ $noOfFiles -gt 0 ]
then

`more /home/pi/email_content/email_picam_motion_detected.txt | mail -t`

fi


#/home/pi/dropbox/dropbox_uploader.sh upload /home/pi/piCamPics/*.avi /
#sleep 5;
#sudo rm -rf /home/pi/piCamPics/*.jpg 
#sudo rm -rf /home/pi/piCamPics/*.avi 


exit;
