#!/bin/bash

current_time=$(date "+%Y%m%d-%H%M%S")

raspistill -t 1000 -o /home/pi/twitter/tweetPics/mypicture_$current_time.jpg

python3 /home/pi/twitter/postTweets.py

exit;
