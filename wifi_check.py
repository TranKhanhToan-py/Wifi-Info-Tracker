"""
⚠️ CẢNH BÁO PHÁP LÝ ⚠️

Công cụ này chỉ được phép sử dụng để kiểm tra thông tin Wi-Fi của thiết bị chính chủ.
Nghiêm cấm sử dụng để quét, truy cập hoặc lấy thông tin từ thiết bị của người khác khi chưa có sự đồng ý hợp pháp.

Tác giả KHÔNG chịu bất kỳ trách nhiệm nào đối với các hành vi sử dụng sai mục đích hoặc vi phạm pháp luật của người dùng.

Sử dụng công cụ này đồng nghĩa với việc bạn đồng ý với các điều khoản trên.

Bản quyền © 2025 by trankhanhtoan5b@gmail.com
-----------------------------------------------------------------------------------------------
⚠️ LEGAL WARNING ⚠️

This tool is only allowed to be used to check the Wi-Fi information of the owner's device.
It is strictly forbidden to use it to scan, access or retrieve information from other people's devices without legal consent.

The author is NOT responsible for any misuse or illegal use by users.

Using this tool means you agree to the above terms.

Copyright © 2025 by trankhanhtoan5b@gmail.com
"""

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
    print("""
==============================
⚠️ CẢNH BÁO PHÁP LÝ ⚠️
Chỉ dùng để kiểm tra Wi-Fi trên thiết bị cá nhân.
Nghiêm cấm sử dụng cho thiết bị người khác khi chưa được phép.
Tác giả không chịu trách nhiệm cho mọi hành vi sai phạm.
==============================
""")
    time.sleep(5)
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
