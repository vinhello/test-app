from flask import Flask, render_template
import requests
import json
import os


app = Flask(__name__)


def get_meme():
    #Uncomment these two lines and comment out the other url line if you want SFW memes
    # sr = "/wholesomememes"
    # url = "https://meme-api.com/gimme" + sr
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request ("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route('/')
def index():
    meme_large, subreddit = get_meme()
    return render_template('index.html', meme_pic=meme_large, subreddit=subreddit) 


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)