import json
import socket
import os
from datetime import datetime


host = "localhost"
port = 5001
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server file manager is running waiting for connections")
active_connection, address = server.accept()

while(True):
    recibido = active_connection.recv(1024)
    message = json.loads(recibido.decode(encoding="ascii", errors="ignore"))
    error = 1
    if(message["cmd"] == "start" and message["msg"]=="all"):
        print("FILE MANAGER STARTED")
        error = 0
    if(message["cmd"]=="1"):
        error = os.system("mkdir "+message["msg"])
    elif (message["cmd"]=="2"):
        error = os.system("touch "+message["msg"])
    elif (message["msg"]=="off"):
        break        
    print("Orden: "+recibido.decode(encoding="ascii", errors="ignore"))
    if(error != 0):
        log = "Ocurrio un error al ejecutar la acción de "+("crear carpeta" if message["cmd"] == "1" else "crear archivo") 
        message["cmd"] = "5"
        message["msg"] = log
        message["dst"] = "gui_user"
        message["src"] = "file_manager"
        message = json.dumps(message)
        active_connection.send(message.encode(encoding="ascii",errors="ignore"))   
    else :
        log = "Accion realizada : "+("crear carpeta" if message["cmd"] == "1" else "crear archivo")
        message["cmd"] = "5"
        message["msg"] = log
        message["dst"] = "gui_user"
        message["src"] = "file_manager"
        message = json.dumps(message)
        active_connection.send(message.encode(encoding="ascii",errors="ignore"))
    now = datetime.now()
    print(now)
    current_time = now.strftime("%H:%M:%S")
    f = open("log_file_manager.txt","a")
    f.write(log+" => time:"+current_time+"\n")
    f.close()
    

active_connection.close()