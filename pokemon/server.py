from flask import Flask, render_template, redirect, request

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')


@application.route('/<id>')
def pokemon(id):
    pokemon = ''
    for i in range(1, 152):
        if id == str(i):
            pokemon = id
            break
    else:
        pokemon = 'pokewho'
    print pokemon
    return render_template('pokemon.html', pokemon=pokemon)

application.run(debug=True)
