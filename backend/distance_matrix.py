# distance_matrix.py

import requests
import json

# input distance in miles and an interest;
# will output json file with results from Google's find place API
def by_interest_and_dist(distance: int, interest: str):
    #url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key=AIzaSyA58JmLlKl8ILlsOtsgKlAO6hYrUCgRDl0"
    
    dist_meters = miles_to_meters(distance)
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={interest}&inputtype=textquery&locationbias=circle%3A{dist_meters}%4047.6918452%2C-122.2226413&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=AIzaSyA58JmLlKl8ILlsOtsgKlAO6hYrUCgRDl0"
    payload={}
    headers = {}
    #querystring = {"distance":}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(json.dumps(response.json(), indent = 4))
    return response.json()

# input number of miles and will output in kilometers to the nearest integer
def miles_to_meters(miles: int):
    meters_in_mile = 1609.34

    return int(miles*meters_in_mile)


by_interest_and_dist(1609, 'restaurants')