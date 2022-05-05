import socket
import json
host = "localhost"
portF = 5001
portA = 5002
objsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket.connect((host,portF))
objsocket1.connect((host,portA))

print("starting client")

while(True):
    message = {"cmd":"","msg":"","src":"","dst":""} 
    operation = input("Ingrese operacion\n")
    msg = input("Ingrese el valor\n")
    message["cmd"] = operation
    message["msg"] = msg
    message["src"] = "kernel"
    if(operation == "3"):
        message["dst"] = "applications"
        enviar = json.dumps(message)
        objsocket1.send(enviar.encode(encoding="ascii", errors="ignore"))
    else:
        message["dst"] = "file_manager"
        enviar = json.dumps(message)
        objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
    recibido = objsocket.recv(1024)
    print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
objsocket.close()