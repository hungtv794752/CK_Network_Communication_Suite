import socket

HOST = "::"        # IPv6 any
PORT = 9004

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("[UDP IPv6] Server listening on port", PORT)

while True:
    data, addr = sock.recvfrom(1024)
    print("Received from", addr, ":", data.decode())
    sock.sendto(b"UDP IPv6 ACK", addr)
