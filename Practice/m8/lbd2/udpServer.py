import socket

def Main():
	host = '10.10.9.47'
	port = 5064
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	print('server started')
	while True:
		data, addr = s.recvfrom(1024)
		print('Server Connected to:' + str(addr))
		dat = str(data.decode())
		print('Data from Connection: ' + str(dat))
		data = str(dat).upper()
		print('Sending data: ' + str(data))
		s.sendto(data.encode(), addr)
	s.close()
if __name__ == '__main__':
	Main()