# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 9:33
# @Author  : lx-rookie


from socket import *

ipaddr = '127.0.0.1'
port = 2404
back_log = 5

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind((ipaddr, port))
tcp_server.listen(back_log)

while True:
    conn,addr = tcp_server.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("data is %s" %data.decode('utf-8'))
        conn.send(data.upper())

    conn.close()
tcp_server.close()

