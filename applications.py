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
    if(message["msg"]=="calc" and message["action"] == 3):
        error = os.system("gnome-calculator &")
        #print (check_output(["pidof","gnome-calculator"]).decode()," THIS IS THE PID OF ",message["msg"])
        pid["calc"] = check_output(["pidof","gnome-calculator"]).decode()
    elif(message["msg"]=="code" and message["action"] == 3):
        error = os.system("code &")
        #print (check_output(["pidof","code"]).decode()," THIS IS THE PID OF ",message["msg"])
        pid["code"] = check_output(["pidof","code"]).decode()
    elif(message["msg"]=="code" and message["action"] == 4):
        error = os.system("kill "+pid["code"])
    elif(message["msg"]=="calc" and message["action"] == 4):
        error = os.system("kill "+pid["calc"])
    print("Orden: "+recibido.decode(encoding="ascii", errors="ignore"))
    print(pid)
    if(error != 0):
        log = "Ocurrio un error al ejecutar la acción de "+("crear carpeta" if message["action"] == "1" else "ejecutar aplicación")    
        message["cmd"] = "send"
        message["action"] = "5"
        message["msg"] = log
        message["dst"] = "gui_user"
        message["src"] = "applications"
        message = json.dumps(message)
        active_connection.send(message.encode(encoding="ascii",errors="ignore"))
    else :
        #+ message["msg"] + pid[message["msg"]]
        log = "Accion realizada : "+("lanzar aplicacion" if message["action"] == "3" else "") 
        message["cmd"] = "send"
        message["action"] = "5"
        message["msg"] = log
        message["dst"] = "gui_user"
        message["src"] = "applications"
        message = json.dumps(message)
        active_connection.send(message.encode(encoding="ascii",errors="ignore"))
    now = datetime.now()
    #print(enviar)
    current_time = now.strftime("%H:%M:%S")
    f = open("log_file_manager.txt","a")
    f.write(log+ "//" + pid+ " => date and time:"+current_time+"\n")
    f.close()
    #print("HOLI2")
    

active_connection.close()

