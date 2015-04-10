#!/bin/bash

current_time=$(date "+%Y%m%d-%H%M%S")

raspivid -t 2000 -fps 25 -o myvideo.h264

sleep 5;

MP4Box -add myvideo.h264 /home/pi/myvideo_$current_time.mp4

rm -r myvideo.h264 

#python3 /home/pi/twitter/postTweets.py

exit;
