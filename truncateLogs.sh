#!/bin/bash

cd /
sudo truncate nohup.out --size 0
cd /var/log
sudo rm *0*
sudo rm *1*
sudo rm *2*
sudo rm *3*
sudo rm *old*
sudo truncate * --size 0
cd /var/log/exim4
sudo rm *0*
sudo rm *1*
sudo rm *2*
sudo rm *3*
sudo truncate * --size 0

exit 0

