import json
import socket
import os
from datetime import datetime


host = "localhost"
port = 5003
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server GUI-USER is running waiting for connections")
active_connection, address = server.accept()

while(True):
    recibido = active_connection.recv(1024)
    message = json.loads(recibido.decode(encoding="ascii", errors="ignore"))
    error = 1
    if(message["msg"]=="off"):
        break
    if(message["cmd"] == "start" and message["msg"]=="all"):
        print("GUI USER STARTED")
        error = 0
    message = {"cmd":"","msg":"","src":"","dst":""} 
    operation = input("Ingrese operacion\n")
    msg = input("Ingrese el valor\n")
    message["cmd"] = operation
    message["msg"] = msg
    message["src"] = "gui_user"
    if(message["cmd"] == "1" or message["cmd"] == "2"):
        message["dst"] = "file_manager"
        enviar = json.dumps(message)
        active_connection.send(enviar.encode(encoding="ascii",errors="ignore"))
    if(message["cmd"] == "3"):
        message["dst"] = "applications"
        enviar = json.dumps(message)
        active_connection.send(enviar.encode(encoding="ascii",errors="ignore"))
        
    if(message["cmd"]=="send"):
        enviar = json.dumps(message)
        active_connection.send(enviar.encode(encoding="ascii",errors="ignore"))
    

active_connection.close()