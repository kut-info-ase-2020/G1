import LEDproc as led
import time

cnt = 0
while True:
	if cnt % 2 == 0:
		led.LED_on(led.GREENPIN)
	else:
		led.LED_on(led.REDPIN)
	time.sleep(1)
	cnt ++
	led.LED_off()
