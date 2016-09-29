from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    ninja = 'tmnt'
    return render_template('ninja.html', ninja=ninja)

@app.route('/ninja/<color>')
def color(color):
    if color == 'blue':
        ninja = 'leonardo'
    elif color == 'red':
        ninja = 'raphael'
    elif color == 'orange':
        ninja = 'michelangelo'
    elif color == 'purple':
        ninja = 'donatello'
    else:
        ninja = 'notapril'

    return render_template('ninja.html', ninja=ninja)

app.run(debug=True)
