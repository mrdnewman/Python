import requests

# API Endpoint URL for testing HTTP 500 response
api_url = "https://httpstat.us/500"

try:
    response = requests.get(api_url)

    # Check the HTTP status code
    if response.status_code == 500:
        print("HTTP 500 - Internal Server Error detected!")
    else:
        print(f"Received unexpected status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Failed to make the request: {e}")
