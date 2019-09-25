import socket
import sys
def create_socket():
  try:
    global host
    global port
    global s
    host=""
    port=9999
    s=socket.socket()
  except socket.error as msg:
    print("socket creation error"+str(msg))
#binding the socket and listening to the connection
def bind_socket():
  try:
    global host
    global port
    global s
    print("binding the port"+str(port))
    s.bind((host,port))#this format is called cuple in python
    s.listen(5)
  except socket.error as msg:
    print("socket creation error"+str(msg)+"\n"+"retrying...")
    bind_socket() #recursive call if the connection was made
    
 
    
