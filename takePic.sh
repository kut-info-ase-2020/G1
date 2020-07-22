#!/bin/sh
# time scale = $1 (arg1)
# take picture by $1
# save in ../Pictures
watch -n $1 fswebcam -r 680x480 ../Pictures/pic.jpg
