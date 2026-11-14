"""
Section 02: RESTCONF Foundations

TODO: Apply your Module 4 requests skills to network automation!
CHALLENGE: Build functions to get device information via RESTCONF

Key Concepts:
- RESTCONF = REST + NETCONF (HTTP API for network devices)
- Uses same requests library you know from Module 4
- Returns JSON data just like regular APIs
- Authentication and headers work the same way

Device Info:
- Host: sandbox-iosxe-latest-1.cisco.com
- Username: admin  
- Password: C1sco12345
- Base URL: https://HOST/restconf/data/
"""

# TODO: Import what you need
import requests
from requests.auth import HTTPBasicAuth
import json


# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = "devnetsandboxiosxec8k.cisco.com"

port = 443

auth = HTTPBasicAuth('admin', 'C1sco12345')

headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}


def get_device_hostname():
    """
    TODO: Get the device hostname via RESTCONF
    
    CHALLENGE: Make a GET request to get system hostname
    Endpoint: /ietf-system:system-state/hostname
    Headers: {"Accept": "application/yang-data+json"}
    
    Hint: Just like Module 4 APIs but for network devices!
    """
    endpoint = "/restconf/data/Cisco-IOS-XE-native:native/hostname"

    url = f"https://{host}:{port}{endpoint}"
    response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        hostname = data['Cisco-IOS-XE-native:hostname']
        print(f"Device Hostname: {hostname}")
    else:
        print(f"Failed to get hostname. Status Code: {response.status_code}, Response: {response.text}")


def list_all_interfaces():
    """
    TODO: Get a list of all device interfaces
    
    CHALLENGE: Parse the JSON response to show interface names
    Endpoint: /ietf-interfaces:interfaces
    
    Hint: The response structure has nested data - explore it!
    """
    endpoint = "/restconf/data/ietf-interfaces:interfaces"

    url = f"https://{host}:{port}{endpoint}"
    response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        interfaces = data['ietf-interfaces:interfaces']['interface']
        interface_names = [iface['name'] for iface in interfaces]
        print("Device Interfaces:")
        for name in interface_names:
            print(f"- {name}")
    else:
        print(f"Failed to get interfaces. Status Code: {response.status_code}, Response: {response.text}")

def get_interface_details(interface_name):
    """
    TODO: Get detailed info about a specific interface
    
    CHALLENGE: Get info for one interface by name
    Endpoint: /ietf-interfaces:interfaces/interface={name}
    
    Parameters:
    - interface_name: Name like "GigabitEthernet1"
    
    Hint: Try different interface names to see what exists!
    """
    endpoint = f"/restconf/data/ietf-interfaces:interfaces/interface={interface_name}"

    url = f"https://{host}:{port}{endpoint}"
    response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"\n{'=' * 40}")
        print(f"Interface Details for {interface_name}:")
        print(f"=" * 40)
        details = data['ietf-interfaces:interface']
        for interface in details:
            print(f"Name: {interface['name']}")
            print(f"Type: {interface['type']}")
            print(f"Enabled: {interface['enabled']}")
            # The following can be handled cleaner, but they require going deper inte nested dictionaries. For simplicity, we can use .get() with defaults.
            print(f"Description: {interface.get('description', 'No description')}")
            print(f"IPv4 Address: {interface.get('ietf-ip:ipv4', {}).get('address', 'No IPv4 address')}")
            print(f"IPv6 Address: {interface.get('ietf-ip:ipv6', {}).get('address', 'No IPv6 address')}")
    else:
        print(f"Failed to get interface details. Status Code: {response.status_code}, Response: {response.text}")

def explore_device_capabilities():
    """
    TODO: Explore what RESTCONF operations this device supports
    
    CHALLENGE: Try the capabilities endpoint
    Endpoint: /ietf-restconf-monitoring:restconf-state/capabilities
    
    Hint: This tells you what the device can do!
    """
    endpoint = "/restconf/data/ietf-restconf-monitoring:restconf-state/capabilities"

    url = f"https://{host}:{port}{endpoint}"
    response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"\n{'=' * 40}")
        print("Device Capabilities:")
        print(f"=" * 40)
        details = data['ietf-restconf-monitoring:capabilities']['capability']
        for capability in details:
            print(f"- {capability}")
    else:
        print(f"Failed to get capabilities. Status Code: {response.status_code}, Response: {response.text}")

# TODO: Write a main() function to test your functions
def main():
    """
    This is the main function that will call the other functions to explore the network device.
    """
    get_device_hostname()
    list_all_interfaces()
    get_interface_details("GigabitEthernet1")
    explore_device_capabilities()
# TODO: Add proper if __name__ == "__main__" guard
if __name__ == "__main__":
    main()
