# Uncomment this to pass the first stage
import socket
import logging

def main() -> None:
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client, _ = server_socket.accept()

    while True:
        data:str = client.recv(1024).decode('utf-8')
        log.debug(f'Received message: {data}')
        client.send(b'+PONG\r\n')

if __name__ == "__main__":
    # Logger config
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    main()
