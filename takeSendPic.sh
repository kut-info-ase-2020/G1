#!/bin/sh
# time scale = $1 (arg1)
# take picture by $1
# save in ../Pictures

trap python finish.py; SIGHUP SIGINT SIGKILL SIGTERM

while [ "$1" -ne 0 ] 
do
	fswebcam -r 680x480 ../Pictures/pic.png;
	python showStat.py ../Pictures/pic.png; 
	sleep $1;
done
