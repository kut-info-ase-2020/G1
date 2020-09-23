import socket
import os, sys

HOST = "18.181.171.51"
PORT = 50001

SC_DIR = "./Pictures"
SC_FILE = "sc_file.png"

# for test
test = 0

def main():
	# definition socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# become to reuse socket
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# bind socket
	s.bind((HOST, PORT))

	# wait connect socket (max que = 10)
	s.listen(10)

	while True:
		# if come connect, create new socket object 
		clientsock, client_address = s.accept()
		
		# call method to receive proc.
		recv_client_data(clientsock)
	
	s.close()

def recv_client_data(clientsock):
	# format parameter
	all_data = ""

	# receive data
	while True:
		data = clientsock.recv(1024)
		# finish in being received all data
		if not data:
			break
		# add data to make complete data
		all_data += data
	# save data as image file
	with open(SC_DIR + '/' + SC_FILE, 'wb') as f:
		f.write(all_data)
	
	# only now 
	global test
	res = test % 2
	test += 1

	'''
	# actually use
	# image in ./Pictures/sc_file.png
	# output is Int (estimate 0 ~ 7)
	# pleese make and use mathod
	res = recognition()
	'''

	# send result to client
	clientsock.sendall(str(res))

	clientsock.close()

if __name__ == '__main__':
	main()
