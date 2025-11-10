import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()  # Call the create_app function to create the app instance
    with app.test_client() as client:  # Use the app instance to create a test client
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data  # Replace "Welcome" with actual content from `index.html`

def test_log_workout_route(client):
    response = client.get('/log_workout')
    assert response.status_code == 200
    assert b"Log Workout" in response.data  # Replace with actual content from `log_workout.html`

def test_view_summary_route(client):
    response = client.get('/view_summary')
    assert response.status_code == 200
    assert b"Workout Summary" in response.data  # Replace with actual content from `view_summary.html`

def test_user_info_route(client):
    response = client.get('/user_info')
    assert response.status_code == 200
    assert b"User Information" in response.data  # Replace with actual content from `user_info.html`