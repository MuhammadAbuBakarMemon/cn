# # getting ip address

import socket 

# hostname = socket.gethostname()

# ip = socket.gethostbyname(hostname)

# print(hostname)
# print(ip)

# # getting any host ip addressin python

# hostnames=["www.google.com", "www.facebook.com"]

# for i in hostnames:
#     ip = socket.gethostbyname(i)
#     print(i)
#     print(ip)

# # get hostname by ip address

# hname = socket.gethostbyaddr('8.8.8.8')
# hname1 = socket.gethostbyaddr('172.16.5.43')

# print(hname)
# print(hname1)

# 4. Getting service name, given port number & protocol in python

# def f_serv_name():

#     portocol_name = 'tcp'
#     port = [80, 25]

#     for x in port:

#         print(f'protocol: {portocol_name}, port: {x}, service name: {socket.getservbyport(x, portocol_name)}\n')

# f_serv_name()

# 5 PORT Scanner

import time 

st = time.time()

def func():

    ta = input("Enter hostname to be scanned: ")
    ip = socket.gethostbyname(ta)

    print('starting scan on ip: ', ip)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        conns = s.connect_ex((ip, i))

        if (conns==0):
            print(f'port; {i}, open')
            s.close()

# server

#importing the socket module:
import socket

#creating a socket object
s=socket.socket()
print("Socket Created")

#binding to the port
s.bind(('localhost',9999))

#now wait for client connection
s.listen(5)
print("Waiting for connection")

while True:
    c, addr=s.accept()     #establish connection with the client
    print("Got connection from",addr)
    c.send(bytes("Thankyou for connecting")) 
    
    c.close()              #close the connection

# clienr

#importing the socket module:
import socket

#creating a socket object
s=socket.socket()
print("Socket Created")

#binding to the port
s.bind(('localhost',9999))

#now wait for client connection
s.listen(5)
print("Waiting for connection")

while True:
    c, addr=s.accept()     #establish connection with the client
    print("Got connection from",addr)
    c.send(bytes("Thankyou for connecting")) 
    
    c.close()              #close the connection