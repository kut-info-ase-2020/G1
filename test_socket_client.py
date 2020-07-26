import socket
import os, sys

HOST = "0.0.0.0"
PORT = 50001

def main():
	image_file = sys.argv[1]

	with open(image_file, 'rb') as f:
    	binary = f.read()
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# connect server
	s.connect((host, port))

	# send image to server
	print("Send " + image_file)
	s.sendall(binary)
	# disconnect 
	s.shutdown(1)

	# receive answer from server (buffer size = 4 bite)
	res = s.recv(4)

	print("Answer is " + str(res))

if __name__ == "main":
	main()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, 1235))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

msg = s.recv(8)
print(str(msg))
