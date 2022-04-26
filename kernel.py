import socket
host = "localhost"
port = 5001
objsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket.connect((host,port))
print("iniciamos cliente")

while(True):
    enviar = input("Client: ")
    objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
    recibido = objsocket.recv(1024)
    print("Servidor: "+recibido.decode(encoding="ascii", errors="ignore"))
objsocket.close()