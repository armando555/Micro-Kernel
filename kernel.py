import socket
import json
import random
import time
host = "localhost"
portF = 5001
portA = 5002
portG = 5003
objsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket.connect((host,portF))
objsocket1.connect((host,portA))
objsocket2.connect((host,portG))

print("starting client- KERNEL")
message = {"cmd":"","msg":"","src":"","dst":""} 
message["cmd"] = "start"
message["msg"] = "all"
message["src"] = "kernel"
message["action"] = "0"
last_dst = ""
count = 0
while(True):
    
    if((message["cmd"] == "start" and message["msg"]=="all") and count == 0):
        count = 1
        #Applications-------------------------------------------------------
        message["dst"] = "applications"
        enviar = json.dumps(message)
        objsocket1.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objsocket1.recv(1024)
        print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
        #File manager-------------------------------------------------------
        message["dst"] = "file_manager"
        enviar = json.dumps(message)
        objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objsocket.recv(1024)
        print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
        #GUI-USER-------------------------------------------------------
        message["dst"] = "gui_user"
        enviar = json.dumps(message)
        objsocket2.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objsocket2.recv(1024)
        print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
    
    #ACA TE DEBO PONER EL MENSAJE 
    #if (last_dst == "applications"):
        #recibido
    #print("ANTES DE MESSAGE")
    message = json.loads(recibido.decode(encoding="ascii", errors="ignore"))
    #print(message)
    if(message["cmd"]=="send" and message["action"] == "5"):
        enviar = json.dumps(message)
        objsocket2.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objsocket2.recv(1024)
        #print(recibido.decode(encoding="ascii", errors="ignore"))
    #print("LLEG?? AL KERNEL\n",message)
    message = json.loads(recibido.decode(encoding="ascii", errors="ignore"))
    if(message["msg"] == "off"):
        message["dst"] = "applications"
        enviar = json.dumps(message)
        objsocket1.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objsocket1.recv(1024)
        print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
        #-------------------------------------------------------------------
        message["dst"] = "file_manager"
        enviar = json.dumps(message)
        objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objsocket.recv(1024)
        print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
        #-------------------------------------------------------------------
        message["dst"] = "gui_user"
        enviar = json.dumps(message)
        objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objsocket.recv(1024)
        print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
        break;
    elif(message["cmd"] == "send" and message["dst"] == "applications"):
        print("VOY A ENVIAR APPLICATIONS")
        time_operation = random.random()
        if( time_operation >=0.99):
            print("Kernel is busy--- wait a second")
            time.sleep(3)
        message["dst"] = "applications"
        enviar = json.dumps(message)
        objsocket1.send(enviar.encode(encoding="ascii", errors="ignore"))
        last_dst = "applications"
        recibido = objsocket1.recv(1024)
        print("RECIBI DE APPLICATIONS")
    else:
        print("VOY A ENVIAR A FILE MANAGER")
        time_operation = random.random()
        if( time_operation >=0.99):
            print("Kernel is busy--- wait a second")
            time.sleep(3)
        message["dst"] = "file_manager"
        last_dst = "file_manager"
        enviar = json.dumps(message)
        objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objsocket.recv(1024)
        print("RECIBI DE FILE MANAGER",recibido)
    print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
objsocket.close()