import requests

def get_device_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        print("[+] Location Trace OSINT Tool")
        print(f"[*] IP Address: {data.get('ip')}")
        print(f"[*] City: {data.get('city')}")
        print(f"[*] Region/State: {data.get('region')}")
        print(f"[*] Country: {data.get('country')}")
        print(f"[*] Postal: {data.get('postal')}")
        print(f"[*] Location (latitude,longitude): {data.get('loc')}")
        print(f"[*] Organization: {data.get('org')}")
        print("[+] Trace complete.")
    except Exception as e:
        print("Could not retrieve location:", e)

# Run the function
get_device_location()



