from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from distance_matrix import extract_distances, uci_to_location
from yelp_data import perform_search, extract_yelp_data
from scheduler import create_itinerary

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, supports_credentials=True)

@app.route('/')
@cross_origin(supports_credentials=True)
def get_itinerary():

    num_activities = int(request.args.get('numActivites'))
    #print(type(num_activities))
    eat = request.args.get('food') # boolean

    activities = request.args.get('Sights') # delimited string with slashes
    try:
        activities = activities.split('/')
    except:
        print('activities is nonetype')

    # 40,000 meters is the max
    radius = float(request.args.get('Miles'))

    if eat == 'true' or eat == 'True':
        food = request.args.get('Preference')
        activities.append(f"{food} food")

    yelp_dict = extract_yelp_data(activities, radius)
    #print('got through yelp')
    distances = extract_distances(yelp_dict)
    distances_from_uci = uci_to_location(yelp_dict)
    itinerary = create_itinerary(distances, distances_from_uci, num_activities)
    return jsonify(itinerary)


