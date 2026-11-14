"""
Section 01: Network Device Explorer

TODO: Build functions to explore network devices using RESTCONF
CHALLENGE: Figure out how to connect to network devices using HTTP!

Hints:
- RESTCONF uses HTTPS (like a web API)  
- You need the right headers: {"Accept": "application/yang-data+json"}
- Base URL: https://sandbox-iosxe-latest-1.cisco.com/restconf/data/
- Credentials: admin/C1sco12345
- Don't forget to disable SSL warnings!
"""

# TODO: Import what you need (you know this from Module 4!)
import requests
from requests.auth import HTTPBasicAuth
import json
import base64
import sys

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
    TODO: Create a function to get the device hostname
    
    CHALLENGE: Make a GET request to get system hostname
    RESTCONF endpoint: /ietf-system:system-state/hostname
    
    Hint: Build the full URL, add auth, add headers, handle the response
    """

    endpoint = "/restconf/data/Cisco-IOS-XE-native:native/hostname"

    url = f"https://{host}:{port}{endpoint}"
    response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
    print(f"Response Status Code: {response.status_code}")

    data = response.json()

    hostname = data['Cisco-IOS-XE-native:hostname']
    print(f"Device Hostname: {hostname}")


def get_interfaces_list():
    """
    TODO: Create a function to list all device interfaces
    
    CHALLENGE: Get all interfaces from the device
    RESTCONF endpoint: /ietf-interfaces:interfaces
    
    Hint: Response will be JSON - dig into it to find interface names
    """

    endpoint = "/restconf/data/ietf-interfaces:interfaces"

    response = requests.get(f"https://{host}:{port}{endpoint}", auth=auth, headers=headers, verify=False, timeout=15)
    print(f"Response Status Code: {response.status_code}")
    data = response.json()
    print(f"=" * 40)
    print(f"Interfaces List:")
    print(f"=" * 40)

    for interface in data['ietf-interfaces:interfaces']['interface']:
        print(f"Interface Name: {interface['name']}")
        print(f"Interface Type: {interface['type']}")
        print(f"Interface Enabled: {interface['enabled']}")
        print(f"Interface Description: {interface.get('description', 'No description')}")
        print(f"Interface IPv4 Address: {interface.get('ietf-ip:ipv4', {}).get('address', 'No IPv4 address')}")
        print(f"Interface IPv6 Address: {interface.get('ietf-ip:ipv6', {}).get('address', 'No IPv6 address')}")
        print("-" * 40)
    print(f"=" * 40)

    print(f"=" * 40)
    print(f"Raw interface JSON Data:")
    print(f"=" * 40)
    print(f"Interfaces Data: {json.dumps(data, indent=2)}")

def explore_yang_paths():
    """
    TODO: Try different YANG paths to see what data you can get
    
    CHALLENGE: Experiment with these endpoints:
    - /Cisco-IOS-XE-native:native/hostname
    - /ietf-interfaces:interfaces/interface=GigabitEthernet1
    
    Hint: Some might work, some might not - that's learning!
    """

    hostname_url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-native:native/hostname"

    interface_url = f"https://{host}:{port}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

    response_hostname = requests.get(hostname_url, auth=auth, headers=headers, verify=False, timeout=15)
    print(f"Response Status Code for Hostname: {response_hostname.status_code}")

    response_interface = requests.get(interface_url, auth=auth, headers=headers, verify=False, timeout=15)
    print(f"Response Status Code for Interface: {response_interface.status_code}")

    print(f"Hostname Data: {json.dumps(response_hostname.json(), indent=2)}")
    print(f"\nInterface Data: {json.dumps(response_interface.json(), indent=2)}")
    pass

# TODO: Write a main() function to test everything
def main():
    """
    This is the main function that will call the other functions to explore the network device.
    """
    # Call the function to get the device hostname
    get_device_hostname()
    
    # Call the function to get the list of interfaces
    get_interfaces_list()
    
    # Call the function to explore different YANG paths
    explore_yang_paths()
    
# TODO: Don't forget if __name__ == "__main__":

if __name__ == "__main__":
    main()