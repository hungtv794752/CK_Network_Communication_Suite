import os
import sys
import subprocess
import json, time
from utils.wireshark import run_wireshark


# ========= UTILS =========
def run_bg(cmd):
    return subprocess.Popen(cmd, shell=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def run(cmd):
    os.system(cmd)

def run_cmd_new_window(cmd, title="CMD"):
    full_cmd = f'start "{title}" cmd /k {cmd}'
    subprocess.Popen(full_cmd, shell=True)

# ========= FEATURES =========
def run_dashboard():
    if WIRESHARK_ENABLED:
        print("[Wireshark] Capturing Dashboard traffic...")
        # HTTP
        run_wireshark(8080, "tcp")
        time.sleep(0.5)
        # REST API
        run_wireshark(8081, "tcp")
        time.sleep(0.5)
        # WebSocket
        run_wireshark(8765, "tcp")
        time.sleep(1)

    print("[+] Starting REST API...")
    run_bg("python http/rest_api.py")

    print("[+] Starting WebSocket Server...")
    run_bg("python http/websocket_server.py")

    print("[+] Starting HTTP Server...")
    run_bg("python http/http_server.py")

    time.sleep(2)
    print("\nDashboard is READY 🚀")
    print("👉 Open browser: http://localhost:8080/dashboard.html")
    input("\nPress Enter to return menu...")

def test_ssl():
    if WIRESHARK_ENABLED:
        print("[Wireshark] Capturing TLS traffic...")
        run_wireshark(9443, "tcp")
        time.sleep(1)

    print("[+] Starting TCP SSL Server...")
    run_bg("python -m tcp.tcp_ssl_server")

    time.sleep(2)

    print("[+] Running SSL client test...")
    run("python tcp/tcp_ssl_client.py")

    input("\nPress Enter to return menu...")




with open("services.json", encoding="utf-8") as f:
    SERVICES = json.load(f)

with open("tools.json", encoding="utf-8") as f:
    TOOLS = json.load(f)

WIRESHARK_ENABLED = True

def show_group(group):
    items = [(k, v) for k, v in SERVICES.items() if v.get("type") == group]
    for i, (_, svc) in enumerate(items, 1):
        print(f"{i}. {svc['name']}")
    print("0. Back")
    return items

def main_menu():
    status = "ON" if WIRESHARK_ENABLED else "OFF"
    print("\n=== NETWORK COMMUNICATION SUITE ===")
    print(f"Wireshark: {status}\n")
    print("1. Servers")
    print("2. Clients")
    print("3. Network Tools")
    print("4. Toggle Wireshark ON/OFF")
    print("5. Run Dashboard")
    print("6. Test SSL Server")
    print("0. Exit")

def main():
    global WIRESHARK_ENABLED

    while True:
        main_menu()
        choice = input("Select: ")

        if choice == "0":
            break

        elif choice == "4":
            WIRESHARK_ENABLED = not WIRESHARK_ENABLED
            print(f"Wireshark {'ENABLED' if WIRESHARK_ENABLED else 'DISABLED'}")
            time.sleep(1)

        elif choice == "1":
            items = show_group("server")
            sel = input("Select server: ")
            
            if not sel.isdigit() or int(sel) < 1 or int(sel) > len(items):
                continue

            if sel == "0": continue
            key, svc = items[int(sel)-1]

            if WIRESHARK_ENABLED and svc.get("capture"):
                run_wireshark(svc["port"], svc["protocol"])
                time.sleep(1)

            run_cmd_new_window(svc["cmd"], svc["name"])

        elif choice == "2":
            items = show_group("client")
            sel = input("Select client: ")
            if sel == "0": continue
            key, svc = items[int(sel)-1]

            if WIRESHARK_ENABLED and svc.get("capture"):
                run_wireshark(svc["port"], svc["protocol"])
                time.sleep(1)

            run_cmd_new_window(svc["cmd"], svc["name"])

        elif choice == "3":
            print("\n--- NETWORK TOOLS ---")
            keys = list(TOOLS.keys())
            for i, k in enumerate(keys, 1):
                print(f"{i}. {TOOLS[k]['name']}")
            print("0. Back")

            sel = input("Select tool: ")
            if sel == "0": continue
            tool = TOOLS[keys[int(sel)-1]]
            run_cmd_new_window(tool["cmd"], tool["name"])

        elif choice == "5":
            run_dashboard()

        elif choice == "6":
            test_ssl()

if __name__ == "__main__":
    main()
