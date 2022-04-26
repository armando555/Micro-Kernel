import socket
host = "localhost"
port = 5001
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server is running waiting for connections")
active_connection, address = server.accept()

while(True):
    recibido = active_connection.recv(1024)
    print("Client answer: "+recibido.decode(encoding="ascii", errors="ignore"))
    enviar = input("Server: ")
    active_connection.send(enviar.encode(encoding="ascii",errors="ignore"))

active_connection.close()