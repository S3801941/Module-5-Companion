"""
Section 03: YANG Model Explorer

TODO: Understand YANG models - the "blueprints" for network device data
CHALLENGE: Figure out how network devices organize their data!

Key Concepts:
- YANG = Data modeling language for network configuration/state
- Like a "schema" or "blueprint" that defines what data exists
- RESTCONF uses YANG paths to access specific data
- Think: YANG is the "menu", RESTCONF is how you "order"
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

auth = HTTPBasicAuth('s3801941', 'vr%5rN66BdY*')

headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}



def explore_yang_structure():
    """
    TODO: Examine how device data is organized using YANG models
    
    CHALLENGE: Compare these different YANG paths:
    1. /ietf-interfaces:interfaces (IETF standard model)  
    2. /Cisco-IOS-XE-native:native (Cisco-specific model)
    3. /ietf-system:system-state (System information)
    
    Hint: Try each endpoint and see what data structure you get back!
    """
    endpoints = [
        "/restconf/data/ietf-interfaces:interfaces",
        "/restconf/data/Cisco-IOS-XE-native:native",
        "/restconf/data/ietf-system:system-state" # Fails for some reason, but the Cisco one works. This is a good example of how different vendors can implement YANG models differently.
    ]

    for endpoint in endpoints:
        url = f"https://{host}:{port}{endpoint}"
        response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
        print(f"\n{'=' * 40}")
        print(f"Exploring YANG Path: {endpoint}")
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4))
        else:
            print(f"Failed to explore YANG path. Status Code: {response.status_code}, Response: {response.text}")

    

def find_interface_yang_paths():
    """
    TODO: Discover different ways to access interface data
    
    CHALLENGE: Try these interface-related YANG paths:
    - All interfaces: /ietf-interfaces:interfaces
    - One interface: /ietf-interfaces:interfaces/interface=GigabitEthernet1  
    - Interface stats: /ietf-interfaces:interfaces-state
    
    Question: What's the difference between config vs state data?
    """
    endpoints = [
        "/restconf/data/ietf-interfaces:interfaces",
        "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1",
        "/restconf/data/ietf-interfaces:interfaces-state"
    ]

    for endpoint in endpoints:
        url = f"https://{host}:{port}{endpoint}"
        response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
        print(f"\n{'=' * 40}")
        print(f"Exploring Interface YANG Path: {endpoint}")
        print(f"=" * 40)
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4))
        else:
            print(f"Failed to explore interface YANG path. Status Code: {response.status_code}, Response: {response.text}")

def compare_yang_models():
    """
    TODO: Compare IETF standard vs Cisco proprietary YANG models
    
    CHALLENGE: Get hostname using both approaches:
    1. IETF way: /ietf-system:system-state/hostname
    2. Cisco way: /Cisco-IOS-XE-native:native/hostname
    
    Discussion: Why might there be multiple ways to get the same data?
    """
    endpoints = [
        "/restconf/data/ietf-system:system-state/hostname", #IETF standard does not work for some reason, but the Cisco one does.
        "/restconf/data/Cisco-IOS-XE-native:native/hostname"
    ]

    for endpoint in endpoints:
        url = f"https://{host}:{port}{endpoint}"
        response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
        print(f"\n{'=' * 40}")
        print(f"Comparing YANG Model Path: {endpoint}")
        print(f"=" * 40)
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            details = data.get('ietf-system:hostname') or data.get('Cisco-IOS-XE-native:hostname')
            print(f"Hostname from {endpoint}: {details}")
        else:
            print(f"Failed to compare YANG model. Status Code: {response.status_code}, Response: {response.text}")

def build_yang_path_from_cli():
    """
    TODO: Practice converting CLI commands to YANG paths
    
    CHALLENGE: Figure out YANG equivalents for these CLI commands:
    - show interface GigabitEthernet1
    - show ip interface brief  
    - show version
    
    Hint: Use trial and error with different YANG paths!
    """
    endpoints = [
        "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1",
        "/restconf/data/ietf-interfaces:interfaces",
        "/restconf/data/Cisco-IOS-XE-native:native/version"
    ]

    for endpoint in endpoints:
        url = f"https://{host}:{port}{endpoint}"
        response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
        print(f"\n{'=' * 40}")
        print(f"Exploring YANG Path for CLI Equivalent: {endpoint}")
        print(f"=" * 40)
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4))
        else:
            print(f"Failed to explore YANG path. Status Code: {response.status_code}, Response: {response.text}")

def yang_data_types_exploration():
    """
    TODO: Explore different YANG data types in responses
    
    CHALLENGE: Find examples of:
    - Container: Groups related data (like "interfaces")
    - List: Multiple items (like interface list) 
    - Leaf: Single values (like hostname)
    
    Hint: Look at the JSON structure from your requests!
    """
    endpoints = [
        "/restconf/data/ietf-interfaces:interfaces",
        "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1",
        "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1/ietf-ip:ipv4",
    ]

    for endpoint in endpoints:
        url = f"https://{host}:{port}{endpoint}"
        response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
        print(f"\n{'=' * 40}")
        print(f"Exploring YANG Data Types at Path: {endpoint}")
        print(f"=" * 40)
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4))
        else:
            print(f"Failed to explore YANG data types. Status Code: {response.status_code}, Response: {response.text}")

# TODO: Create a main() function that calls these challenges
def main():
    explore_yang_structure()
    find_interface_yang_paths()
    compare_yang_models()
    build_yang_path_from_cli()
    yang_data_types_exploration()
# TODO: Add error handling and user-friendly output

if __name__ == "__main__":
    main()