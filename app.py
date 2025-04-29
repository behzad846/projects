from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Events/Peyrang/Brochure')
def index():
    return render_template('index.html')