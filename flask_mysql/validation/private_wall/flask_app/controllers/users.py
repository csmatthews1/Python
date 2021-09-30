from flask_app import app
from flask import Flask,render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.message import Message
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
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    session['user'] = User.save(data)
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

    session['user'] = user_in_db.id
    return redirect("/success")
    
@app.route('/success')         
def result():
    data = {
        'id': session['user']
    }
    user = User.get_by_id(data)
    users = User.get_all()
    messages = Message.get_all_by_recipient(data)
    return render_template('wall.html', user = user, users = users, messages = messages)
    
@app.route('/goback')         
def goback():
    session.clear()
    return redirect('/')
