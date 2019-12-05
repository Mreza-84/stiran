import socket
from turtle import *
sty=('arial',30,'normal')
ht()
us=[]
ous=[]
a=textinput('username','Enter your group name')
us.append(a)
b=0
d=0
c=0
v=[]
p=0
file=open('r')
file.write('hi')
for i in range(len(a)):
    ous.append(ord(us[0][b]))
    b=b+1
    p=p+ous[d]
    d=d+1
def server_program():
    global sty
    host = '192.168.110.28' ##servers IP##
    port =p
    penup()
    goto(-185,285)
    write(port,font=sty,align='center')

    server_socket = socket.socket()     
    server_socket.bind((host, port))
    

    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        goto(-185,285)
        write(port,font=sty,align='center')
        data = conn.recv(1024).decode()
        if not data:
            goto(-185,285)
            write(port,font=sty,align='center')
            data =  conn.send(data.encode())
        else:
            reset()
            ht()
            penup()
            goto(-185,285)
            write(a,font=sty,align='center')
            goto(0,0)
            write("client:  " + str(data),font=sty,align='center')

    conn.close()  


if __name__ == '__main__':
    server_program()
