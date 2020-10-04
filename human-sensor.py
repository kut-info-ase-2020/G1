# -*- coding:utf-8 -*-
import time
import RPi.GPIO as GPIO
import os
import subprocess
import showStat as show
sensor_pin = 26

ONE = 300
TWO = 120
MANY = 30

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

A = 0

while True:
    if( GPIO.input(sensor_pin) == 0 ):
        print ("OFF")
    else:
        print("ON")
        # -*- coding: utf-8 -*-

    #def call_shell():
    path = os.path.dirname(os.path.abspath(__file__))
    #cmd = '{}/takeSendPic.sh {}'.format(path, 10)
    cmd = '{}/takeSendPic.sh'.format(path)
    res = show.main("../Pictures/pic.ong")
    #res = subprocess.call(cmd, shell=True)
    #print(res)

    if res == 0:
	time.sleep(ONE)
    elif res == 1:
        time.sleep(ONE)
    elif res == 2:
        time.sleep(TWO)
    elif res == 3:
        time.sleep(MANY)
	

#if __name__ == '__main__':
#    call_shell()
#        subprocess.takeSendPic('')
    #time.sleep(2)

"""
    if A == 0:
	
    elif A == 1:
	time.sleep(600)
    elif A == 2:
        time.sleep(300)
    elif A >= 3:
        time.sleep(60)
"""
