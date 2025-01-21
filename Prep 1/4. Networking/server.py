import psutil
import socket


def server():
    print("Server started")
    get_active_connections()
    server_ip="127.0.0.1"
    server_port=8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((server_ip, server_port))
        server_socket.listen()
        print("Server listening on port", server_port)

        while True:
            client_socket,client_address=server_socket.accept()
            print(f"Client connected {client_address}")
            client_socket.sendall(b"Hello, client!")
            client_socket.close()
            print("Client disconnected")
        


def get_active_connections():

    for conn in psutil.net_connections():
        if conn.raddr and conn.laddr:
            # Active Connections
            print(f"Local Address: {conn.laddr}, Port: {conn.laddr.port}")
            print(f"Remote Address: {conn.raddr}, Port: {conn.raddr.port}")
            print(f"Connection Status: {conn.status}")


server()