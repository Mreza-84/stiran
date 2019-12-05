import socket
from turtle import *
ht()
sty=('arial',30,'normal')
penup()
ous=[]
us=[]
a=textinput('username','username')
us.append(a)
b=0
d=0
c=0
v=[]
p=0
for i in range(len(a)):
    ous.append(ord(us[0][b]))
    b=b+1
    p=p+ous[d]
    d=d+1
def client_program():
    global sty
    host = '192.168.110.28' ##servers IP##
    port = p 

    client_socket = socket.socket() 
    client_socket.connect((host, port))  

    message = input(" -> ")
    up()
    goto(-250,200)
    write(port,font=sty,align='center')

    while message.lower().strip() != 'bye':
        penup()
        goto(0,0)
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        if not data:
            message = input(" -> ")
        else:
            reset()
            up()
            ht()
            goto(-250,200)
            write(a,font=sty,align='center')
            goto(0,0)
            write(('server:  ' + data),font=sty,align='center') 



    client_socket.close() 


if __name__ == '__main__':
    client_program()
