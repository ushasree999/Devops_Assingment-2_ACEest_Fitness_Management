import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()  # Call the create_app function to create the app instance
    with app.test_client() as client:  # Use the app instance to create a test client
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness and Gym Management System!" in response.data

def test_add_workout(client):
    response = client.post('/workouts', json={"workout": "Running", "duration": 30})
    assert response.status_code == 201
    assert b"'Running' added successfully!" in response.data

def test_get_workouts(client):
    client.post('/workouts', json={"workout": "Running", "duration": 30})
    response = client.get('/workouts')
    assert response.status_code == 200
    assert b"Running" in response.data