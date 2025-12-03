from flask import Flask, request, render_template, redirect,url_for, session
import pymongo
import os
import requests

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
DB_NAME = os.getenv("MONGO_INITDB_DATABASE")

AUTH_SERVICE_URL = "http://auth_service:3000"

def get_analytics():
    client = pymongo.MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@mongo:27017/",authSource=DB_NAME)
    mongo_db = client[DB_NAME]
    mongo_collection = mongo_db["course_stats"]
    analytics = list(mongo_collection.find({}, {"_id": 0, "course": 1, "max": 1, "min": 1, "avg": 1}))
    client.close()
    return analytics

@app.route("/show_results", methods=["GET"])
def show_results():
    if "token" not in session:
        #return redirect(f"{AUTH_SERVICE_URL}/login?next={request.url}")
        return redirect(url_for("login"))
    
    course_analytics = get_analytics()
    return render_template("results.html", data=course_analytics)

@app.route("/login", methods=["GET", "POST"])
def login(): 
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        res = requests.post(f'{AUTH_SERVICE_URL}/login', json={'username': username, 'password': password})
        if res.status_code == 200: 
            data = res.json()
            session["token"] = data["token"]
            return redirect(url_for("show_results"))
        else: 
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("token", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
