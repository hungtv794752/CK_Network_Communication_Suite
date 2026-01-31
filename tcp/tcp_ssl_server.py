import socket
from security.ssl_context import create_ssl_context

HOST = "0.0.0.0"
PORT = 9443

context = create_ssl_context()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

print("[SSL TCP Server] Running on port", PORT)

while True:
    client, addr = sock.accept()
    ssl_conn = context.wrap_socket(client, server_side=True)

    print("[SSL TCP Server] Secure connection from", addr)

    data = ssl_conn.recv(1024)
    ssl_conn.sendall(b"SSL ACK: " + data)

    ssl_conn.close()
