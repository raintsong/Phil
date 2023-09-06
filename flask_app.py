from flask import Flask, render_template,url_for
import js2py


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


#incomplete
@app.route('/editor')
def editor():
    return render_template('index.html')


@app.route('/puzzler')
def puzzler():
    cross = js2py.run_file(url_for('static', filename='cross.js'))
    cross.toggleEditor()
    return render_template('index.html')
