import requests
from requests_oauthlib import OAuth2Session


def fetch_protected_resource(url, oauth_session):
    try:
        response = oauth_session.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code

        # If the response was successful, no exception will be raised
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error 404: Resource not found at {url}")
        elif response.status_code == 500:
            print(f"Error 500: Server error at {url}")
        else:
            print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")

    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")

    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")


# Example usage
client_id = 'your_client_id'
client_secret = 'your_client_secret'
authorization_base_url = 'https://example.com/oauth/authorize'
token_url = 'https://example.com/oauth/token'
redirect_uri = 'https://yourapp.com/callback'

# Create an OAuth2 session
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

# Redirect user to the OAuth provider to authorize
authorization_url, state = oauth.authorization_url(authorization_base_url)
print(f'Please go to {authorization_url} and authorize access.')

# Get the authorization verifier code from the callback URL
redirect_response = input('Paste the full redirect URL here: ')

# Fetch the access token
token = oauth.fetch_token(token_url, authorization_response=redirect_response, client_secret=client_secret)

# URL of the protected resource
protected_url = 'https://api.example.com/protected_resource'

# Fetch the resource and handle potential errors
resource_data = fetch_protected_resource(protected_url, oauth)

if resource_data:
    print(resource_data)
