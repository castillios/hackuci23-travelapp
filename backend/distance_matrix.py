# distance_matrix.py

import requests
import json

# input distance in miles and an interest;
# will output json file with results from Google's find place API
def by_interest_and_dist(distance: int, interest: str):
    #url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key=AIzaSyA58JmLlKl8ILlsOtsgKlAO6hYrUCgRDl0"
    api_key = "AIzaSyA58JmLlKl8ILlsOtsgKlAO6hYrUCgRDl0"
    dist_meters = miles_to_meters(distance)
    
    # https://towardsdatascience.com/how-to-use-the-google-places-api-for-location-analysis-and-more-17e48f8f25b1
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={interest}+irvine+ca&radius={dist_meters}&region=us&type=restaurant,gym,university,tourist_attraction,store,shopping_mall,park,museum&key={api_key}"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    #print(json.dumps(response.json(), indent = 4))
    return response.json()

# get the time and distance in miles between two locations
def get_distance(addrFrom: str, addrTo: str):
    api_key = "AIzaSyA58JmLlKl8ILlsOtsgKlAO6hYrUCgRDl0"
    formatted_from = addrFrom.replace(' ', '+')
    formatted_to = addrTo.replace(' ', '+')
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    full_url = f"{base_url}origins={formatted_from}&destinations={formatted_to}&key={api_key}"
    response = requests.request("GET", full_url)
    return response.json()


# input number of miles and will output in kilometers to the nearest integer
def miles_to_meters(miles: int):
    meters_in_mile = 1609.34

    return int(miles*meters_in_mile)

#by_interest_and_dist(1609, 'restaurants')

# extract values of an attribute from json file
def extract_attr(attr: str, distance: int, interest: str):
    attr_list = []
    file = by_interest_and_dist(distance, interest)

    for i in range(len(file)):
        attr_list.append(file["results"][i][attr])

    return attr_list

#print(extract_attr("formatted_address", 3000, "restaurants"))
print(get_distance('Costco Wholesale, 2700 Park Ave, Tustin, CA 92782', '30305 Arroyo Dr, Irvine, CA 92617'))
