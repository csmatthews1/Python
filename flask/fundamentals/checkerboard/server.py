from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board():
    return render_template("board.html", width=8, height=8, color="black")

@app.route('/<int:height>')
def board_height(height):
    return render_template("board.html", width=8, height=height, color="black")	

@app.route('/<int:height>/<int:width>')
def board_h(height, width):
    return render_template("board.html", width=width, height=height, color="black")	

@app.route('/<int:height>/<int:width>/<string:color>')
def board_hw(height, width, color):
    return render_template("board.html", width=width, height=height, color=color)	

if __name__=="__main__":
    app.run(debug=True)