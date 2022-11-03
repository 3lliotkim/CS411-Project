import requests

class Audio_sky_backend:

    #Spotify API Call
    response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")

    CLIENT_ID = 'c9674e43370b4e75ab0ee20826fc6279'
    CLIENT_SECRET = 'dae30c00aa8a4af489511e2bda4cff83'

    AUTH_URL = 'https://accounts.spotify.com/api/token'


    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']