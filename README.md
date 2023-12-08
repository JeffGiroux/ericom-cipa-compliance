# ZTEdge CIPA Compliance

## Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)

## Introduction

This code will create an Internet Security Policy that is CIPA Compliant using [Ericom's ZTEdge platform](https://www.ericom.com) to provide filtering and protection.

## Requirements

- Access to ZTAdmin portal
- ZTEdge API key
- Python3

```
git clone git clone https://github.com/JeffGiroux/ztedge-cipa-compliance.git
cd ztedge-cipa-compliance
pip3 install -r requirements.txt
```

## Usage

1. Execute python command.

Syntax:
```
python3 create_cipa_policy.py <Tenant ID> <API Key> </folder/Output-CSV-file>
```

Example:
```
python3 create_cipa_policy.py 555-444-333-222-111 keyAAABBBCCC ./output.csv

Authenticating and retrieving token...
Creating CIPA policy...
Done!
```

2. View results

Example Output in CSV file:
```
{TBD -- sample-json-output}
```