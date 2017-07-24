# coding:utf-8
import socket
import time
import threading


def tcplink(sock, addr, da):
    print("Accept new connection from %s:%s..." % addr)
    sock.send(b'Welcome')
    i = 0
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('%s' % da[i].encode("utf8"))
        i = i + 1
    sock.close()
    print("Connection from %s: %s closed." % addr)


def setserver(da):
    host = socket.gethostname()
    ip="10.138.77.155"
    print host
    print ip
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    print("1")
    s.listen(5)
    while True:
        # 接受一个新连接：
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink, args=(sock, addr, da))
        t.start()
