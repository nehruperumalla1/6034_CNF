import socket

def Main():
	host = '10.1.133.72'
	port = 2011
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, addr = s.accept()
	print("Connection from: " + str(addr))
	while True:
		data = c.recv(1024)
		if not data:
			break
		print("From Connected User: " + str(data.decode()))
		data = str(data.decode()).upper()
		print("Sending: " + data)
		c.send(data.encode())
	c.close()

if __name__ == '__main__':
	Main()