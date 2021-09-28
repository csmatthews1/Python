from flask_app import app
from flask import Flask,render_template, redirect, request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

@app.route('/')         
def index():
    return render_template("index.html")
    
@app.route('/register', methods=['POST'])         
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': crypt.generate_password_hash(request.form['password'])
    }
    User.save(data)
    session['user'] = request.form['email']
    return redirect("/success")
    
@app.route('/login', methods=['POST'])         
def login():
    if not User.validate_login(request.form):
        return redirect('/')

    user_in_db = User.get_by_email(request.form)
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect ('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect ('/')

    session['user'] = request.form['email']
    return redirect("/success")
    
@app.route('/success')         
def result():
    return render_template('success.html')
    
@app.route('/goback')         
def goback():
    session.clear()
    return redirect('/')
