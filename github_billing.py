import argparse
import requests
import json
import os
from dotenv import load_dotenv



def github_org_actions_billing(organization:str):
    """ pull github org billing details"""
    org_billing_endpoint = f'https://api.github.com/orgs/{organization}/settings/billing/actions'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    # API call here
    response = requests.get(url=org_billing_endpoint, headers=headers)
    response_json = response.json()
    if response.status_code == 200:
        print(f"API request successful on {org_billing_endpoint}")
        # print(response_json)
    else:
        print(f"API request failed with status code {response.status_code}:")
        # print(response_json)
    json_data = json.dumps(response_json, indent=4)
    # Write JSON string to a file
    with open("org_billing_details.json", "w") as file:
        file.write(json_data)

def github_org_packages_billing(organization: str):
    """
    pull github org billing details
    :param organization:
    :return:
    """
    org_package_billing_endpoint = f'https://api.github.com/orgs/{organization}/settings/billing/packages'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    # API call here
    response = requests.get(url=org_package_billing_endpoint, headers=headers)
    response_json = response.json()
    if response.status_code == 200:
        print(f"API request successful on {org_package_billing_endpoint}")
        # print(response_json)
    else:
        print(f"API request failed with status code {response.status_code}:")
        # print(response_json)
    json_data = json.dumps(response_json, indent=4)
    # Write JSON string to a file
    with open("org_package_billing_details.json", "w") as file:
        file.write(json_data)

def github_user_actions_billing(user: str):
    """
    pull github org billing details
    :param user:
    :return:
    """
    user_actions_billing_endpoint = f'https://api.github.com/users/{user}/settings/billing/actions'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN_CLASSIC')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    # API call here
    response = requests.get(url=user_actions_billing_endpoint, headers=headers)
    response_json = response.json()
    if response.status_code == 200:
        print(f"API request successful on {user_actions_billing_endpoint}")
        # print(response_json)
    else:
        print(f"API request failed with status code {response.status_code}:")
        # print(response_json)
    json_data = json.dumps(response_json, indent=4)
    # Write JSON string to a file
    with open("user_actions_billing_details.json", "w") as file:
        file.write(json_data)

def github_user_packages_billing(user: str):
    """
    pull github org billing details
    :param user:
    :return:
    """
    user_actions_billing_endpoint = f'https://api.github.com/users/{user}/settings/billing/packages'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN_CLASSIC')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    # API call here
    response = requests.get(url=user_actions_billing_endpoint, headers=headers)
    response_json = response.json()
    if response.status_code == 200:
        print(f"API request successful on {user_actions_billing_endpoint}")
        # print(response_json)
    else:
        print(f"API request failed with status code {response.status_code}:")
        # print(response_json)
    json_data = json.dumps(response_json, indent=4)
    # Write JSON string to a file
    with open("user_packages_billing_details.json", "w") as file:
        file.write(json_data)


def main():
    """ main function to test"""
    load_dotenv()
    parser = argparse.ArgumentParser(description="Github organization billing details")
    parser.add_argument("--organization", required=True, type=str, help="Github organization name")
    parser.add_argument("--account_name",required=True, type=str, help="Github user name")
    args = parser.parse_args()
    organization = args.organization
    account_name = args.account_name
    github_org_actions_billing(organization=organization)
    github_org_packages_billing(organization=organization)
    github_user_actions_billing(user=account_name)
    github_user_packages_billing(user=account_name)

if __name__ == '__main__':
    main()