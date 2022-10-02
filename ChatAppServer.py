import socket
import select

HEADER_LENGTH = 10
IP = '192.168.93.9'
PORT = 1234

#activating the socket
#AF_INET is for IPV4
#socket.SOCK_STREAM for TCP
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#using setsockopt to get rid of OS error address already in use
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server_socket.bind((IP,PORT))

server_socket.listen()

#till here we have setup the server prerequisite in order to send and receieve message

#the first thing to do is to list all our clients for select

socket_list = [server_socket]

#and maintain client dictionary

clients = {}

#our server would recieve message
def receieve_message(client_socket):
    try : 
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        #we are getting the size of the message
        message_length = int(message_header.decode("utf-8").strip())
        
        #we then return the message in form of dictionary containing the header and the actual body of the message
        return {"header":message_header,"data":client_socket.recv(message_length)}
        
    except:
        return False
    
#what we wish to do is, in a continuous loop, receive messages for all of our client sockets, then send all of the messages out to all of the client sockets.
    
while True:
        read_socket,_,exception_sockets = select.select(socket_list,[],socket_list)
        
        #we are mostly concerned with the read_sockets
        for notified_socket in read_socket:
            if notified_socket == server_socket:
                print("HELLO")
                client_socket,client_address = server_socket.accept()
                user = receieve_message(client_socket)
                if user is False:
                    continue
                socket_list.append(client_socket)
                clients[client_socket] = user
                print(f"Accepted new connection from {client_address[0]}  : {client_address[1]} username:{user['data'].decode('utf-8')}")
            else:
                message = receieve_message(notified_socket)
                if message is False : 
                    print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                    socket_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue
                user = clients[notified_socket]
            
                print(f'Received message from {user["data"].decode} : {message["data"].decode("utf-8")}')
            
                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data']+message['header']+message['data'])

 
                    
    

    



