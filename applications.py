import json
import socket
import os
from subprocess import check_output
from datetime import datetime


host = "localhost"
port = 5002
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server applications is running waiting for connections")
active_connection, address = server.accept()
pid = {}
while(True):
    recibido = active_connection.recv(1024)
    message = json.loads(recibido.decode(encoding="ascii", errors="ignore"))
    error = 1
    if(message["cmd"] == "start" and message["msg"]=="all"):
        print("APPLICATIONS STARTED")
        error = 0
    if(message["msg"]=="off"):
        break
    if(message["msg"]=="calc"):
        error = os.system("gnome-calculator &")
        #print (check_output(["pidof","gnome-calculator"]).decode()," THIS IS THE PID OF ",message["msg"])
        pid["calc"] = check_output(["pidof","gnome-calculator"]).decode()
    elif(message["msg"]=="code"):
        error = os.system("code &")
        #print (check_output(["pidof","code"]).decode()," THIS IS THE PID OF ",message["msg"])
        pid["code"] = check_output(["pidof","code"]).decode()
    print("Orden: "+recibido.decode(encoding="ascii", errors="ignore"))
    print(pid)
    if(error != 0):
        log = "Ocurrio un error al ejecutar la acción de "+("crear carpeta" if message["cmd"] == "1" else "ejecutar aplicación")    
        message["cmd"] = "5"
        message["msg"] = log
        message["dst"] = "gui_user"
        message["src"] = "applications"
        message = json.dumps(message)
        active_connection.send(message.encode(encoding="ascii",errors="ignore"))
    else :
        log = "Accion realizada : "+("lanzar aplicacion" if message["cmd"] == "3" else "")
        message["cmd"] = "5"
        message["msg"] = log
        message["dst"] = "gui_user"
        message["src"] = "applications"
        message = json.dumps(message)
        active_connection.send(message.encode(encoding="ascii",errors="ignore"))
    now = datetime.now()
    #print(enviar)
    current_time = now.strftime("%H:%M:%S")
    f = open("log_file_manager.txt","a")
    f.write(log+" => date and time:"+current_time+"\n")
    f.close()
    #print("HOLI2")
    

active_connection.close()

