"""
Section 05: NETCONF Fundamentals 

TODO: Master NETCONF - the SSH/XML approach to network management
CHALLENGE: Learn a completely different protocol from RESTCONF!

Key Differences from RESTCONF:
- NETCONF = SSH + XML (not HTTP + JSON)
- More powerful: transactions, rollback, validation
- Uses ncclient library (new for you!)
- XML data format (different from JSON)

Connection Info:
- Host: sandbox-iosxe-latest-1.cisco.com
- Port: 830 (NETCONF standard port)
- Same username/password as RESTCONF
"""

# TODO: Import ncclient and XML libraries
import ncclient
from ncclient import manager
import xml.etree.ElementTree as ET

def establish_netconf_session():
    """
    TODO: Create your first NETCONF connection
    
    CHALLENGE: Connect to device using ncclient manager.connect_ssh()
    Parameters needed:
    - host, port (830), username, password
    - hostkey_verify=False (for lab environment)
    - device_params={'name': 'iosxe'} (Cisco specific)
    
    Hint: Use context manager (with statement) for auto-cleanup!
    """

    connection_params = {
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "port": 830,
        "username": "s3801941",
        "password": "vr%5rN66BdY*",
        "hostkey_verify": False,
        "device_params": {"name": "iosxe"}
    }

    with manager.connect_ssh(**connection_params) as m:
        print("NETCONF session established!")
        # Optional: Print server capabilities
        print("Server Capabilities:")
        server_capabilities = m.server_capabilities
        for cap in server_capabilities:
            print(cap)


def explore_device_capabilities():
    """
    TODO: Discover what the device supports via NETCONF
    
    CHALLENGE: Every NETCONF device advertises its capabilities
    - session.server_capabilities shows what device can do
    - Look for supported YANG models
    - Find NETCONF protocol versions
    
    Question: How do capabilities differ from RESTCONF discovery?
    """
    connection_params = {
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "port": 830,
        "username": "s3801941",
        "password": "vr%5rN66BdY*",
        "hostkey_verify": False,
        "device_params": {"name": "iosxe"}
    }

    with manager.connect_ssh(**connection_params) as m:
        print("Exploring device capabilities...")
        server_capabilities = m.server_capabilities
        for cap in server_capabilities:
            print(cap)

def get_configuration_data():
    """
    TODO: Retrieve device configuration using NETCONF
    
    CHALLENGE: Use session.get_config() method
    - source parameter: 'running', 'startup', or 'candidate'
    - Returns XML data (not JSON!)
    
    Advanced: Try with XPath filters to get specific data
    """
    pass

def get_operational_data():
    """
    TODO: Get device state/operational data (non-config)
    
    CHALLENGE: Use session.get() method (not get_config!)
    - Gets operational state, statistics, counters
    - Try filter parameter with XPath expressions
    
    Example filters to try:
    - filter=('xpath', '/interfaces-state')
    - filter=('subtree', '<interfaces/>')
    """
    pass

def parse_xml_responses():
    """
    TODO: Master XML parsing for NETCONF responses
    
    CHALLENGE: Learn xml.etree.ElementTree
    - Parse XML strings into Element objects  
    - Navigate XML hierarchy with findall(), find()
    - Extract text content from XML elements
    - Handle XML namespaces properly
    
    Hint: NETCONF XML has lots of namespaces - be prepared!
    """
    pass

def compare_netconf_vs_restconf():
    """
    TODO: Get the same data using both protocols
    
    CHALLENGE: Implement parallel functions:
    1. Get hostname via NETCONF (XML)
    2. Get hostname via RESTCONF (JSON) 
    3. Compare the responses and performance
    
    Discussion: When would you choose one over the other?
    """
    pass

# TODO: Build a comprehensive main() function
def main():

    # Establish NETCONF session
    establish_netconf_session()

    # Explore device capabilities
    explore_device_capabilities()

    # Get configuration data
    get_configuration_data()

    # Get operational data
    get_operational_data()

    # Parse XML responses
    parse_xml_responses()

    # Compare NETCONF vs RESTCONF
    compare_netconf_vs_restconf()

# TODO: Add robust error handling for network issues
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")