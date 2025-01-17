
import psutil
import socket
def client():
    print("Client Initiated")
    server_ip="127.0.0.1"
    server_port=8000
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip,server_port))
        data=client_socket.recv(1024).decode()
        print(f"data received {data}")
        net_info()


def net_info():
    net =psutil.net_io_counters()
    print(net.bytes_sent,net.bytes_recv)

client()