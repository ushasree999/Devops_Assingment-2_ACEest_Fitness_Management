import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()  # Call the create_app function to create the app instance
    with app.test_client() as client:  # Use the app instance to create a test client
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    expected_html = (
        b'<!DOCTYPE html>\n<html>\n<head>\n    <title>ACEest Fitness</title>\n</head>\n'
        b'<body>\n    <h1>Welcome to ACEest Fitness & Gym Tracker</h1>\n    <a href="/log_workout">Log Workout</a> | '
        b'<a href="/view_summary">View Summary</a> | <a href="/user_info">User Info</a>\n</body>\n</html>'
    )
    assert response.data == expected_html

def test_add_workout(client):
    response = client.post('/workouts', json={"workout": "Running", "duration": 30})
    assert response.status_code == 201
    assert b"'Running' added successfully!" in response.data

def test_get_workouts(client):
    client.post('/workouts', json={"workout": "Running", "duration": 30})
    response = client.get('/workouts')
    assert response.status_code == 200
    assert b"Running" in response.data