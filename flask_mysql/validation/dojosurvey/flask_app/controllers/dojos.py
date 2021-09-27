from flask_app import app
from flask import Flask,render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route('/')         
def index():
    return render_template("index.html")
    
@app.route('/submit', methods=['POST'])         
def submit():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    
    Dojo.save(request.form)
    return redirect("/result")
    
@app.route('/result')         
def result():
    dojo = Dojo.get_last()
    return render_template('result.html', dojo = dojo)
    
@app.route('/goback')         
def goback():
    session.clear()
    return render_template('index.html')
