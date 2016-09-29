from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello World!"

@app.route('/Hello')

def hello_again():
    return render_template('index.html')



app.run(debug=True)
