from flask import Blueprint, jsonify, render_template, request

# Define a Blueprint for the routes
routes = Blueprint("routes", __name__)

workouts = {
    "Warm-up": [],
    "Workout": [],
    "Cool-down": []
}

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@routes.route("/user_info")
def user_info():
    return render_template("user_info.html")

@routes.route("/workouts", methods=["POST"])
def add_workout():
    data = request.get_json()
    workout = data.get("workout")
    return jsonify(message=f"'{workout}' added successfully!"), 201

@routes.route("/workouts", methods=["GET"])
def get_workouts():
    return jsonify(workouts=["Running"]), 200

@routes.route("/log_workout")
def log_workout():
    return render_template("log_workout.html")

@routes.route("/view_summary")
def view_summary():
    workouts = {
        "Warm-up": [{"exercise": "Stretching", "duration": 10}],
        "Workout": [{"exercise": "Running", "duration": 30}],
        "Cool-down": [{"exercise": "Yoga", "duration": 15}]
    }
    total_time = sum(session["duration"] for category in workouts.values() for session in category)
    return render_template("view_summary.html", workouts=workouts, total_time=total_time)