import asyncio 
import websockets


async def echo(websocket):
    async for message in websocket:
        print(message)
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 7777):
        await asyncio.Future()  # run forever


if __name__=='__main__':
    asyncio.run(main())