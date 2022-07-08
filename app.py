import os

from flask import Flask, request, send_file

app = Flask(__name__)

musicpath = '/home/icecast/music'

@app.route('/getTrack', methods=['GET'])
def hello():
    track = request.args['track']
    return send_file(f'{musicpath}/{track}.mp3')

    
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=1337)
