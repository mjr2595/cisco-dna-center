import requests
from dnac_config import DNAC_IP, DNAC_PASSWORD, DNAC_PORT, DNAC_USER
from requests.auth import HTTPBasicAuth


def get_device_health():
    """
    Building out function to retrieve health of devices. Using requests.get to make a call to the network device Endpoint
    """
    token = get_auth_token()  # Get Token
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/device-health"
    hdr = {"x-auth-token": token, "content-type": "application/json"}
    resp = requests.get(url, headers=hdr, verify=False)  # Make the Get Request
    device_list = resp.json()
    print(f"Number of devices: {len(device_list)}")
    print(device_list)


def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"  # Endpoint URL
    resp = requests.post(
        url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify=False
    )  # Make the POST Request
    token = resp.json()["Token"]  # Retrieve the Token
    return token  # Create a return statement for the Token


if __name__ == "__main__":
    get_device_health()
