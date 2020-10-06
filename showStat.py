import socket
import os, sys
import LEDproc as led
import struct

HOST = "18.183.181.34"
#HOST = "192.168.0.30"
PORT = 50001

def main(image_file):

	with open(image_file, 'rb') as f:
		binary = f.read()
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# connect server
	s.connect((HOST, PORT))
	
	# send image to server
	print("Send " + image_file)
	s.sendall(binary)
	# disconnect 
	s.shutdown(1)

	# receive answer from server (buffer size = 4 bite)
	tmp = s.recv(4)
	
	# result process
	# turn off LED
	led.LED_off()
	
	# tern on LED
	res = max(struct.unpack('>B', tmp))
	print 'res = %d' % res
	#res = int(str(tmp))
	#print("type : " + str(type(tmp)) + ", value : " + tmp)
	#print("type : " + str(type(res)) + ", value : " + str(res))
	
	if res < 4:
		# all green
		led.LED_on(led.GREENPIN)
	if res / 8 == 1:
		# cannot keep social distance
		led.LED_on(led.YELLOWPIN)
	if int(res) % 8 / 4  == 1:
		# anyone don't put on mask
		led.LED_on(led.REDPIN)
	
	print(str(res % 4) + " person(s) in this picture.")
	return res % 4
	
if __name__ == '__main__':
	led.setup_LED()
	try:
		main("../Pictures/pic.png")
	except KeyboardInterrupt:
		led.destroy()
