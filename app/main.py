# Uncomment this to pass the first stage
import socket

def main() -> None:
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.listen()

    while True:
        client, _ = server_socket.accept() # wait for client
        client.send(b'+PONG\r\n')
        client.send(b'+PONG\r\n')

if __name__ == "__main__":
    main()
