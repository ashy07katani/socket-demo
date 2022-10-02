import socket
HEADERSIZE=10
def createSocket():
    #this method takes two arguments first if ipv4 /v6 and tcp/udp . By default ipv4 and tcp
    clientSocket  = socket.socket()
    print(clientSocket)
    #next thing is bind some socket
    clientSocket.connect(('localhost',9999))
    # clientSocket
    # clientSocket.send(bytes('Ashish','utf-8'))
    while True:
        full_msg = ''
        new_msg = True
        while True:
            msg = clientSocket.recv(16)
            print(msg)
            if new_msg:
                print("new msg len:",msg[:HEADERSIZE])
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            print(f"full message length: {msglen}")

            full_msg += msg.decode("utf-8")

            print(len(full_msg))


            if len(full_msg)-HEADERSIZE == msglen:
                print("full msg recvd")
                print(full_msg[HEADERSIZE:])
                new_msg = True


    
    
createSocket()