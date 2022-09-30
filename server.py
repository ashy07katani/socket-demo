from encodings import utf_8
import socket
import random
import string
HEADER_SIZE = 10

def createSocket():
    #this method takes two arguments first if ipv4 /v6 and tcp/udp . By default ipv4 and tcp
    serverSocket  = socket.socket()
    print(serverSocket)
    #next thing is bind some socket passing ip address and port as a single object
    serverSocket.bind(('localhost',9999))
    #Listen passively for the connection, important thing here is backlog which is a queue, all the request will come the queue if reuest exceed the size of the queue then it is simply refused
    serverSocket.listen(3)
    print("server is Listening")
    
    #till it is listening for connection it won't do anything
    # we want to accept in a continuous loop
    while(True):
        #this mehtod would return the client socket and address of it
        size = random.randint(100,1001)
        # generating random strings
        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=size))
        clientSocket,address=serverSocket.accept()
        msg = res
        msg=f"{len(msg):<{HEADER_SIZE}}"+msg
        #'{:<30}'.format('left aligned')
        #name= clientSocket.recv(1024).decode('utf-8')
        print("connection with",address)
        clientSocket.send(bytes(msg,'utf-8'))
        print("data sent ",msg)
createSocket()