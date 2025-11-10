from flask import render_template
from app import create_app

app = create_app()

# app/routes.py
workouts = {
    "Warm-up": [],
    "Workout": [],
    "Cool-down": []
}
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/user_info')
def user_info():
    return render_template('user_info.html')