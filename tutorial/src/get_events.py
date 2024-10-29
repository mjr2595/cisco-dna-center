import requests
from dnac_config import DNAC_IP, DNAC_PASSWORD, DNAC_PORT, DNAC_USER
from requests.auth import HTTPBasicAuth


def get_event_list():
    """
    Building out function to retrieve list of events. Using requests.get to make a call to the events Endpoint
    """
    token = get_auth_token()  # Get Token
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/events?tags=ASSURANCE"
    hdr = {"x-auth-token": token, "content-type": "application/json"}
    resp = requests.get(url, headers=hdr, verify=False)  # Make the Get Request
    event_list = resp.json()
    print_event_list(event_list)


def print_event_list(event_json):
    for event in event_json:
        print("Event ID: {}".format(event["eventId"]))
        print("Event Name: {}".format(event["name"]))
        print("Event Severity: {}".format(event["severity"]))
        print("Event Description: {}".format(event["description"]))
        print("Event Category: {}".format(event["category"]))
        # print("Event Importance: {}".format(event["importance"]))
        print("\n")


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
    get_event_list()
