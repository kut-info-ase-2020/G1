import socket

HOST = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, 1235))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

msg = s.recv(8)
print(str(msg))
