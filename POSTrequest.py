import requests
import json

# URL of the public API for creating a new post
url = 'https://jsonplaceholder.typicode.com/posts'

# Data to be sent in the POST request
post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Convert the data to JSON format
json_data = json.dumps(post_data)

# Headers to indicate the type of data being sent
headers = {'Content-Type': 'application/json'}

# Make the POST request to the API
response = requests.post(url, data=json_data, headers=headers)

# Check if the request was successful
if response.status_code == 201:
    # Print the JSON response
    print(response.json())
else:
    print(f"Failed to create data: {response.status_code}")
