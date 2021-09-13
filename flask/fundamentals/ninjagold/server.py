from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'dojosurveyform'

@app.route('/')         
def index():
    if session.get('yourgold') == None:
        session['yourgold'] = 0
        session['activity'] = ""
    return render_template("index.html")

@app.route('/process_money',  methods=['POST'])         
def process_money():
    if request.form['location'] == 'farm':
        coins = random.randint(10,20)
        session['activity'] += "Earned "+str(coins)+" golds from the farm! "+ datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\r\n"
        session['yourgold'] += coins
    elif request.form['location'] == 'cave':
        coins = random.randint(5,10)
        session['activity'] += "Earned "+str(coins)+" golds from the cave! "+ datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\r\n"
        session['yourgold'] += coins
    elif request.form['location'] == 'house':
        coins = random.randint(2,5)
        session['activity'] += "Earned "+str(coins)+" golds at the house! "+ datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\r\n"
        session['yourgold'] += coins
    elif request.form['location'] == 'casino':
        coins = random.randint(-50,50)
        if coins >= 0:
            session['activity'] += "Won "+str(coins)+" golds at the casino! "+ datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\r\n"
        else:
            session['activity'] += "Lost "+str(abs(coins))+" at the casino! "+ datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\r\n"
        session['yourgold'] += coins
    return redirect("/")


if __name__=="__main__":   
    app.run(debug=True)    