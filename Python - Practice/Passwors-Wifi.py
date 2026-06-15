import subprocess

def show_saved_wifi_passwords():
    # Get all Wi-Fi profiles
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8', errors='backslashreplace').split('\n')
    profiles = []
    for line in data:
        if "All User Profile" in line:
            profiles.append(line.split(":")[1].strip())

    print("Profile Name".ljust(30), "Password")
    print("-" * 45)

    # Get password for each profile
    for profile in profiles:
        try:
            result = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'],
                encoding='utf-8', errors='backslashreplace'
            ).split('\n')
            password = None
            for line in result:
                if "Key Content" in line:
                    password = line.split(":")[1].strip()
                    break
            print(profile.ljust(30), password if password else "--")
        except Exception as e:
            print(profile.ljust(30), "ERROR")
            # Uncomment for detailed error: # print("Error:", e)

show_saved_wifi_passwords()
