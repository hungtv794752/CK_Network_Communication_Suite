import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Message: ")
    sock.sendto(msg.encode(), ("127.0.0.1", 9001))
    data, _ = sock.recvfrom(1024)
    print(data.decode())
