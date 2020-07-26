import socket
import os, sys

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

	print("Answer is " + str(res))

if __name__ == '__main__':
	main()
