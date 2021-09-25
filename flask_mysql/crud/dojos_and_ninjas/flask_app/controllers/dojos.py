from flask_app import app
from flask import Flask,render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    # call the get all classmethod to get all users
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos = dojos)

@app.route('/dojos/create',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect ('/dojos')

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos = dojos)

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id":id
    }
    dojo = Dojo.get_with_ninjas(data)
    return render_template("showdojo.html", dojo=dojo)

