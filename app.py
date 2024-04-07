from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder="templates", static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fixtures', methods=['GET'])
def fixtures():
    golf_fixtures = get_golf_fixtures()
    print(golf_fixtures)
    return render_template('fixtures.html', golf_fixtures=golf_fixtures)

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    golf_leaderboard = get_golf_leaderboard()
    golf_leaderboard['results']['leaderboard'] = sorted(golf_leaderboard['results']['leaderboard'], key=lambda x: x['strokes'], reverse=True)

    for index, player in enumerate(golf_leaderboard['results']['leaderboard'], start=1):
        player['rank'] = index

    print(golf_leaderboard)
    return render_template('leaderboard.html', golf_leaderboard=golf_leaderboard)

def get_golf_fixtures():
    url = "https://golf-leaderboard-data.p.rapidapi.com/fixtures/2/2021"
    headers = {
        'x-rapidapi-host': "golf-leaderboard-data.p.rapidapi.com",
        'x-rapidapi-key': "707255cfcfmsh4f9f30d55347d3ep120e5ejsna77f04301e06"
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

def get_golf_leaderboard():
    url = "https://golf-leaderboard-data.p.rapidapi.com/leaderboard/25"
    headers = {
        'x-rapidapi-host': "golf-leaderboard-data.p.rapidapi.com",
        'x-rapidapi-key': "707255cfcfmsh4f9f30d55347d3ep120e5ejsna77f04301e06"
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
