import socket
from threading import *
import os,signal

def Main():
    host = '10.10.9.47'
    port = 1513
    s = socket.socket()
    try:
        s.connect((host, port))
    except OSError as e:
        print('Sorry, you are Late')
        return
    thread2 = Thread(target = send, args = (s,)).start()
    while True:
        data = s.recv(1024).decode()
        if (data == 'ATTENDANCE SUCCESS' or data == 'ROLL NUMBER-NOT FOUND' or data == 'TIMEOUT'):
            print(data)
            break
        print(data)
    s.close()
    os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)


def send(s):
    while True:
        msg = input()
        # print('MSG Sening')
        s.send(msg.encode())
    s.close()
    

if __name__ == '__main__':
    Main()
