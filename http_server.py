from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

BASE_DIR = os.path.dirname(__file__)
os.chdir(BASE_DIR)   # 👈 CỰC KỲ QUAN TRỌNG

server = HTTPServer(("0.0.0.0", 8080), SimpleHTTPRequestHandler)
print("HTTP Server running on port 8080")
server.serve_forever()
