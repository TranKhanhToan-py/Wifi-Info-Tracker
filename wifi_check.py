import subprocess
import time
import os
from datetime import datetime

def get_wifi_info():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], encoding='utf-8')
        lines = result.splitlines()
        
        wifi_info = {}
        for line in lines:
            if "State" in line:
                wifi_info['State'] = line.split(":")[1].strip()
            elif "SSID" in line and "BSSID" not in line:
                wifi_info['SSID'] = line.split(":")[1].strip()
            elif "Signal" in line:
                wifi_info['Signal'] = line.split(":")[1].strip()
            elif "Radio type" in line:
                wifi_info['RadioType'] = line.split(":")[1].strip()
            elif "Authentication" in line:
                wifi_info['Authentication'] = line.split(":")[1].strip()
            elif "Encryption" in line:
                wifi_info['Encryption'] = line.split(":")[1].strip()

        if wifi_info.get("State", "").lower() == "connected":
            return wifi_info
        else:
            return {"Status": "Not connected to Wi-Fi"}

    except subprocess.CalledProcessError as e:
        return {"Status": "Error", "Details": str(e)}

try:
    while True:
        wifi = get_wifi_info()
        now = datetime.now()  # Cập nhật thời gian tại đây
        os.system('cls')
        print("=== Wi-Fi Info ===")
        for key, value in wifi.items():
            print(f"{key:<15}: {value}")
        print("Time now: ", now.strftime("%d/%m/%Y %H:%M:%S"))
        print("Press Ctrl + C to stop...")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("-----------------------")
    print("stopped tracking Wi-fi!")
    print("-----------------------")
