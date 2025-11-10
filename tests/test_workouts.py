from app import workouts

def test_add_workout():
    workouts["Warm-up"].append({"exercise": "Jumping Jacks", "duration": 5})
    assert len(workouts["Warm-up"]) == 1
    assert workouts["Warm-up"][0]["exercise"] == "Jumping Jacks"
    assert workouts["Warm-up"][0]["duration"] == 5

def test_total_time():
    workouts["Warm-up"] = [{"exercise": "Jumping Jacks", "duration": 5}]
    workouts["Workout"] = [{"exercise": "Push-ups", "duration": 10}]
    total_time = sum(sum(entry['duration'] for entry in sessions) for sessions in workouts.values())
    assert total_time == 15