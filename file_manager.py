import json
import socket
import os
from datetime import datetime


host = "localhost"
port = 5001
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is running waiting for connections")
active_connection, address = server.accept()

while(True):
    recibido = active_connection.recv(1024)
    message = json.loads(recibido.decode(encoding="ascii", errors="ignore"))
    error = 1
    if(message["action"]=="1"):
        error = os.system("mkdir "+message["value"])
    else:
        error = os.system("touch "+message["value"])
    print("Orden: "+recibido.decode(encoding="ascii", errors="ignore"))
    if(error != 0):
        enviar = "Ocurrio un error al ejecutar la acción de "+("crear carpeta" if message["action"] == "1" else "crear archivo")    
    else :
        enviar = "Accion realizada : "+("crear carpeta" if message["action"] == "1" else "crear archivo")
    now = datetime.now()
    print(now)
    current_time = now.strftime("%H:%M:%S")
    f = open("log_file_manager.txt","a")
    f.write(enviar+" => date and time:"+current_time+"\n")
    f.close()
    active_connection.send(enviar.encode(encoding="ascii",errors="ignore"))
    

active_connection.close()