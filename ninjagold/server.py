from flask import Flask, render_template, redirect, session, request
import random, datetime

app = Flask(__name__)
app.secret_key = "ericsux"

#Begins initial route to index.html
@app.route('/')
def index():

    #Checks to see if session['gold'] exists and if it does not, creates it
    try:
        session['gold']
    except:
        session["gold"] = 0

    #Checks to see if session['activities'] exists and if it does not, creates it
    try:
        session['activities']
    except:
        session['activities'] = []

    #Renders the html page we will continually redirect to
    return render_template('index.html')

#Begins our route process for calculating gold and redirecting back to index
@app.route('/process', methods=["POST"])
def process():

    #Defines our buildings and how much each will randomly generate
    buildings = {
    'farm':random.randint(10,20),
    'cave':random.randint(5,10),
    'house':random.randint(2,5),
    'casino':random.randint(-50,50)
    }

    #Checks to see which building we selected and sets the random int = result
    if request.form['building'] in buildings:
        result = buildings[request.form['building']]

        #Adds result to total session['gold']
        session['gold'] = session['gold'] + result

        #Creates our activity log entries
        result_log =    {

                        #If result is not greater than 0, color is red. If greater than it is green.
                        'class': ('red','green')[result > 0],

                        #Formats the output into the string that will be appended in the html
                        'activity': "You went to the {} and {} {} gold!".format(request.form['building'],
                        ('lost','gained')[result > 0], result)
                        }
        #Appends the session['activities'] which will be called upon in the html
        session['activities'].append(result_log)

    #redirects back to
    return redirect('/')

#This defines reset button which clears all sessions and resets back to initial load
@app.route('/reset', methods=["POST"])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
