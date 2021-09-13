from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'dojosurveyform'

@app.route('/')         
def index():
    return render_template("index.html")
    
@app.route('/submit', methods=['POST'])         
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/result")
    
@app.route('/result')         
def result():
    return render_template('result.html')
    
@app.route('/goback')         
def goback():
    session.clear()
    return render_template('index.html')
    
if __name__=="__main__":   
    app.run(debug=True)    