from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for workouts
workouts = []

@app.route('/')
def home():
    return "Welcome to ACEest Fitness and Gym Management System!"

@app.route('/workouts', methods=['GET'])
def get_workouts():
    if not workouts:
        return jsonify({"message": "No workouts logged yet."}), 200
    return jsonify(workouts), 200

@app.route('/workouts', methods=['POST'])
def add_workout():
    data = request.get_json()
    workout = data.get('workout')
    duration = data.get('duration')

    if not workout or not duration:
        return jsonify({"error": "Please provide both workout and duration."}), 400

    try:
        duration = int(duration)
        workouts.append({"workout": workout, "duration": duration})
        return jsonify({"message": f"'{workout}' added successfully!"}), 201
    except ValueError:
        return jsonify({"error": "Duration must be a number."}), 400

if __name__ == '__main__':
    app.run(debug=True)