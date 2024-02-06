# Ericom CIPA Compliance

## To Do -- WORK IN PROGRESS
1. create output CSV file to be used in Tenant UI "import policy"
2. Works only with the Profile "All"

## Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)

## Introduction

This code will create an example Internet Security Policy that follows [CIPA Compliance requirements](https://www.usac.org/e-rate/applicant-process/starting-services/cipa/) using the [Ericom Security platform](https://www.ericom.com). Ericom Web Security will perform filtering and protection. The [cipa_categories.csv](./cipa_categories.csv) file is used as an input file and can be modified with additional Ericom Web Security categories based on current CIPA requirements.

*Note: The full category list can be seen in the Ericom tenant portal. You can also call the API endpoint. See [Ericom API](https://editor.swagger.io/?url=https://ztadmin.ericomcloud.net/api/v1/api-reference/specification.json) for more details. Reference endpoint /api/v1/policies/categories/names.*

## Requirements

- Access to ZTAdmin portal
- Ericom Security API key
- Python3

```
git clone git clone https://github.com/JeffGiroux/ericom-cipa-compliance.git
cd ericom-cipa-compliance
pip3 install -r requirements.txt
```

## Usage

1. Update [cipa_categories.csv](./cipa_categories.csv) as needed using current CIPA requirements. 

2. Execute python command.

Syntax:
```
python3 create_cipa_policy.py <Tenant ID> <API Key> </folder/Output-CSV-file>
```

Example:
```
python3 create_cipa_policy.py 555-444-333-222-111 keyAAABBBCCC ./output.csv

Authenticating and retrieving token...
Creating CIPA policy...
Updating Default policy...
Done!
```

3. View results

Example Output in CSV file:
```
{TBD -- sample-json-output}
```