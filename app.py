from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data storage
workouts = {"Warm-up": [], "Workout": [], "Cool-down": []}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/log_workout', methods=['GET', 'POST'])
def log_workout():
    if request.method == 'POST':
        category = request.form['category']
        exercise = request.form['exercise']
        duration = request.form['duration']
        if category and exercise and duration:
            workouts[category].append({"exercise": exercise, "duration": int(duration)})
            return redirect(url_for('view_summary'))
    return render_template('log_workout.html', categories=workouts.keys())

@app.route('/view_summary')
def view_summary():
    total_time = sum(sum(entry['duration'] for entry in sessions) for sessions in workouts.values())
    return render_template('view_summary.html', workouts=workouts, total_time=total_time)

@app.route('/user_info')
def user_info():
    return render_template('user_info.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)