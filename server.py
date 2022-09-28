from encodings import utf_8
import socket
def createSocket():
    #this method takes two arguments first if ipv4 /v6 and tcp/udp . By default ipv4 and tcp
    serverSocket  = socket.socket()
    print(serverSocket)
    #next thing is bind some socket passing ip address and port as a single object
    serverSocket.bind(("192.168.93.9",9999))
    #Listen passively for the connection, important thing here is backlog which is a queue, all the request will come the queue if reuest exceed the size of the queue then it is simply refused
    serverSocket.listen(3)
    print("server is Listening")
    
    #till it is listening for connection it won't do anything
    # we want to accept in a continuous loop
    while(True):
        #this mehtod would return the client socket and address of it
        clientSocket,address=serverSocket.accept()
        name= clientSocket.recv(1024).decode('utf-8')
        print("connection with",address,name)
        clientSocket.send(bytes('welcome to the chat room','utf-8'))
        clientSocket.close()
createSocket()