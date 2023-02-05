from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from distance_matrix import get_distance
from yelp_data import perform_search, extract_yelp_data

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, supports_credentials=True)

@app.route('/')
@cross_origin(supports_credentials=True)
def get_itinerary():

    num_hours = request.args.get('Hours')
    num_activities = request.args.get('numActivities')
    eat = request.args.get('food') # boolean

    activities = request.args.get('Sights') # delimited string with slashes
    activities = activities.split('/')

    radius = request.args.get('Miles')

    if eat == True:
        food = request.args.get('Preference')
        activities.extend(food)

    yelp_dict = extract_yelp_data(activities, radius)

    return "temporary return"


'''
@app.route('/byaddr')
def places_by_dist():
    return jsonify(get_distance('Costco Wholesale, 2700 Park Ave, Tustin, CA 92782', '30305 Arroyo Dr, Irvine, CA 92617'))

@app.route('/yelp')
def yelp_locations():
    return jsonify(parse_data(perform_search({'sightsee' : 'hiking', 'dine': 'dim sum', 'shop' : 'plant nursey'})))
    # return jsonify(get_place(keyword="dine beach"))


# 'hello/mueseum/beach/hike'

'''
