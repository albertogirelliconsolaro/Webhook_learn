import requests
import json

# Replace 'your_api_key' with your actual Alchemy API key
alchemy_api_key = 'xxxxxx'

# Alchemy Ethereum node endpoint
url = 'https://eth-mainnet.alchemyapi.io/v2/{}'.format(alchemy_api_key)

# JSON-RPC request payload to get the latest block number
payload = {
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
    "id": 1
}

# Send POST request to Alchemy Ethereum node
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    if 'result' in data:
        # Extract block number from response
        block_number = int(data['result'], 16)
        print("Latest block number on Ethereum mainnet:", block_number)
    else:
        print("Error: Response does not contain block number")
else:
    print("Error:", response.status_code)