from flask import Flask, session, render_template, redirect, request
import random

app = Flask(__name__)
app.secret_key = "asdf1234"

#Routes to index.html
@app.route('/')
def index():

    data = {}


    try:
        print 'session number is already set: ' + str(session['number'])
    except:
        session['number'] = random.randint(0,101)
        print "this got excepted and set"

    try:
        guess = int(session['guess'])
        if session['number'] > guess:
            data = {'event':'Your guess is too low'}
            data['color'] = 'red'
            print "Guess is too low"

        elif session['number'] < guess:
            data = {'event':'Your guess is too high'}
            data['color'] = 'red'
            print "guess is too high"

        elif session['number'] == guess:
            data = {'event':"You guessed right!"}
            data['color'] = 'green'
            data['again'] = 'Press reset to play again!'
            print "You guessed right!"

    except:
        print "couldn't get form"


    return render_template('index.html', data=data, reset=reset)

@app.route('/guess', methods=["POST"])
def guess():
    session['guess'] = request.form['guess']
    print 'Session number is ' + str(session['number'])
    print 'guess is ' + str(session['guess'])
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
