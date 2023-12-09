import requests
import json
import uuid, sys, time


def get_jwt(tenant, key):
    url = "https://ztadmin.ericomcloud.net/api/v1/auth"
    payload = json.dumps({
      "tenantID": tenant,
      "key": key
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    jwt = response.json()['JWT']
    cookie = response.cookies['route']
    return jwt, cookie

def logout(jwt):
    url = "https://ztadmin.ericomcloud.net/api/v1/auth"
    headers = {
      'Content-Type': 'application/json',
      'Authorization': (f'Bearer {jwt}')
    }
    response = requests.request("DELETE", url, headers=headers)
    return response

def create_policy_category(category,access,jwt,cookie):
    url = "https://ztadmin.ericomcloud.net/api/v1/policies/categories"
    payload = json.dumps({
      "category": category,
      "profile": "All",
      "access": access
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': (f'Bearer {jwt}'),
      'Cookie': 'route={0}'.format(str(cookie))
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def usage():
    print("Usage: python3 create_cipa_policy.py <Tenant ID> <API Key> </folder/Output-CSV-file>")

if __name__ == "__main__":
    
    try:
        auth_tenant = sys.argv[1]
    except:
        print("Tenant ID missing")
        usage()
        exit(1)
    try:
        key = sys.argv[2]
    except:
        print("API Key missing")
        usage()
        exit(1)
    try:
        outputFile = sys.argv[3]
    except:
        print("Output File missing")
        usage()
        exit(1)
    
    print("Authenticating and retrieving token...")
    jwt, cookie = get_jwt(auth_tenant, key)

    inputFile = "cipa_categories.csv"

    with open(inputFile, 'r') as file, open(outputFile, 'w') as output_file:
        # Skip input file header row
        header = next(file)

        # Write output file header row
        output_file.write("Category,Access\n")
        print("Creating CIPA policy...")
        for line in file:
            # Assuming each line contains values separated by a comma
            values = line.strip().split(',')
            category = values[0]
            access = values[1]
            #resp = create_policy_category(category,access,jwt,cookie)
            output_file.write(f'{category},{access}\n')
            print(category,access)
    
    print("Done!")

    logout(jwt)

