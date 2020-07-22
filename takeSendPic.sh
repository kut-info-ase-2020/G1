#!/bin/sh
# time scale = $1 (arg1)
# take picture by $1
# save in ../Pictures
while [ "$1" -ne 0 ] 
do
	sleep $1;
	fswebcam -r 680x480 ../Pictures/pic.jpg;
	scp ../Pictures/pic.jpg root@116.198.163.223:~/Pictures/;
done
