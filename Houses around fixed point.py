import requests

# Replace YOUR_API_KEY with your actual API key
api_key = 'YOUR_API_KEY'

# Set the location of the fixed point
location = 'latitude,longitude'

# Set the radius around the fixed point to search
radius = 5000  # 5 km

# Set the type of place to search for
place_type = 'house'

# Set the parameters for the API request
params = {
    'key': api_key,
    'location': location,
    'radius': radius,
    'type': place_type,
}

# Send the request to the Place Search API
response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=params)

# Check the status code of the response
if response.status_code == 200:
    # The request was successful
    data = response.json()
    if data['status'] == 'OK':
        # The Place Search API returned a valid response
        houses = data['results']
        print(f'Found {len(houses)} houses within {radius / 1000} km of the fixed point.')
        for house in houses:
            print(house['name'])
    else:
        # The Place Search API returned an error
        print(f'Error: {data["status"]} - {data["error_message"]}')
else:
    # The request to the Place Search API failed
    print(f'Error: {response.status_code}')
