import socket
import os, sys
from mask.image_test import mask_catch
import csv

HOST = "0.0.0.0"
PORT = 50001

SC_DIR = "../Pictures"
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
	all_data = b""

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
	
	'''
	# only now 
	global test
	res = test % 16
	test += 1
	'''
	
	# actually use
	# image in ./Pictures/sc_file.png
	# output is Int (estimate 0 ~ 15)
	# pleese make and use mathod
	res = recognition()
	print(str(res))
	print(type(res))	
	# send result to client
	clientsock.sendall(res.to_bytes(1, "big"))

	clientsock.close()

# recognition method
def recognition():
	# parameter for return (INT)
	res = 0
	
	#start to do the test on Mask-Detection
	
	input_path="/home/ec2-user/Pictures"
	out_path="/home/ec2-user/Pictures/result"
	
	#Create a variable that returns 1 if there is even one person without a mask, 0 if everyone wears it. ---a
	a=mask_catch(input_path,out_path)# This function will feedback signal 0 or 1 to server. And save result image and txt file in the output_path.	

	# sent result by csv
	nam_csv = 'result.csv'
	res_csv_path = os.path.join('/home/ec2-user/result', nam_csv) 
	
	csvfile = open(res_csv_path, 'r')
	for row in csv.reader(csvfile):
		res_num = row[1]
		res_mk = row[2]
	csvfile.close()
	
	if int(res_num) > 3:
		res = int(res_mk) * 4 + 3
	else:
		res = int(res_mk) * 4 + int(res_num)

	return res

	# please fit your models to image	
	# received image is saved in ./Pictures/sc_file.png
	


	# return is INT
	# 1st-6th bit means number of person
	# 7th bit means anyone don't put on mask(1) or safe(0)
	# 8th bit means people distance is too close(1) or safe(0)
	return res

if __name__ == '__main__':
	main()
