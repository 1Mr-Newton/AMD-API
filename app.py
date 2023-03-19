from flask import Flask, jsonify, request
from yt_dlp import YoutubeDL

app = Flask(__name__)


def get_data(url):
    ydl = YoutubeDL()
    info = ydl.extract_info(url, download=False)
    return info


@app.route('/', methods=['POST'])
def get_url():
    try:
        url = request.get_json().get('url')
        return jsonify(
            get_data(url)

        )
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
