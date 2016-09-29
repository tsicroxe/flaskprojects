from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "mySuperSecretPassword"

#Renders our counter html page. Counter will default to 1
@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html', count=session['count'])

#Routes the Ninja +2 button and adds an counter (index will already add one)
@app.route('/addTwo', methods=["POST"])
def addTwo():
    session['count'] += 1
    return redirect('/')

#Routes the count through the reset function and resets it back to 0
@app.route('/reset', methods=["POST"])
def reset():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
