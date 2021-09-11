from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fruitOrdered = {
        'strawberry': 0,
        'raspberry': 0, 
        'blackberry': 0,
        'apple': 0
    }
    userInfo = {
        'first_name': '',
        'last_name': '',
        'id': ""
    }
    fruitCount = 0;

    fruitOrdered['strawberry'] = int(request.form['strawberry'])
    fruitOrdered['raspberry'] = int(request.form['raspberry'])
    fruitOrdered['blackberry'] = int(request.form['blackberry'])
    fruitOrdered['apple'] = int(request.form['apple'])
    fruitCount = sum(fruitOrdered.values())

    userInfo['first_name'] = request.form['first_name']
    userInfo['last_name'] = request.form['last_name']
    userInfo['id'] = request.form['id']

    return render_template("checkout.html", fruits=fruitOrdered, count=fruitCount, user=userInfo)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    