from flask import Flask
from flask import render_template
import os
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    host = '0.0.0.0'
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 8000))
    app.run(host=host, port=port)