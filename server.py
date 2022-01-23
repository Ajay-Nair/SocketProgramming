import os
import socket
from pathlib import Path

s=socket.socket() #Created a socket
print("Socket Created Successfully")

port = 12345

s.bind(('',port))
print("Socket binded to %s" %(port))

s.listen(5)
print("socket is listening")

c , addr = s.accept()
print("Got connection from",addr)

c.send("Thanks for connecting".encode())

#command = c.recv(1024).decode()

while(True):
    command = c.recv(1024).decode()

    if "exit" in command:
        break

    if "create file" in command:
        x = command.split(" ")
        fn = x[2]
        path = Path(fn)
        if(path.is_file()):
            c.send("File Exists".encode())
        else:
            f = open(fn,"w+")
            f.close()
            c.send("File Created".encode())
    if "append file" in command:
        x = command.split(" ")
        fn = x[2] 
        c.send("Enter Text".encode())
        content = c.recv(1024).decode()
        f = open(fn,"w+")
        f.write(content)
        #c.send("Append successfull".encode())
        f.close()
    if "read file" in command:
        x = command.split(" ")
        fn = x[2] 
        if os.path.exists(fn):
            f = open(fn,"r")
            contents = f.read()
            c.send(contents.encode())
        else:
            c.send("File does not exist".encode())
        f.close()

    if "delete file" in command:
        x = command.split(" ")
        fn = x[2] 
        if os.path.exists(fn):
            os.remove(fn)
            c.send("File deleted".encode())
        else:
            c.send("File does not exist".encode())

c.close()
