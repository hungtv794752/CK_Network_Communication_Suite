import socket, threading

HOST = "0.0.0.0"
PORT = 9002

def handle_client(conn, addr):
    print("Client:", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()

server = socket.socket()
server.bind((HOST, PORT))
server.listen()

print("Multi TCP Server running")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
