import requests
import json

# Returns JSON data
def get_place(keyword=""):
    url = "https://api.yelp.com/v3/businesses/search"

    querystring = {"location":"irvine","term":"korean"}

    payload = ""
    headers = {"Authorization": "Bearer p50ITgphUvksSaf_a2ENswHKJscwJhR5ps0p00g7nfU8SBeBupjw6bfhaIoyLXygUzlKoN6XFxTvU4JTObchhULslD1PKiSLUf4TcYvhA5uhgI5c9c2Q4ICDsw_eY3Yx"}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    #print(response.text)
    return response.json()

# Returns formatted string of JSON data
def format_data(json_data):
    json_formatted_str = json.dumps(json_data, indent=4)
    return json_formatted_str

places_str = format_data(get_place())