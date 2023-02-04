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
sort_data returns a dictionary containing keys for categories (business types)
List of categories:
    - Sightseeing (sightsee)
    - Dining (dine)
    - Shopping (shop)


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
def parse_data(json_data, business_type) -> dict:
    b_data = json_data['businesses']
    loc_dict = {
        'sightsee' : [],
        'dine' : [],
        'shop' : []
    }
    
    for b in b_data:
        b_dict = dict()
        b_dict['name'] = b['name']
        b_dict['rating'] =  b['rating']
        b_dict['img'] = b['image_url']
        b_dict['is_closed'] = b['is_closed']
        if 'price' in b.keys():
            b_dict['price'] = b['price']
        b_dict['loc'] = b['location']
        b_dict['coords'] = b['coordinates']

        loc_dict[business_type].append(b_dict)
    
    return loc_dict
    
def print_locs(locs) -> None:
    for loc_type, loc_dict in locs.items():
        print(loc_type)
        for location in loc_dict:
            for loc, loc_data in location.items():
                print(f"{loc}: {loc_data}")
            print('\n' * 2)

        


def temp_main():
    # User input is temporary, categories will be hard coded later
    # Simply for testing
    user_in = input("Enter a search query: ")

    yelp_json = get_place(user_in)
    location_dict = parse_data(yelp_json, user_in)
    print(format_data(yelp_json))
    print('\n' * 10)
    print_locs(location_dict)

        

if __name__ == "__main__":
    temp_main()
