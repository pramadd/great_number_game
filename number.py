from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    rand = random.randrange(0, 101) 
    rand = int(rand)
    session['rand'] = rand # set session  like so
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def take_number():
    playerNumber = int(request.form['number'])
    print "Random:",session['rand']
    print "My number:",playerNumber

    if playerNumber == session['rand']:
        print "equal"
        return redirect('/green')
    elif playerNumber > session['rand']:
        print "toohigh"
        return redirect('/toohigh')
    elif playerNumber < session['rand']:
        print "tooLow"
        return redirect('/toolow')

@app.route('/green')
def green():
    return render_template("green.html")

@app.route('/toohigh')
def redhigh():
    return render_template("toohigh.html")

@app.route('/toolow')
def redlow():
    return render_template("toolow.html")

@app.route('/last')
def reset_page():
    return redirect('/') # redirect to a route not file

app.run(debug=True)