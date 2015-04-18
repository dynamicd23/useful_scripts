#!/bin/bash

current_time=$(date "+%Y%m%d-%H%M%S")

raspistill -t 1000 -o /home/pi/twitter/tweetPics/mypicture_$current_time.jpg


if [ "$1" != "" ]; then
    echo "Positional parameter $1"
    python3 /home/pi/twitter/postTweets.py "$1"

else
    echo "Positional parameter 1 is empty" 
    python3 /home/pi/twitter/postTweets.py

fi


exit;
