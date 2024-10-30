import requests
from dnac_config import DNAC_IP, DNAC_PASSWORD, DNAC_PORT, DNAC_USER
from requests.auth import HTTPBasicAuth


def get_event_list():
    """
    Building out function to retrieve list of events. Using requests.get to make a call to the events Endpoint
    """
    token = get_auth_token()  # Get Token
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/event/event-series"
    hdr = {"x-auth-token": token, "content-type": "application/json"}
    resp = requests.get(url, headers=hdr, verify=False)  # Make the Get Request
    event_list = resp.json()
    # print(event_list)
    print_event_list(event_list)


def print_event_list(event_json):
    print("\n=== Event Series ===\n")
    for event in event_json:
        print("ID: {}".format(event["eventId"]))
        print("InstanceID: {}".format(event["instanceId"]))
        print("Namespace: {}".format(event["namespace"]))
        print("Name: {}".format(event["name"]))
        print("Description: {}".format(event["description"]))
        print("Version: {}".format(event["version"]))
        print("Category: {}".format(event["category"]))
        print("Domain: {}".format(event["domain"]))
        print("Sub-Domain: {}".format(event["subDomain"]))
        print("Source: {}".format(event["source"]))
        print("Timestamp: {}".format(event["timestamp"]))
        print("Start Time: {}".format(event["startTime"]))
        print("Details: {}".format(event["details"]))
        print("Event Hierarchy: {}".format(event["eventHierarchy"]))
        print("Type: {}".format(event["type"]))
        print("Severity: {}".format(event["severity"]))
        print("Network Info: {}".format(event["network"]))
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
