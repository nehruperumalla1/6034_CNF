import socket

def Main():
	host = '10.10.9.47'
	port = 5111
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	print('server started')
	dict = {'Dollar': 1, 'INR': 0, 'Pounds': 2, 'Yen': 3}
	matrix = [[1.0, 0.014, 0.011, 1.58], [72.1, 1.0, 0.79, 112.60], [89.98, 1.26, 1.0, 142.17], [0.63, 0.0089, 0.0070, 1.0]]
	while True:
		data, addr = s.recvfrom(1024)
		print('Server Connected to:' + str(addr))
		datalist = str(data.decode()).split()
		value = float(matrix[dict[datalist[1]]][dict[datalist[4]]])
		value = int(datalist[2]) * value
		print('Sending Converted Currency: ' + str(value))
		s.sendto(str(value).encode(), addr)
	s.close()
if __name__ == '__main__':
	Main()