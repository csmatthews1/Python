from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("play.html", num=3, color="cornflowerblue")

@app.route('/play/<int:num>')
def playNum(num):
    return render_template("play.html", num=num, color="cornflowerblue")	

@app.route('/play/<int:num>/<string:color>')
def playNumCol(num, color):
    return render_template("play.html", num=num, color=color)	

if __name__=="__main__":
    app.run(debug=True)