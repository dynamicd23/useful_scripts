#!/bin/bash
vncserver -kill :0
vncserver -kill :1
vncserver -kill :2 
sudo rm -rf /tmp/.X*-lock
sudo rm -rf /tmp/.X11-unix/X*
sudo rm -rf /tmp/.*-pi
rm -rf /home/pi/.vnc/*.log
rm -rf /home/pi/.vnc/*.pid
vncserver


