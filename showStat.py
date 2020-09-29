import socket
import os, sys
import LEDproc as led

HOST = "18.183.181.34"
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
	tmp = s.recv(4)
	
	# result process
	# turn off LED
	led.LED_off()
	
	# tern on LED
	res = struct.unpack('>H', tmp)
	if int(res) < 4:
		led.LED_on(led.GREENPIN)
	if int(res) / 8 == 1:
		led.LED_on(led.YELLOWPIN)
	if (int(res) % 8) / 4  == 1:
		led.LED_on(led.REDPIN)
	
	print("Answer is " + str(int(res) % 4))

if __name__ == '__main__':
	led.setup_LED()
	try:
		main()
	except KeyboardInterrupt:
		led.destroy()
