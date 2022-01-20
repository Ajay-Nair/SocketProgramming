import os
import socket

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

command = c.recv(1024).decode()
print(command)

if "create file" in command:
    x = command.split(" ")
    fn = x[2] + ".txt"
    f = open(fn,"w+")
    f.close()
if "append file" in command:
    x = command.split(" ")
    fn = x[2] + ".txt"
    print("Enter Text")
    des = input()
    f = open(fn,"w+")
    f.write(des)
    f.close()
if "read file" in command:
    x = command.split(" ")
    fn = x[2] + ".txt"
    f = open(fn,"r")
    contents = f.read()
    print(contents)
    f.close()

if "delete file" in command:
    x = command.split(" ")
    fn = x[2] + ".txt"
    if os.path.exists(fn):
        os.remove(fn)
    else:
        print("File does not exist")

c.close()
