from flask_app import app
from flask import Flask,render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/send', methods=['POST'])         
def send_message():

    data = {
        'author_id': request.form['author_id'],
        'recipient_id': request.form['recipient_id'],
        'message': request.form['message'],
    }
    Message.save(data)
    return redirect("/success")

@app.route('/delete/message/<int:id>')         
def delete_message(id):

    data = {
        'id': id,
    }
    Message.delete(data)
    return redirect("/success")

