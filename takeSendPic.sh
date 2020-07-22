#!/bin/sh
# time scale = $1 (arg1)
# take picture by $1
# save in ../Pictures
watch -n $1 
do
	fswebcam -r 680x480 ../Pictures/pic.jpg
	scp ../Pictures/pic.jpg root@116.198.163.223:~/Pictures/
done
