import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))
cmd='GET '.encode()
time.sleep(1)
sock.send(cmd)




while True:
     data = sock.recv(1024)
     if len(data) < 1:
        break
     print(data.decode(), end='')

sock.close()