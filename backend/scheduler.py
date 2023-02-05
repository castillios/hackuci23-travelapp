from distance_matrix import extract_distances
from yelp_data import extract_yelp_data

"""
Scheduler plans based on:
    - User inputting how many activities they want to do (we create the length of the trip)
    - Filter out by radius
    - What they want to do (sightsee/dine/shop)
        - Filter out what they want
        - *ask frontend* Specifics of each category (what do they want to see/eat/shop? user input)
    - Return locations
        - A dictionary where keys categories, values are list of businesses
        - Each business is a dictionary
    - Create itinerary from returned locations
        - Itinerary is a dictionary (1, 2, 3, ... n) with n number of activities -- each one is in order
            - Values would be the business (contains the name, address, distance to travel to from prior activity)
            - *ask frontend* display business image, since we can send image url
    - Send itinerary to front end
"""
"""
Params include:
 - num_hours
 - num_activities
 - eat
 - activites: string with '/' as a delimiter
 - radius
"""
class Itinerary:
    # implement food later
    def __init__(self, radius, activities, num_hours):
        self.boundary = radius
        self.activities_lst = activities.split('/')
        self.length_day = num_hours

    # Creates activities
    # Returns list of dictionaries. Each dictionary is a list of activities
    # to select locations and businesses from. Each location has various
    # keys and values (names, ratings, pricing, distance, etc)
    # i.e.
    # [
    #   museum : [{museum 1}, {museum 2}]
    # ]
    def plan(self):
        self.plan_lst = []
        for a in self.activity:
            self.a_json = extract_yelp_data(a)



    # Creates a randomized itinerary 
    def generate_itinerary():
        pass

    

