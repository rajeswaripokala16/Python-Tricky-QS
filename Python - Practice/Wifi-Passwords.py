import subprocess

# Get all Wi‑Fi profiles
profiles_output = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles']
).decode('utf-8', errors='ignore')

profiles = []
for line in profiles_output.split('\n'):
    line = line.strip()
    if line.startswith("All User Profile"):
        # line looks like: "All User Profile     :  MyWifi"
        name = line.split(":", 1)[1].strip()
        profiles.append(name)

print("{:<30}  {:<}".format("SSID", "PASSWORD"))
print("-" * 45)

for ssid in profiles:
    try:
        # Get profile details including key
        result = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear']
        ).decode('utf-8', errors='ignore')

        password = ""
        for line in result.split('\n'):
            line = line.strip()
            if "Key Content" in line:
                # line looks like: "Key Content            : mypassword"
                password = line.split(":", 1)[1].strip()
                break

        print("{:<30}  {:<}".format(ssid, password))

    except subprocess.CalledProcessError:
        print("{:<30}  {:<}".format(ssid, "ENCODING ERROR"))
    except IndexError:
        print("{:<30}  {:<}".format(ssid, ""))  # no password found
