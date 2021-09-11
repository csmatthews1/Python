from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'bananasplit'

@app.route('/')         
def index():
    if 'key_name' in session:
        session['key_name'] += 1
    else:
        session['key_name'] = 1

    return render_template("count.html")
    
@app.route('/alterVisits', methods=['POST'])
def alterVisits():
    print(request.form)
    if 'click' in request.form:
        session['key_name'] += 1
        return redirect ('/')
    elif 'reset' in request.form:
        return redirect("/destroy_session")
 

@app.route("/destroy_session")
def clear_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    