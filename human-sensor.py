# -*- coding:utf-8 -*-
import time
import RPi.GPIO as GPIO
import subprocess
sensor_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)


while True:
    if( GPIO.input(sensor_pin) == 0 ):
        print ("OFF")
    else:
        print("ON")
        subprocess.run('takeSendPic.sh')
    time.sleep(10)
