from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test GET /
def test_read_root():
    # Arrange
    # (client is already arranged)

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    # Should redirect to /static/index.html
    assert response.status_code in (302, 307)
    assert response.headers["location"].endswith("/static/index.html")

# Test GET /activities
def test_read_activities():
    # Arrange
    # (client is already arranged)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Optionally, check for a known activity
    assert "Soccer Team" in data

# Test POST /activities/{activity_name}/signup
def test_signup_activity():
    # Arrange
    activity_name = "Soccer Team"
    email = "test_user@example.com"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code in (200, 400, 404)
    assert isinstance(response.json(), dict)
