import socket

def Main():
	host = '10.1.133.72'
	port = 2011
	s = socket.socket()
	s.bind((host, port))
	s.listen(2)
	clients = {}
	while True:
		c, addr = s.accept()
		clients[addr] = c
		pressed = 0
		for eachsocket, eachaddrtuple in clients.iteritems():
			print('Recieving data from ' + eachaddrtuple)
			data = c.recv(1024)
			if not data:
				break
			pressed = pressed + 1
			print("From Connected User: " + str(data.decode()))
			data = str(data.decode()).upper()
			print("Sending: " + data)
			c.send(data.encode())
	c.close()

if __name__ == '__main__':
	Main()