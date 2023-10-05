from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/login", methods=("GET","POST"))
def login():
    if request.method == "POST":
        reg_number = request.form["reg_number"]
        password = request.form["password"]
        connection = sqlite3.connect('database.db')
        conn = connection.cursor()
        res = conn.execute('SELECT * FROM students WHERE reg_number = ? AND password = ? ', (reg_number,password))
        if res.fetchone() == None:
            success = "Incorrect Username or Password !!!!"
            conn.close()
            return render_template("index.html", success=success)   
            
        success = conn.execute('SELECT * FROM courses WHERE reg_number = ?', (reg_number,))
        if success.fetchone() == None:       
            conn.close()
            return render_template("dashboard.html")
        else:
            response = conn.execute('SELECT * FROM courses WHERE reg_number = ?', (reg_number,))
            has_courses = response.fetchone()
            print("courses", has_courses)
            return render_template("dashboard.html", has_courses=has_courses)
            

@app.route("/createAccount", methods=("GET","POST"))
def createAccount():
    if request.method == "POST":
        print(request.form)
        reg_number = request.form["reg_number"]
        password = request.form["password"]
        level = request.form["level"]
        department = request.form["department"]
        faculty = request.form["faculty"]
        name = request.form["name"]
        surname = request.form["surname"]
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()
        cur.execute(
            "INSERT INTO students (reg_number,password,level,department,faculty,name,surname) VALUES (?, ?, ?, ?, ?, ?, ?)",
             (reg_number,password,level,department,faculty,name,surname)
                     )
        connection.commit()
        connection.close()
        success = "You have successfully created an account"
        return render_template("index.html",success=success)


@app.route("/registerCourse", methods=("GET", "POST"))
def registerCourse():
    if request.method == "POST":
        print(request.form)
        reg_number = request.form["reg_number"]
        name = request.form["name"]
        course1 = request.form["course1"]
        course2 = request.form["course2"]
        course3 = request.form["course3"]
        course4 = request.form["course4"]
        course5 = request.form["course5"]
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()
        cur.execute(
            "INSERT INTO courses (reg_number,course1,course2,course3,course4,course5,name) VALUES (?, ?, ?, ?, ?, ?, ?)",
             (reg_number,course1,course2,course3,course4,course5,name)
                     )
        connection.commit()
        response = cur.execute('SELECT * FROM courses WHERE reg_number = ?', (reg_number,))
        has_courses = response.fetchone()
        #connection.close()
        return render_template("dashboard.html", has_courses=has_courses)