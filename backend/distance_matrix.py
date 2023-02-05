# distance_matrix.py
# using Google's distance matrix API

import requests
import random
from api import google_api_key

# get the time and distance in miles between two locations
def get_distance(addrFrom: str, addrTo: str):
    api_key = google_api_key
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
    meters_in_mile = 1609
    meters = miles * meters_in_mile
    return int(meters)

def meters_to_miles(meters: int):
    miles_in_a_meter = 0.000621371
    miles = float(meters) * float(miles_in_a_meter)
    return int(miles)

def km_to_miles(km: int):
    km_in_a_mile = 0.621371
    miles = km_in_a_mile*km
    return int(miles)

# gives distance as a string with a unit attached
def convert_to_miles(distance_w_unit: str):
    unit = distance_w_unit.split()[-1]
    if unit == 'km':
        distance = float(distance_w_unit[:-3])
        dist_between = km_to_miles(distance)
    elif unit == 'm':
        distance = float(distance_w_unit[:-2])
        dist_between = distance

    return dist_between


#print(extract_attr("formatted_address", 3000, "restaurants"))
#print(get_distance('Costco Wholesale, 2700 Park Ave, Tustin, CA 92782', '30305 Arroyo Dr, Irvine, CA 92617'))
#dist_file = get_distance('Costco Wholesale, 2700 Park Ave, Tustin, CA 92782', '30305 Arroyo Dr, Irvine, CA 92617')

# input: yelp_dict = {name: {price : price, addr : addr}}
# output: dist_dict = {name1: [{name2 : other establishment name, addr1: addr1, addr2: addr2, 
    # dist : distance, time : time to get to name2 from name1}]}


def extract_distances(yelp_dict):

    dist_dict = dict()
    skip = random.randint(2, 10)

    for interest in yelp_dict.keys():
        for place1 in yelp_dict[interest]:
            for place2 in yelp_dict[interest]:
                
                if skip < 5:
                    if 'name' in place1.keys() and 'name' in place2.keys():
                        if place1['name'] != place2['name']:
                            addr1 = place1['location']
                            addr2 = place2['location']

                            distance_file = get_distance(addr1, addr2)

                            if 'distance' in distance_file['rows'][0]['elements'][0].keys():
                                distance = distance_file['rows'][0]['elements'][0]['distance']['text'].replace(',', '')
                                dist_between = convert_to_miles(distance)

                                #dist_between = meters_to_miles(float(distance))
                                time_between = distance_file['rows'][0]['elements'][0]['duration']['text'][:-5]

                                if place1['name'] not in dist_dict.keys():
                                    dist_dict[place1['name']] = [{'place2': place2['name'], 'addr1': addr1, 'addr2': addr2,
                                    'dist': dist_between, 'time': time_between}]
                                else:
                                    dist_dict[place1['name']].append({'place2': place2['name'], 'addr1': addr1, 'addr2': addr2,
                                    'dist': dist_between, 'time': time_between})

                skip = random.randint(2, 10)

    return dist_dict

# output: {name: {'address': place['location'], 'dist_from_uci': dist_between, 'time_from_uci': time_between}}
def uci_to_location(yelp_dict):

    uci_dist_dict = dict()
    uci_addr = "204 Aldrich Hall, Irvine, CA 92697"
    for interest in yelp_dict.keys():
        for place in yelp_dict[interest]:

            distance = get_distance(uci_addr, place['location'])

            if 'distance' in distance['rows'][0]['elements'][0].keys():
                dist_between = convert_to_miles(distance['rows'][0]['elements'][0]['distance']['text'].replace(',', ''))

                time_between = distance['rows'][0]['elements'][0]['duration']['text'][:-5]

                uci_dist_dict[place['name']] = {'address': place['location'], 'dist_from_uci': dist_between, 'time_from_uci': time_between}

    return uci_dist_dict




    
               
'''
# check keys for get_distance json
dist_file = get_distance('Costco Wholesale, 2700 Park Ave, Tustin, CA 92782', '30305 Arroyo Dr, Irvine, CA 92617')
print(dist_file.keys())
print(dist_file['rows'][0].keys())
print(dist_file['rows'][0]['elements'][0])
print(dist_file['rows'][0]['elements'][0]['distance']['text'][:-3]) # get distance in km
print(dist_file['rows'][0]['elements'][0]['duration']['text'][:-5]) # get trip time in minutes
'''




