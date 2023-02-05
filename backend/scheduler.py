
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

class Itinerary:
    def __init__(radius, interest):
        pass

    

