import requests
import phonenumbers
from phonenumbers import geocoder

def trace_location():
    try:
        print("[+] Starting device IP-based location trace ...")
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        print("[+] Location Trace Info (IP based)")
        print(f"[*] IP Address: {data.get('ip')}")
        print(f"[*] City/Town: {data.get('city')}")
        print(f"[*] Region/State: {data.get('region')}")
        print(f"[*] Country: {data.get('country')}")
        print(f"[*] Postal Code: {data.get('postal')}")
        print(f"[*] Latitude/Longitude: {data.get('loc')}")
        print(f"[*] Organization/ISP: {data.get('org')}")
        print("[+] IP trace complete.")

        # Phone number region lookup (not live GPS)
        number = input("Enter phone number with country code (e.g. +91 ********): ")
        try:
            parsed_number = phonenumbers.parse(number, None)
            region = geocoder.description_for_number(parsed_number, "en")
            print(f"[+] Phone number {number} is registered in: {region}")
        except Exception as e:
            print("Could not trace phone number location:", e)
    except Exception as e:
        print("Error tracing location:", e)

# Run it
trace_location()


