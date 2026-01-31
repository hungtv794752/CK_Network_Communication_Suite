import socket

HOST = "127.0.0.1"
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input("Message: ")
    if msg == "exit":
        break
    client.send(msg.encode())
    print(client.recv(1024).decode())

client.close()
