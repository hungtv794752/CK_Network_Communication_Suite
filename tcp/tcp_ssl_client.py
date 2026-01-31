import socket
import ssl

HOST = "localhost"
PORT = 9443

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        print("[SSL CLIENT] Connected with", ssock.version())
        ssock.sendall(b"Hello SSL Server")
        print("[SSL CLIENT] Received:", ssock.recv(1024))
