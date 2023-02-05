from distance_matrix import extract_distances
from yelp_data import extract_yelp_data
import random

def create_itinerary(activities_dict, dist_from_uci, num_activities):

    chosen_activities = dict()

    rand_first_choice = random.choice(activities_dict.keys()) 
    chosen_activities['choice 1'] = rand_first_choice

    # get travel time from uci to first choice
    travel_time = dist_from_uci[rand_first_choice]['time_from_uci']
    travel_dist = dist_from_uci[rand_first_choice]['dist_from_uci']

    # get other activities randomly from the values in the previous activity
    num_chosen = 1
    prev_choice = rand_first_choice

    while num_chosen != num_activities:

        # get random index out of list from previous choice
        while True:
            cur_choice = random.randint(0, len(activities_dict[prev_choice]))

            # if random choice has not already been chosen continue and add to return dictionary
            if activities_dict[prev_choice][cur_choice]['name2'] not in chosen_activities.keys():
                break

        # path to dictionary for next activity choice
        path = activities_dict[prev_choice][cur_choice]
        travel_time += path['time']
        travel_dist += path['dist']

        chosen_activities[f"choice {num_chosen + 1}"] = path['name2']

        num_chosen += 1
        prev_choice = cur_choice

    chosen_activities['total time'] = travel_time
    chosen_activities['total distance'] = travel_dist

    print(chosen_activities)
    return chosen_activities

     




        


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

    

