# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 9:33
# @Author  : lx-rookie


import socket

host = '127.0.0.1'
port = 2404
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

conn,addr = server.accept()
msg = conn.recv(1024)
print('客户端发来消息是%s' %msg.decode('utf-8'))
conn.send(msg.upper())

conn.close()
server.close()

