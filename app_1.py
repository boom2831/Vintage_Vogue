from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Explore_car")
def index1():
    return render_template("Explore_car.html")

@app.route("/AboutUs")
def index2():
    return render_template("AboutUs.html")

@app.route("/Blog")
def index3():
    return render_template("Blog.html")

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        pickup = request.form['pickupDate']
        returnDate = request.form['returnDate']
        comments = request.form['comments']
        insert_form(name, email, phone, pickup, returnDate, comments)
        flash("Form submitted successfully")
        return redirect(url_for('form'))
    return render_template('form.html')

@app.route("/Signin", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        if verify(password, cpassword):
            insert_signup(username, email, password)
            flash("Signup Successful")
        else:
            flash("Password and Confirm Password mismatch")
    return render_template('Signin.html')

def verify(password, cpassword):
    return password == cpassword

def create_table():
    connection = sqlite3.connect('Form.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Rent (
                      Slno INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      email TEXT,
                      phone TEXT,
                      pickupDate TEXT,
                      returnDate TEXT,
                      comments TEXT)''')
    connection.commit()
    connection.close()

    connection = sqlite3.connect('Signup.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS signup (
                      Slno INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      email TEXT,
                      password TEXT)''')
    connection.commit()
    connection.close()

def insert_form(name, email, phone, pickup, returnDate, comments):
    connection = sqlite3.connect('Form.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Rent (name, email, phone, pickupDate, returnDate, comments) VALUES (?,?,?,?,?,?)",
                   (name, email, phone, pickup, returnDate, comments))
    connection.commit()
    connection.close()

def insert_signup(username, email, password):
    connection = sqlite3.connect('Signup.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO signup (username, email, password) VALUES (?,?,?)",
                   (username, email, password))
    connection.commit()
    connection.close()

create_table()

if __name__ == '__main__':
    app.run(port=2389)
