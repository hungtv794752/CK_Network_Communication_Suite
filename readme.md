🖧 Network Communication Suite

Network Communication Suite là một bộ công cụ Python dùng để mô phỏng, kiểm thử và phân tích các giao thức mạng (HTTP, REST API, WebSocket, TCP/SSL) với menu điều khiển tập trung và tích hợp Wireshark tự động để capture traffic.

Phù hợp cho:

Học tập Network / Security

Demo giao thức mạng

Test client–server

Phân tích traffic thực tế bằng Wireshark

🚀 Tính năng chính
📡 Server & Client Management

Quản lý Server và Client thông qua menu

Mở mỗi service trong CMD window riêng

Cấu hình động thông qua services.json

🌐 Dashboard Web

HTTP Server (Port 8080)

REST API Server (Port 8081)

WebSocket Server (Port 8765)

Giao diện Dashboard truy cập tại:

http://localhost:8080/dashboard.html

🔐 SSL / TLS Testing

TCP SSL Server

SSL Client test

Capture TLS traffic bằng Wireshark

🦈 Wireshark Integration

Bật / tắt Wireshark trực tiếp trong menu

Tự động capture theo:

Port

Protocol (TCP)

Áp dụng cho Server, Client, Dashboard, SSL

🛠 Network Tools

Danh sách công cụ mạng riêng

Quản lý bằng tools.json

📋 Yêu cầu hệ thống

Python 3.8+

Wireshark (đã cài & thêm vào PATH)

Hệ điều hành:

✅ Windows (khuyến nghị)

⚠ Linux / macOS (cần chỉnh lệnh cmd)

📦 Thư viện cần thiết

Cài đặt các package Python sau:

flask
flask-cors
websockets
psutil
cryptography


Cài nhanh bằng pip:

pip install flask flask-cors websockets psutil cryptography

📁 Cấu trúc thư mục (ví dụ)
.
├── http
│   ├── __init__.py
│   ├── dashboard.html
│   ├── email_smtp.py
│   ├── http_server.py
│   ├── rest_api.py
│   └── websocket_server.py
│
├── security
│   ├── certs
│   │   ├── server.crt
│   │   └── server.key
│   ├── __init__.py
│   └── ssl_context.py
│
├── tcp
│   ├── __init__.py
│   ├── tcp_client.py
│   ├── tcp_multiclient.py
│   ├── tcp_server.py
│   ├── tcp_ssl_client.py
│   └── tcp_ssl_server.py
│
├── tools
│   ├── __init__.py
│   ├── netstat_info.py
│   ├── nslookup_test.py
│   ├── ping_test.py
│   └── traceroute_test.py
│
├── udp
│   ├── __init__.py
│   ├── udp_broadcast.py
│   ├── udp_client.py
│   ├── udp_ipv6.py
│   └── udp_server.py
│
├── utils
│   ├── __init__.py
│   └── wireshark.py
│
├── LICENSE
├── main.py
├── readme.md
├── requirements.txt
├── services.json
└── tools.json

▶️ Cách chạy chương trình
python main.py


Menu chính:

=== NETWORK COMMUNICATION SUITE ===
Wireshark: ON

1. Servers
2. Clients
3. Network Tools
4. Toggle Wireshark ON/OFF
5. Run Dashboard
6. Test SSL Server
0. Exit

🧪 Test Dashboard

Chọn:

5. Run Dashboard


Sau khi chạy xong, mở trình duyệt:

http://localhost:8080/dashboard.html

🔐 Test SSL

Chọn:

6. Test SSL Server


Chương trình sẽ:

Chạy TCP SSL Server

Capture TLS traffic (nếu Wireshark bật)

Chạy SSL Client test

⚙️ Cấu hình Services & Tools
services.json

Khai báo server/client

Port, protocol

Lệnh chạy

Có capture Wireshark hay không

tools.json

Danh sách công cụ mạng

Lệnh thực thi riêng

📝 Ghi chú

Wireshark có thể yêu cầu quyền Administrator

Một số port cần đảm bảo chưa bị chiếm

Dashboard và SSL test sẽ tự động mở capture nếu Wireshark bật

📌 Mục đích dự án

Demo – học tập – thực hành Network Programming & Traffic Analysis
Không khuyến nghị dùng cho môi trường production