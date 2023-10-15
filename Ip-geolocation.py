#By:Khaled Dafi
#10/15/2023

import requests

def get_location(ip_address=None):

    url = f"https://ipinfo.io/{ip_address}/json" if ip_address else "https://ipinfo.io/json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        ip = data['ip']
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        org = data.get('org', 'N/A')

        return f"IP Address: {ip}\nCity: {city}\nRegion: {region}\nCountry: {country}\nOrganization: {org}"

    except requests.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    ip = input("Enter an IP address (or press Enter to check your own IP): ")
    print(get_location(ip.strip() or None))
