# Uncomment this to pass the first stage
import socket
import logging
import asyncio

from asyncio import AbstractEventLoop

async def response(client:socket.socket, loop:AbstractEventLoop):
    while client:
        data = await loop.sock_recv(client, 1024)
        if not data:
            break
        await loop.sock_sendall(client, b'+PONG\r\n')

async def handle_connection(server_socket:socket.socket, loop:AbstractEventLoop):
    while True:
        client, addr = await loop.sock_accept(server_socket)
        client.setblocking(False)
        asyncio.create_task(response(client, loop))

async def main() -> None:
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.setblocking(False)
    server_socket.listen()
    await handle_connection(server_socket, asyncio.get_event_loop())

if __name__ == "__main__":
    # Logger config
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    asyncio.run(main())
