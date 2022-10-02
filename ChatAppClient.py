import socket 
import select
import errno
import sys

HEADER_LENGTH = 10
IP = "192.168.93.9"
PORT=1234
my_username = input("Username: ")

#create a socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to the given IP and PORT
client_socket.connect((IP,PORT))

#set connection to non-blocking state
client_socket.setblocking(False)

#Prepare username and header and send them
#We need to encode username to bytes, then count number of bytes
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

while True : 
    #wait for user to input a message
    message = input(f'{my_username} > ')
    #If message is not empty - send it
    if message:
        #Encode message to bytes, prepare header and convert to bytes 
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)
        
    try:
        #Now we want to loop over received messages
        while True:
            #Receive header containing username length
            username_header  = client_socket.recv(HEADER_LENGTH)
            
            if not len(username_header):
                print('Connection closed by te server')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            
            print(f'{username} > {message}')
    
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error:{}'.format(str(e)))
            sys.exit()
        continue
    except Exception as e:
        print('Reading error:{}'.format(str(e)))
        sys.exit()
        
            


