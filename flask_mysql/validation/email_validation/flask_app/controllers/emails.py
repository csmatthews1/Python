from flask_app import app
from flask import Flask,render_template, redirect, request
from flask_app.models.email import Email

@app.route('/')         
def index():
    return render_template("index.html")
    
@app.route('/submit', methods=['POST'])         
def submit():
    if not Email.validate_email(request.form):
        return redirect('/')
    
    Email.save(request.form)
    return redirect("/success")
    
@app.route('/success')         
def result():
    emails = Email.get_all()
    new_email = Email.get_last().email;
    return render_template('success.html', emails = emails, new_email=new_email)
    
@app.route('/goback')         
def goback():
    session.clear()
    return render_template('index.html')
