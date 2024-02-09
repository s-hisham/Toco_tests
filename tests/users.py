import requests

base_url = "https://api.users.com"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}  # Replace with your actual access token

# Test the /users endpoint to create a new user (Success Scenario)
def test_create_user_success():
    user_data = {"name": "Sara Hisham", "email": "sara@test.com", "password": "password123"}
    response = requests.post(f"{base_url}/users", json=user_data, headers=headers)

    # Assert that the user creation was successful
    assert response.status_code == 201


# Test the /users endpoint with invalid data (negative scenario)
def test_create_user_invalid_data():
    user_data = {"name": "", "email": "sara@test.com", "password": "password123"}
    response = requests.post(f"{base_url}/users", json=user_data, headers=headers)

    # Assert that the API returns bad request due to invalid data (missing name)
    assert response.status_code == 400


if __name__ == "__main__":
    test_create_user_success()
    test_create_user_invalid_data()
