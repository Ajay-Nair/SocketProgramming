
# Import socket module
import socket            
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345        
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server and decoding to get the string.
t = s.recv(1024).decode()
print(t)
while(True):
    print("Enter command:")
    command = input()
    s.send(command.encode())
    if "exit" in command:
        break
    t = s.recv(1024).decode()
    print(t)
    if "Enter Text" == t:
        content = input()
        s.send(content.encode())
    
# close the connection
s.close()    
     