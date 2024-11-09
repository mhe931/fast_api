#!/usr/bin/env python3.12

import requests

# Server details
BASE_URL = "http://172.20.14.236:8000"
TOKEN_ENDPOINT = f"{BASE_URL}/token"
DATA_ENDPOINT = f"{BASE_URL}/api/dkg_data"

# User credentials and date range
username = "bot_user"
from_date = "14030908"
to_date = "14030909"

# Step 1: Request a JWT token
def get_token():
    response = requests.post(TOKEN_ENDPOINT, data={
        "username": username,
        "from_date": from_date,
        "to_date": to_date
    })
    if response.status_code == 200:
        token = response.json().get("access_token")
        print("Token obtained:", token)
        return token
    else:
        print("Failed to obtain token:", response.json())
        return None

# Step 2: Access the protected endpoint using the token
def get_data_with_token(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(DATA_ENDPOINT, headers=headers)
    
    if response.status_code == 200:
        print("Data obtained successfully:", response.json())
    else:
        print("Failed to obtain data:", response.json())

if __name__ == "__main__":
    # Request token and call the API with it
    token = get_token()
    if token:
        get_data_with_token(token)
