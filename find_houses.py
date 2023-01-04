import requests

# Replace YOUR_API_KEY with your actual API key
api_key = 'YOUR_API_KEY'

# Set the origin and destination locations
origin = 'beach'
destination = 'house'

# Set the mode of transportation to walking
mode = 'walking'

# Set the maximum distance that you are willing to walk
max_distance = '5000'  # 5 km

# Set the unit system to metric
units = 'metric'

# Set the language of the response
language = 'en'

# Set the parameters for the API request
params = {
    'key': api_key,
    'origins': origin,
    'destinations': destination,
    'mode': mode,
    'units': units,
    'language': language,
}

# Send the request to the Distance Matrix API
response = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=params)

# Check the status code of the response
if response.status_code == 200:
    # The request was successful
    data = response.json()
    if data['status'] == 'OK':
        # The Distance Matrix API returned a valid response
        distance = data['rows'][0]['elements'][0]['distance']['value']  # distance in meters
        duration = data['rows'][0]['elements'][0]['duration']['value']  # duration in seconds
        if distance <= max_distance:
            # The house is within walking distance from the beach
            print(f'The house is {distance / 1000:.2f} km away and it will take {duration / 60:.2f} minutes to walk.')
        else:
            # The house is not within walking distance from the beach
            print(f'The house is too far away. It is {distance / 1000:.2f} km from the beach and it will take {duration / 60:.2f} minutes to walk.')
    else:
        # The Distance Matrix API returned an error
        print(f'Error: {data["status"]} - {data["error_message"]}')
else:
    # The request to the Distance Matrix API failed
    print(f'Error: {response.status_code}')
