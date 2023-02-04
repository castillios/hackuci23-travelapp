import requests
import json

# Returns JSON data
# dictionary with keys ['businesses', 'total', 'region (containing center)']
def get_place(keyword=""):
    url = "https://api.yelp.com/v3/businesses/search"

    querystring = {"location":"irvine","term":keyword}

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
def perform_search(query_dict) -> dict:
    loc_dict = dict() 

    for category in query_dict.keys():
        loc_dict[category] = None
    
    for cat, query in query_dict.items():
        string_query = f"{cat} {query}" # i.e. "sightsee beaches" or "dine korean"
        loc_json = get_place(string_query)
        loc_dict[cat] = loc_json

    return loc_dict


"""
parse_data returns a dictionary containing keys for categories (business types)
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
    - Image
    - Rating (threshold?)
    - etc...

This is NOT the final itinerary, but rather a function to sort the data in order
to easily create the itinerary later on.

"""
def parse_data(loc_interests) -> dict:
    sorted_loc_dict = dict()
    for cat, business_data in loc_interests.items():
        sorted_loc_dict[cat] = []
        for b in business_data['businesses']:
            b_dict = dict()
            b_dict['name'] = b['name']
            b_dict['rating'] =  b['rating']
            b_dict['img'] = b['image_url']
            b_dict['is_closed'] = b['is_closed']
            if 'price' in b.keys():
                b_dict['price'] = b['price']
            b_dict['loc'] = b['location']
            b_dict['coords'] = b['coordinates']

            sorted_loc_dict[cat].append(b_dict)
    return sorted_loc_dict
    
def print_locs(locs) -> None:
    for loc_type, loc_dict in locs.items():
        print(loc_type)
        for location in loc_dict:
            for loc, loc_data in location.items():
                print(f"{loc}: {loc_data}")
            print('\n' * 2)

def extract_yelp_data():
    # User input is temporary, categories will be hard coded later
    # Simply for testing (TEMPORARY)
    sight_query = input("Enter a search query for sightseeing: ")
    dine_query = input("Enter a search query for dining: ")
    shop_query = input("Enter a search query for shops: ")

    # User will be able to specify categories but for now they are all hard coded
    # Each category has a search query attached to it.
    cats = {'sightsee' : sight_query, 'dine': dine_query, 'shop' : shop_query}
    search_results = perform_search(cats)
    json_data = parse_data(search_results)

    # TEMPORARY FOR DEBUGGING
    formatted_json = format_data(json_data)
    print(formatted_json)
    print('\n' * 10)
    print_locs(json_data)

    return json_data

        

if __name__ == "__main__":
    extract_yelp_data()
