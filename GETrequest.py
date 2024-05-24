import requests

# URL of the public API
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the JSON response
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code}")
