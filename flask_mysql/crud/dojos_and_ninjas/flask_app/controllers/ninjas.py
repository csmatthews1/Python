from flask_app import app
from flask import Flask,render_template, redirect, request
from flask_app.models.ninja import Ninja

@app.route('/ninjas/create',methods=['POST'])
def create_user():
    Ninja.save(request.form)
    return redirect ('/')

