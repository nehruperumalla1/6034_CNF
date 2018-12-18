import socket

def Main():
	host = '10.1.133.72'
	port = 2011
	s = socket.socket()
	s.connect((host,port))
	message = input("-->")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024)
		print("Recieved from Server: " + str(data.decode()))
		message = input("-->")
	s.close()
if __name__ == '__main__':
	Main()