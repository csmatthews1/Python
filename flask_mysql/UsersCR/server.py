from flask import Flask, render_template, request, redirect

# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    # call the get all classmethod to get all users
    users = User.get_all()
    return render_template("index.html", all_users = users)

@app.route('/user/new')
def newuser():
    return render_template("newuser.html")

@app.route('/user/create',methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect ('/users') 

if __name__ == "__main__":
    app.run(debug=True)
