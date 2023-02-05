# distance_matrix.py
# using Google's distance matrix API

import requests
import json

# get the time and distance in miles between two locations
def get_distance(addrFrom: str, addrTo: str):
    api_key = "AIzaSyA58JmLlKl8ILlsOtsgKlAO6hYrUCgRDl0"
    formatted_from = addrFrom.replace(' ', '+')
    formatted_to = addrTo.replace(' ', '+')

    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    full_url = f"{base_url}origins={formatted_from}&destinations={formatted_to}&key={api_key}"

    payload={}
    headers = {}

    response = requests.request("GET", full_url, headers=headers, data=payload)
    return response.json()


# input number of miles and will output in kilometers to the nearest integer
def miles_to_meters(miles: int):
    meters_in_mile = 1609.34

    return int(miles*meters_in_mile)


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




