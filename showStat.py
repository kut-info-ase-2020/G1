import socket
import os, sys
import LEDproc as led

HOST = "192.168.0.30"
PORT = 50001

def main():
	image_file = sys.argv[1]

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
	res = s.recv(4)
	
	# result process
	# turn off LED
	led.LED_off()

	#tern on LED
	if int(res) == 0:
		led.LED_on(led.BLUEPIN)
	else:
		led.LED_on(led.REDPIN)
	
	print("Answer is " + str(res))

if __name__ == '__main__':
	led.setup_LED()
	try:
		main()
	except KeyboardInterrupt:
		led.destroy()
