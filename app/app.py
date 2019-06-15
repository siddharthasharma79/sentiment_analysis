import logging
import os

from flask import Flask
from flask import render_template
from flask import request

from modules.sentiment import Sentiment

logger = logging.getLogger('Preprocess Analysis')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def prediction():
    text = request.form['sentiment']
    response = Sentiment().check_sentiment(text)
    return render_template('index.html', message=response)


if __name__ == "__main__":
    logger.info('starting flask server...')
    host = '0.0.0.0'
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 8000))
    app.run(host=host, port=port)
