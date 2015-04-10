#!/bin/bash

echo "Starting wrapper"
    while [ true ]
        do
                sudo su - pi -c "/home/pi/dropbox/uploadPics.sh &"
                sleep 180
        done
echo "Ending wrapper"
