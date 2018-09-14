from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "thisissecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    fname = request.form['fname']
    session['fname'] = fname

    lname = request.form['lname']
    session['lname'] = lname

    email = request.form['email']
    session['email'] = email

    password = request.form['password']
    confirm_pw = request.form['confirm_pw']

    if not fname:
        flash("First name cannot be blank.")
    elif not fname.isalpha():
        flash("First name cannot contain numbers.")

    if not lname:
        flash("Last name cannot be blank.")
    elif not fname.isalpha():
        flash("Last name cannot contain numbers.")

    if not email:
        flash("Email cannot be blank.")
    elif not EMAIL_REGEX.match(email):
        flash("Not a valid email.")

    if not password:
        flash("Password cannot be blank.")
    elif len(password) < 8:
        flash("Password must be at least 8 characters.")

    if not confirm_pw:
        flash("Confirm password cannot be blank.")
    elif password != confirm_pw:
        flash("Passwords must match.")


    if "_flashes" in session.keys():
        return redirect('/')
    else:
        return redirect('/success')

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')


app.run(debug=True)
