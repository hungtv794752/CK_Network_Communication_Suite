import socket

HOST = "0.0.0.0"
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[TCP SERVER] Listening on {PORT}")

conn, addr = server.accept()
print("Client connected:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received:", data.decode())
    conn.sendall(b"ACK: " + data)

conn.close()
