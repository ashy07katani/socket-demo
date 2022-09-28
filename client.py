import socket
def createSocket():
    #this method takes two arguments first if ipv4 /v6 and tcp/udp . By default ipv4 and tcp
    clientSocket  = socket.socket()
    print(clientSocket)
    #next thing is bind some socket
    clientSocket.connect(('localhost',9999))
    # clientSocket
    clientSocket.send(bytes('Ashish','utf-8'))
    msg = clientSocket.recv(1024).decode('utf-8')
    print(msg)
createSocket()