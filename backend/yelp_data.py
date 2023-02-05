# yelp_data.py
import requests
import json
from distance_matrix import miles_to_meters

# Returns JSON data
# dictionary with keys ['businesses', 'total', 'region (containing center)']
def get_place(keyword="", radius=10000):
    url = "https://api.yelp.com/v3/businesses/search"
    querystring = {"location":"University of California, Irvine","term":keyword, "radius":radius}

    payload = ""
    headers = {"Authorization": "Bearer p50ITgphUvksSaf_a2ENswHKJscwJhR5ps0p00g7nfU8SBeBupjw6bfhaIoyLXygUzlKoN6XFxTvU4JTObchhULslD1PKiSLUf4TcYvhA5uhgI5c9c2Q4ICDsw_eY3Yx"}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()

# Returns formatted string of JSON data
def format_data(json_data) -> str:
    json_formatted_str = json.dumps(json_data, indent=4)
    return json_formatted_str

"""
Performs searches on Yelp and returns a dictionary containing
JSON data under each category (key)

key : value --> category : JSON data
"""
def perform_search(query_list, radius) -> dict:
    loc_dict = dict() 
    for loc_type in query_list:
        loc_json = get_place(loc_type, radius)
        loc_dict[loc_type] = loc_json
    return loc_dict


"""
parse_data returns a dictionary containing keys for categories (business types)
loc_interests is a dictionary
List of categories:
    - Sightseeing (sightsee)
    - Dining (dine)
    - Shopping (shop)

Outer Dictionary key : values -> category : [business_dict, business_dict2, ...]
Inner Dictionary key : values -> JSON label : data
Data List, JSON label = "businesses" --> list contains a dictionaries containing
data for each business


Each category is a list of dictionaries. Each category list contains a different
business (also a dictionary).

Each business contains the following attributes:
    - Name
    - Yelp ID (for reference)
    - Rating (threshold?)
    - Image
    - IsClosed
    - Price (if applicable)
    - Location
    - Coordinates
    - etc...

This is NOT the final itinerary, but rather a function to sort the data in order
to easily create the itinerary later on.

"""
def parse_data(loc_interests) -> dict:
    sorted_loc_dict = dict()
    print(loc_interests)
    for cat, business_data in loc_interests.items():
        sorted_loc_dict[cat] = []
        for b in business_data['businesses']:
            b_dict = dict()
            b_dict['name'] = b['name']
            b_dict['location'] = parse_location_str(b['location'])
            b_dict['img'] = b['image_url']
            b_dict['rating'] =  b['rating']
            b_dict['is_closed'] = b['is_closed']
            if 'price' in b.keys():
                b_dict['price'] = b['price']
            b_dict['coords'] = b['coordinates']

            sorted_loc_dict[cat].append(b_dict)
    return sorted_loc_dict


def parse_location_str(loc_dict) -> str:
    loc_str = ""
    for i, data in enumerate(loc_dict['display_address']):
        loc_str += f"{data} "
    return loc_str
"""
Isolates name, addresses, and yelp id
Filters data to be sent to distance_matrix.py
Yelp ID is saved that way we can filt
"""

def print_locs(locs) -> None:
    for loc_type, loc_dict in locs.items():
        print(loc_type)
        for location in loc_dict:
            for loc, loc_data in location.items():
                print(f"{loc}: {loc_data}")
            print('\n' * 2)

# Returns json data of search queries off of yelp using user input
# Our parameter user_in would be a list of str inputs received from the user which we iterate through
def extract_yelp_data(user_in, radius):
    radius_meters = miles_to_meters(radius)
    search_results = perform_search(user_in, radius_meters)
    # parse data receives a dictionary --> keyword:results
    json_data = parse_data(search_results)

    # can comment this out -- print is for testing
    #print(format_data(json_data))
    return json_data


# this function is for testing, can comment out
def test_yelp_data(user_in, radius):
    # User input is temporary, categories will be hard coded later
    # Simply for testing (TEMPORARY)
    radius_meters = miles_to_meters(radius)
    search_results = perform_search(user_in, radius_meters)
    # parse data receives a dictionary --> keyword:results
    json_data = parse_data(search_results)

    # TEMPORARY FOR DEBUGGING
    # Print to console
    formatted_json = format_data(json_data)
    print(formatted_json)
    print('\n' * 10)
    print_locs(json_data)

    return json_data

        

if __name__ == "__main__":
    extract_yelp_data("dim sum", 10)
