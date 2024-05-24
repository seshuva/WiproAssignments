import requests
from requests_oauthlib import OAuth2Session

# Replace these values with your application's credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
authorization_base_url = 'https://example.com/oauth/authorize'
token_url = 'https://example.com/oauth/token'

# Redirect URI for your application (it must match the one set in your OAuth provider)
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

# Example of accessing a protected resource
protected_url = 'https://api.example.com/protected_resource'
response = oauth.get(protected_url)

print(response.json())
