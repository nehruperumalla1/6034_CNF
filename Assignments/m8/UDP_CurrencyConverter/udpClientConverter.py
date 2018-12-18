import socket

def Main():
	host = '10.10.9.47'
	port = 5101
	server = ('10.10.9.47',5111)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	message = input('-->')
	while True:
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		print('Data Recieved from Server: ' + str(data.decode()))
		message = input('-->')
	s.close()
if __name__ == '__main__':
	Main()