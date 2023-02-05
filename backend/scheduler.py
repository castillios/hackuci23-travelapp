from yelp_data import extract_yelp_data
import random


# output: dictionary where n keys are the n activities
   # and additonal keys for total travel time and total trip distance
def create_itinerary(activities_dict, dist_from_uci, num_activities):


   chosen_activities = dict()


   rand_first_choice = random.choice(list(activities_dict.keys()))
   chosen_activities['Activity 1:'] = rand_first_choice


   # get travel time from uci to first choice
   travel_time = int(dist_from_uci[rand_first_choice]['time_from_uci'])
   travel_dist = dist_from_uci[rand_first_choice]['dist_from_uci']


   # get other activities randomly from the values in the previous activity
   num_chosen = 1
   prev_choice = rand_first_choice


   #print(num_activities)
   while num_chosen <= num_activities:


       # get random index out of list from previous choice
       while True:


           cur_choice = random.randint(0, len(activities_dict[prev_choice]) - 1)


           # if random choice has not already been chosen continue and add to return dictionary
           if activities_dict[prev_choice][cur_choice]['place2'] not in chosen_activities.keys():
               break


       # path to dictionary for next activity choice
       path = activities_dict[prev_choice][cur_choice]
       try:
           travel_time += int(path['time'])
       except:
           pass
       travel_dist += int(path['dist'])


       chosen_activities[f"Activity {num_chosen}:"] = path['place2']


       num_chosen += 1
       prev_choice = path['place2']


   try:
       chosen_activities['Total Time:'] = str(f"{travel_time} Minutes")
   except:
       pass
   chosen_activities['Total Distance:'] = str(f"{travel_dist} Miles")


   return chosen_activities
