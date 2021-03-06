import json
import socket
import os
from datetime import datetime
import asyncio
import websockets


async def echo(websocket):
    async for message in websocket:
        print("gola ejej")
        print(message)
        retorno = handleConnection(message)
        await websocket.send(retorno)

async def main():
    async with websockets.serve(echo, "localhost", 7777):
        await asyncio.Future()  # run forever


def handleConnection(recv):
    message = json.loads(recv)
    if(message["cmd"] == "1" or message["cmd"] == "2"):
        message["action"] = "1" if message["cmd"] == "1" else "2"
        message["cmd"] = "send"
        message["dst"] = "file_manager"
        enviar = json.dumps(message)
        print(enviar)
        active_connection.send(enviar.encode(encoding="ascii",errors="ignore"))
        message = active_connection.recv(1024)
        print("PASE DE RECIBIRLO")
        message = message.decode(encoding="ascii",errors="ignore")
        
    elif(message["cmd"] == "3" or message["cmd"] == "4"):
        print("")
        message["action"] =  "3" if message["cmd"] == "3" else "4"
        message["cmd"] = "send"
        message["dst"] = "applications"
        enviar = json.dumps(message)
        active_connection.send(enviar.encode(encoding="ascii",errors="ignore"))
        message = active_connection.recv(1024).decode(encoding="ascii",errors="ignore")
        print("PASE DE RECIBIRLO")
    elif(message["action"] == "5"):
        print(message)  

    return message

    


if __name__=='__main__':
    host = "localhost"
    port = 5003
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(1)
    print("Server GUI-USER is running waiting for connections")
    active_connection, address = server.accept()

    recibido = active_connection.recv(1024)

    message = json.loads(recibido.decode(encoding="ascii", errors="ignore"))
    error = 1
    if(message["msg"]=="off"):
        print("Ejecución finalizada")
        os.exit(1)
    if(message["cmd"] == "start" and message["msg"]=="all"):
        print("GUI USER STARTED")
        error = 0

    asyncio.run(main())

