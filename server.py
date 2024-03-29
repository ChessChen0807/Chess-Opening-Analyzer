from flask import Flask, jsonify

from gpt import get_opening_advice
from opening_name_analyzer import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "chess server"

@app.route('/get_opening_advice/<opening_name>')
def return_openingadvice(opening_name):
    advice = get_opening_advice(opening_name)
    return advice

#route to get opening name
@app.route('/get_opening_name')
def fetch_opening_name():
    result = get_opening_name()
    return jsonify(result)

#route for get_top_n_opening_name(n)
@app.route('/top_n_opening_name/<int:number>')
def fetch_top_opening(number):
    val = get_top_n_opening_name(int(number))
    result = val.set_index('opening_name').T.to_dict('dict')
    return jsonify(result)

# route for get victory status
@app.route('/get_victory_status')
def fetch_victory_status():
    victory = get_victory_status()
    result = victory.set_index('opening_name').T.to_dict('dict')
    return jsonify(result)

# route for get victory_status_by_opening_name
@app.route('/victory_status_by_opening_name/<opening_name>')
def fetch_victory_status_by_opening_name(opening_name):
    victory_status_by_opening_name = get_victory_status_by_opening_name(opening_name)
    data = victory_status_by_opening_name.values.tolist()
    result = {'statistics': data}
    suggestion = get_opening_advice(opening_name)
    result['suggestion'] = suggestion
    return jsonify(result)

# route to fetch the winner statistics
@app.route('/winners')
def fetch_winners():
    winner = get_winner()
    return jsonify(winner)

# route to fetch winner statistics by opening name
@app.route('/winners_by_opening_name/<opening_name>')
def fetch_winner_by_opening_name(opening_name):
    winners_by_opening_name = get_winner_by_opening_name(opening_name)
    result = {'statistics': winners_by_opening_name}
    suggestion = get_opening_advice(opening_name)
    result['suggestion'] = suggestion
    return jsonify(result)

# route to fetch the min and max opening phase for a specific opening name
@app.route('/min_and_max_moves/<opening_name>')
def fetch_min_max_number_moves_in_the_opening_phase(opening_name):
    min_max_number_moves_in_the_opening_phase = get_min_max_number_moves_in_the_opening_phase(opening_name)
    data = min_max_number_moves_in_the_opening_phase.set_index('opening_name').values.tolist()
    result = {'statistics' : data}
    suggestion = get_opening_advice(opening_name)
    result['suggestion'] = suggestion
    return jsonify(result)

# route to fetch the min and max number of turns in a specific opening name
@app.route('/min_and_max_turns/<opening_name>')
def fetch_min_max_number_turns(opening_name):
    min_max_number_turns = get_min_max_number_turns(opening_name)
    data = min_max_number_turns.set_index('opening_name').values.tolist()
    result = {'statistics' : data}
    suggestion = get_opening_advice(opening_name)
    result['suggestion'] = suggestion
    return jsonify(result)

#main will start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)