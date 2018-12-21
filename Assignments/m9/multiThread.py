from threading import *
import socket,time
import os
import random
import signal

x = 0
# i = os.getpid()
# global thread_count
def Main():
	# thread_count = 0
	host = '10.10.9.47'
	port = 1246
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print('Server Started')
	
	print(os.getpid())
	s.listen(10)
	while True:
		c, addr = s.accept()
		x = int(random.randint(1,51))
		welcome = 'Im thinking of a number between 1 to 50, guess it'
		c.send(welcome.encode())
		print('Connection Established: ' + str(c) + ':' + str(addr))
		thread = Thread(target = clientthread, args = (c,x)).start()
		# print(active_count())

def check():
	i = os.getpid()
	print(active_count())
	if active_count() == 2:
		print("going to sleep")
		time.sleep(15)
		if(active_count() == 2):
			os.kill(i, signal.CTRL_BREAK_EVENT)
		


def clientthread(conn, x):
	great = 'Guess is great'
	less = 'Guess is less'
	y = int(0)
	while True:
		y += 1
		data = conn.recv(1024)
		if not data:
			break
		if data.decode() == 'q':
			print(get_ident())
			check()
			return 1
		value = int(data.decode())
		if (value > x):
			conn.send(great.encode())
		elif (value < x):
			conn.send(less.encode())
		else:
			correct = 'Correct, number of guesses: ' + str(y)
			conn.send(correct.encode())
			check()
			return 1
	conn.close()

if __name__ == '__main__':
	Main()