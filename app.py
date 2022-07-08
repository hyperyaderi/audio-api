import json
import requests

from flask import Flask, request, send_file

app = Flask(__name__)

musicpath = '/home/icecast/music'

@app.route('/get_track', methods=['GET'])
def get_track():
    track = request.args['track']
    return send_file(f'{musicpath}/{track}.mp3')


@app.route('/get_nowplaying_track', methods=['GET'])
def get_nowplaying_track():
    url = 'https://radio.hyperyaderi.ru/status-json.xsl'
    resp = requests.get(url).text
    data = json.loads(resp)
    nowplaying = data['icestats']['source']['title']
    return send_file(f'{musicpath}/{nowplaying}.mp3')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=1488)
