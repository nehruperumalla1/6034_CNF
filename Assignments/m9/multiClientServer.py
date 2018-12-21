import socket,time
import os
from _thread import *
import random
import signal

x = 0
# global thread_count
def Main():
	# thread_count = 0
	host = '10.10.9.47'
	port = 1245
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print('Server Started')
	# i = os.getpid()
	# print(os.getpid())
	s.listen(10)
	while True:
		c, addr = s.accept()
		x = int(random.randint(1,51))
		welcome = 'Im thinking of a number between 1 to 50, guess it'
		c.send(welcome.encode())
		print('Connection Established: ' + str(c) + ':' + str(addr))
		print(start_new_thread( clientthread, (c,x)))
		# if thread_count == 0:
		# 	print("going to sleep")
		# 	time.sleep(15)
		# 	if(thread_count == 0):
		# 		os.kill(i, signal.CTRL_BREAK_EVENT)
		


def clientthread(conn, x):
	great = 'Guess is great'
	less = 'Guess is less'
	y = int(0)
	while True:
		y += 1
		data = conn.recv(1024)
		if not data:
			break
		# if data.decode() == 'q':
		# 	# print(get_ident())
		# 	thread_count -= 1
		# 	return 1
		value = int(data.decode())
		if (value > x):
			conn.send(great.encode())
		elif (value < x):
			conn.send(less.encode())
		else:
			correct = 'Correct, number of guesses: ' + str(y)
			conn.send(correct.encode())
	conn.close()
if __name__ == '__main__':
	Main()