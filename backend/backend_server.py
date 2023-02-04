from flask import Flask, jsonify
from flask_cors import CORS
from distance_matrix import by_interest_and_dist, get_distance
from yelp_data import extract_yelp_data

app = Flask(__name__)
CORS(app)

@app.route('/')
def places_by_interest_and_dist():

    return jsonify(by_interest_and_dist(3000, 'restaurants'))
    #names = extract_attr("name", 3000, 'restaurants')
    #return f"<p>{names}</p>"

@app.route('/byaddr')
def places_by_dist():
    return jsonify(get_distance('Costco Wholesale, 2700 Park Ave, Tustin, CA 92782', '30305 Arroyo Dr, Irvine, CA 92617'))

@app.route('/yelp')
def yelp_locations():
    return jsonify(extract_yelp_data())