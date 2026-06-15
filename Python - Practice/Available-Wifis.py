import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8', errors='backslashreplace').split('\n')
print("Available Wi-Fi profiles on your system:")
for line in data:
    if "All User Profile" in line:
        print(line.split(":")[1].strip())
