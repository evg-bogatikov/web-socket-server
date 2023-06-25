import socket
from src.main.bgtkv.handler import requestHandler

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8001

def start():
    server_socket = build_server_socket()
    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024).decode()
        response = requestHandler.handle_request_handshake(request)
        if response:
            client_socket.send(response.encode("utf-8"))
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = requestHandler.handler_request_message(data)
                print("Receive: " + message)


def build_server_socket():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((DEFAULT_HOST, DEFAULT_PORT))
    server.listen()
    return server

if __name__ == "__main__":
    start()
