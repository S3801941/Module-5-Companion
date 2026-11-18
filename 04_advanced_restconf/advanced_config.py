"""
Section 04: RESTCONF Configuration

TODO: Master configuration changes using RESTCONF PUT/PATCH operations  
CHALLENGE: Make safe configuration changes to network devices!

WARNING: These are REAL configuration changes!
- Start with safe changes (descriptions, non-critical settings)
- Always read current config before changing
- Verify changes after applying

Key Concepts:  
- GET = Read configuration
- PUT = Replace/Update configuration  
- PATCH = Modify part of configuration
- DELETE = Remove configuration
"""

# TODO: Import what you need
import requests
from requests.auth import HTTPBasicAuth
import json


# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = "devnetsandboxiosxec9k.cisco.com"

port = 443

auth = HTTPBasicAuth('s3801941', 'vr%5rN66BdY*')

headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

def read_before_write():
    """
    TODO: ALWAYS read current configuration before making changes
    
    CHALLENGE: Get current interface description for GigabitEthernet1
    Endpoint: /ietf-interfaces:interfaces/interface=GigabitEthernet1
    
    Best Practice: Never change config without knowing current state!
    """
    endpoint = "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

    url = f"https://{host}:{port}{endpoint}"
    response = requests.get(url, auth=auth, headers=headers, verify=False, timeout=15)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        description = data['ietf-interfaces:interface']
        for interface in data['ietf-interfaces:interface']:
            if interface['name'] == 'GigabitEthernet1':
                description = interface.get('description', 'No description set')
                print(f"Current Description for GigabitEthernet1: {description}")
    else:
        print(f"Failed to read current configuration. Status Code: {response.status_code}, Response: {response.text}")

def update_interface_description():
    """
    TODO: Safely update an interface description
    
    CHALLENGE: Use PUT to change interface description
    Endpoint: /ietf-interfaces:interfaces/interface=GigabitEthernet1/description
    Method: PUT
    Data: Just a string with new description
    
    Hint: PUT replaces the entire description field
    """
    endpoint = "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"
    new_description = "Updated via RESTCONF PUT"
    interface_data = {
        "ietf-interfaces:interface": {
            "name": "GigabitEthernet1",
            "description": new_description,
            "enabled": True,
            "type": "iana-if-type:ethernetCsmacd"
        }
    }

    url = f"https://{host}:{port}{endpoint}"
    response = requests.put(url, auth=auth, headers=headers, data=json.dumps(interface_data), verify=False, timeout=15)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code in [200, 204]:
        print(f"Successfully updated description for GigabitEthernet1 to: '{new_description}'")
    else:
        print(f"Failed to update description. Status Code: {response.status_code}, Response: {response.text}")

def enable_disable_interface():
    """
    TODO: Practice enabling/disabling an interface  
    
    CHALLENGE: Change admin-status of an interface
    Endpoint: /ietf-interfaces:interfaces/interface=GigabitEthernet1/enabled
    Data: true (enable) or false (disable)
    
    WARNING: Be careful - this affects network connectivity!
    """
    endpoint = "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1/enabled"
    new_status = False  # Change to True to enable, False to disable
    interface_data = {
        "ietf-interfaces:enabled": new_status
    }

    url = f"https://{host}:{port}{endpoint}"
    response = requests.put(url, auth=auth, headers=headers, data=json.dumps(interface_data), verify=False, timeout=15)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code in [200, 204]:
        status_str = "enabled" if new_status else "disabled"
        print(f"Successfully {status_str} GigabitEthernet1")
    else:
        print(f"Failed to change interface status. Status Code: {response.status_code}, Response: {response.text}")

def bulk_configuration_change():
    """
    TODO: Update multiple interface properties at once
    
    CHALLENGE: Use PUT on entire interface to change multiple things:
    - description
    - enabled status  
    - maybe MTU?
    
    Endpoint: /ietf-interfaces:interfaces/interface=GigabitEthernet1
    
    Hint: Send complete interface object with all properties
    """
    pass

def configuration_rollback():
    """
    TODO: Learn to undo changes (restore original settings)
    
    CHALLENGE: 
    1. Save original configuration
    2. Make a change
    3. Restore original configuration
    
    Hint: Store the original data from your GET request!
    """
    pass

def error_handling_and_validation():
    """
    TODO: Handle configuration errors gracefully
    
    CHALLENGE: Try these scenarios and handle errors:
    - Invalid interface name
    - Invalid configuration data
    - Device busy/locked
    - Authentication failure
    
    Hint: Check response status codes and error messages!
    """
    pass

# TODO: Create main() function with step-by-step configuration workflow
def main():
    # Step 1: Read current configuration
    read_before_write()
    
    # Step 2: Update interface description
    #update_interface_description()
    
    # Step 3: Enable/Disable interface
    #enable_disable_interface()
    
    # Step 4: Bulk configuration change
    #bulk_configuration_change()
    
    # Step 5: Rollback changes if needed
    #configuration_rollback()
    
    # Step 6: Handle errors and validate changes
    #error_handling_and_validation()

# TODO: Add proper error handling and rollback capabilities
if __name__ == "__main__":
    main()