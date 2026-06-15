import subprocess

def get_wifi_password(profile_name):
    try:
        results = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'],
            encoding='utf-8', errors='backslashreplace'
        ).split('\n')
        password = None
        for line in results:
            if "Key Content" in line:
                password = line.split(':')[1].strip()
                break
        if password:
            print(f"Password for '{profile_name}': {password}")
        else:
            print(f"Password for '{profile_name}' not found (may be open network or not saved).")
    except Exception as e:
        print(f"Error occurred for '{profile_name}': {e}")

# Usage example—replace 'YOUR_WIFI_NAME' with your SSID
get_wifi_password("Brundavanam2G")
