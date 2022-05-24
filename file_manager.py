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
    print("ESTO ES LO QUE ESTÁ LLEGANDO \n",message)
    error = 1
    if(message["cmd"] == "start" and message["msg"]=="all"):
        print("FILE MANAGER STARTED")
        error = 0
    if(message["action"]=="1"):
        error = os.system("mkdir "+message["msg"])
    elif (message["action"]=="2"):
        f = open(message["msg"],'w')
        error = 0
    elif (message["msg"]=="off"):
        break        
    print("Orden: "+recibido.decode(encoding="ascii", errors="ignore"))
    if(error != 0):
        log = "Ocurrio un error al ejecutar la acción de "+("crear carpeta" if message["action"] == "1" else "crear archivo") 
        message["cmd"] = "send"
        message["action"] = "5"
        message["msg"] = log
        message["dst"] = "gui_user"
        message["src"] = "file_manager"
        message = json.dumps(message)
        active_connection.send(message.encode(encoding="ascii",errors="ignore"))   
    else :
        now = datetime.now()
        #print(now)
        current_time = now.strftime("%H:%M:%S")
        log = "Accion realizada : "+("crear carpeta" if message["action"] == "1" else "crear archivo")+"=> time:"+current_time
        message["cmd"] = "send"
        message["action"] = "5"
        message["msg"] = log
        message["dst"] = "gui_user"
        message["src"] = "file_manager"
        message = json.dumps(message)
        active_connection.send(message.encode(encoding="ascii",errors="ignore"))
    now = datetime.now()
    #print(now)
    current_time = now.strftime("%H:%M:%S")
    f = open("log_file_manager.txt","a")
    f.write(log+" => time:"+current_time+"\n")
    f.close()
    

active_connection.close()