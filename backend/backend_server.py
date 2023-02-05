from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from distance_matrix import by_interest_and_dist, get_distance
from yelp_data import perform_search, parse_data

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, supports_credentials=True)

@app.route('/')
@cross_origin(supports_credentials=True)
def get_itinerary():
    num_hours = request.args.get('Hours')
    num_activities = request.args.get('numActivities')
    eat = request.args.get('food') # boolean
    activities = request.args.get('Sights')
    radius = request.args.get('Miles')

    return jsonify(by_interest_and_dist(3000, 'restaurants'))
    #names = extract_attr("name", 3000, 'restaurants')
    #return f"<p>{names}</p>"


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
