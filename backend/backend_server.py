from flask import Flask, jsonify
from flask_cors import CORS
from distance_matrix import by_interest_and_dist

app = Flask(__name__)
CORS(app)

@app.route('/')
def places_by_interest_and_dist():

    return jsonify(by_interest_and_dist(3000, 'restaurants'))
