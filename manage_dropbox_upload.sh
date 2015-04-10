#!/bin/bash

# The following part always gets executed.
echo "upload script"

# The following part carries out specific functions depending on arguments.
case "$1" in
  start)
    echo "Starting"
    /home/pi/dropbox/start_wrapper.sh & 
    exit 0
    echo "hmm Ending"
    ;;
  stop)
    echo "Stopping"
    PID=`ps -ef | grep manage_dropbox_upload | awk 'BEGIN {pid=999999} {if($0 ~ /start/){pid=$2}} END {print pid}'`
    echo "Killing $PID.. All done. I am the bereaved"
     if [ $PID -lt 999999 ]
     then
	sudo kill -9 $PID
      fi
    PID2=`ps -ef | grep start_wrapper | awk 'BEGIN {pid=999998} {if($0 !~ /grep/){pid=$2}} END {print pid}'`
    echo "Killing $PID2.. All done. I am the bereaved" 
    if [ $PID2 -lt 999998 ]
     then
	sudo kill -9 $PID2
     fi
    ;;
  *)
    echo "Usage: /home/pi/my_scripts/upload_dropbox_pics_every_min.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
