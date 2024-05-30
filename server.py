from flask import Flask, jsonify

from gpt import get_opening_advice
from opening_name_analyzer import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "chess server"


trending_header_items = {
    "image_url": "https://image.com/image",
    "title": "Welcome to Chess Opening Analyzer!",
    "description": "Where the Openings come hot and fresh!"
}

posts = [{
    "title":
    "Check out what Magnus Carlson did this weekend! (epic Chess tournament)",
    "description":
    "He's really cool.",
    "image_url":
    "https://images.daznservices.com/di/library/sporting_news/61/ca/magnus-carlsen-050320-getty-ftr_sx3g4xdqgtda1c6lb0o9mzpcc.jpg?t=-549273311&w=%7Bwidth%7D&quality=80",
    "article_url":
    "https://www.sportingnews.com/ca/other-sports/news/magnus-carlsen-finds-the-champion-toughness-that-could-prolong-his-peak-define-his-30s/11sq6u560ex3310x0y0ehw85oo"
}, {
    "title": "News on the latest Chess Championship candidate tournaments",
    "description": "",
    "image_url":
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FChessboard&psig=AOvVaw2AqyMvoABC_IL5HtDTloLm&ust=1717024523387000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCND-lvm8sYYDFQAAAAAdAAAAABAE",
    "article_url": "https://new.uschess.org/upcoming-tournaments",
}]

@app.route('/get_trending_header_items')
def get_trending_header_items():
  return jsonify(trending_header_items)

@app.route('/get_posts')
def get_posts():
  return jsonify(posts)
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
