import subprocess
import os

WIRESHARK_PATH = r"C:\Program Files\Wireshark\Wireshark.exe"
INTERFACE_ID = "5"   # Loopback

def run_wireshark(port, protocol):
    if not os.path.exists(WIRESHARK_PATH):
        print("❌ Wireshark not found")
        return

    cap_filter = f"{protocol} port {port}"

    cmd = [
        WIRESHARK_PATH,
        "-i", INTERFACE_ID,
        "-k",
        "-f", cap_filter
    ]

    subprocess.Popen(cmd)
    print(f"🦈 Wireshark capturing {protocol.upper()} port {port}")
