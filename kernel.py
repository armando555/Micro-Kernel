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
    message = {"action":"","value":""} 
    operation = input("Ingrese operacion\n")
    value = input("Ingrese el valor\n")
    message["action"] = operation
    message["value"] = value
    enviar = json.dumps(message)
    if(operation == "3"):
        objsocket1.send(enviar.encode(encoding="ascii", errors="ignore"))
    else:
        objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
    recibido = objsocket.recv(1024)
    print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
objsocket.close()