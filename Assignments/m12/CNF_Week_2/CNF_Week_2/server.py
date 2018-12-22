import socket
import csv
from threading import *
import os,signal,time

def Main():
	host = '10.10.9.47'
	port = 1513

	s = socket.socket()
	s.bind((host,port))
	s.listen(10)
	print('server started....')
	data = {}
	with open('data.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			data[row[0]] = [row[1],row[2]]
	ident = {}
	present_rolls = []
	while True:
		c, addr = s.accept()
		inpu = c.recv(1024).decode()
		dat = inpu.split()
		roll = dat[1]
		flag = True
		if dat[0] == 'MARK-ATTENDANCE':
			for key, value in data.items():
				if key == roll:
					flag = False
					ident[c] = key
					print(key + ' -- Started PUZZLE')
					Thread(target = att, args = (data,c,ident,present_rolls)).start()
			if flag:
				c.send('ROLL NUMBER-NOT FOUND'.encode())
				check(present_rolls)
	s.close()
			
def check(present_rolls):
	if (active_count() == 2):
		print('WAIT TIME - 15 Seconds')
		time.sleep(15)
		if (active_count() == 2):
			print('Rollnumbers of Presented Students are: ')
			print(present_rolls)
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)

def att(data, c, ident,present_rolls):
	count = 0
	lis = data[ident[c]]
	while True:
		count += 1
		c.send(('SECRETQUESTION-' + lis[0]).encode())
		user_ans = c.recv(1024).decode().split('-')
		if (user_ans[0] == 'SECRETANSWER'):
			if (user_ans[1] == lis[1]):
				present_rolls.append(ident[c])
				print(str(ident[c]) + ' -- Present')
				c.send('ATTENDANCE SUCCESS'.encode())
				check(present_rolls)
				return 1
			elif count == 5:
				c.send('TIMEOUT'.encode())
			else:
				c.send('ATTENDANCE FAILURE'.encode())
		else:
			c.send('Invalid Syntax'.encode())
if __name__ == '__main__':
	Main()