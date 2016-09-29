from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create():
    print request.form
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('result.html', user=name, location=location, language=language, comment=comment)

app.run(debug=True)
