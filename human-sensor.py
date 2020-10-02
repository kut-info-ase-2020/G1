# -*- coding:utf-8 -*-
import time
import RPi.GPIO as GPIO
import os
import subprocess
sensor_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)


while True:
    if( GPIO.input(sensor_pin) == 0 ):
        print ("OFF")
    else:
        print("ON")
        # -*- coding: utf-8 -*-

    #def call_shell():
    	path = os.path.dirname(os.path.abspath(__file__))
    	cmd = '{}/takeSendPic.sh {}'.format(path, 20)
    	res = subprocess.call(cmd, shell=True)
    	#print(res)


#if __name__ == '__main__':
#    call_shell()
#        subprocess.takeSendPic('')
    
    time.sleep(10)

"""
    if A == 0:
	
    elif A == 1:
	time.sleep(600)
    elif A == 2:
        time.sleep(300)
    elif A >= 3:
        time.sleep(60)
"""
