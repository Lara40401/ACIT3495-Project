from flask import Flask, request, render_template, redirect, url_for, session
import requests
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

db_config = {
    'host': os.getenv("MYSQL_HOST"),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DATABASE")
}

AUTH_SERVICE_URL = 'http://auth_service:3000'
courses = ['Math', 'English', 'Science', 'History', 'Social Studies']

@app.route('/')
def home():
    if "token" not in session: 
        return redirect(url_for("login"))
    return render_template("home.html", courses=courses)

@app.route("/login", methods=["GET", "POST"])
def login(): 
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        response = requests.post(f'{AUTH_SERVICE_URL}/login', json={'username': username, 'password': password})
        if response.status_code == 200: 
            data = response.json()
            session["token"] = data["token"]
            return redirect(url_for("home"))
        else: 
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit(): 
    if "token" not in session: 
        return "Unauthorized, 401"
    
    token = session["token"]
    headers = {"Authorization": token}
    response = requests.post(f'{AUTH_SERVICE_URL}/validate', headers=headers)
    if response.status_code != 200: 
        session.pop("token", None)
        return redirect(url_for("login"))
    
    student_number = request.form["student_number"]
    course = request.form["course"]
    grade = request.form["grade"]

    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    cursor.execute('INSERT INTO grades (student_number, course, grade) VALUES (%s, %s, %s)', (student_number, course, grade))
    cnx.commit()
    cursor.close()
    cnx.close()

    return redirect(url_for("home", message="Grade recorded successfully"))

@app.route("/logout")
def logout(): 
    session.pop("token", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    print("Running on http://127.0.0.1:{port}")