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

'''
# extract values of an attribute from json file
def extract_attr(attr: str, distance: int, interest: str):
    attr_list = []
    file = by_interest_and_dist(distance, interest)

    for i in range(len(file)):
        attr_list.append(file["results"][i][attr])

    return attr_list
'''

#print(extract_attr("formatted_address", 3000, "restaurants"))
#print(get_distance('Costco Wholesale, 2700 Park Ave, Tustin, CA 92782', '30305 Arroyo Dr, Irvine, CA 92617'))
#dist_file = get_distance('Costco Wholesale, 2700 Park Ave, Tustin, CA 92782', '30305 Arroyo Dr, Irvine, CA 92617')

# input: yelp_dict = {name: {price : price, addr : addr}}
# output: dist_dict = {name1: [{name2 : other establishment name, addr1: addr1, addr2: addr2, 
    # dist : distance, time : time to get to name2 from name1}]}


def extract_distances(yelp_dict, origin):

    dist_dict = dict()

    for estab1 in yelp_dict.keys():
        for estab2 in yelp_dict.keys():
            
            # if establishment 1 and 2 are not the same and the second establishment
            # isn't already in the dictionary (don't want symmetric duplicates)
            if estab1 != estab2 and estab2 not in dist_dict.keys():

                addr1 = yelp_dict[estab1]['location']
                addr2 = yelp_dict[estab2]['location']
                distance_file = get_distance(addr1, addr2)
                dist_between = distance_file['rows'][0]['elements'][0]['distance']['text'][:-3]
                time_between = distance_file['rows'][0]['elements'][0]['duration']['text'][:-5]

                if estab1 not in dist_dict.keys():

                    dist_dict[estab1] = [{'estab2': estab2, 'addr1': addr1, 'addr2': addr2,
                        'dist': dist_between, 'time': time_between}]

                else:
                    dist_dict[estab1].append({'estab2': estab2, 'addr1': addr1, 'addr2': addr2,
                        'dist': dist_between, 'time': time_between})

    return dist_dict


    
               
'''
# check keys for get_distance json
dist_file = get_distance('Costco Wholesale, 2700 Park Ave, Tustin, CA 92782', '30305 Arroyo Dr, Irvine, CA 92617')
print(dist_file.keys())
print(dist_file['rows'][0].keys())
print(dist_file['rows'][0]['elements'][0])
print(dist_file['rows'][0]['elements'][0]['distance']['text'][:-3]) # get distance in km
print(dist_file['rows'][0]['elements'][0]['duration']['text'][:-5]) # get trip time in minutes
'''




