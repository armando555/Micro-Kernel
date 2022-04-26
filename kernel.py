import socket
import json
host = "localhost"
port = 5001
objsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket.connect((host,port))
print("starting client")

while(True):
    message = {"action":"","value":""} 
    operation = input("Ingrese operacion\n")
    value = input("Ingrese el valor\n")
    message["action"] = operation
    message["value"] = value
    enviar = json.dumps(message)
    objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
    recibido = objsocket.recv(1024)
    print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
objsocket.close()