#!/bin/sh
# time scale = $1 (arg1)
# take picture by $1
# save in ../Pictures

while [ "$1" -ne 0 ] 
do
	fswebcam -r 680x480 ../Pictures/pic.png;
	python3 showStat.py ../Pictures/pic.png; 
	sleep $1;
done
