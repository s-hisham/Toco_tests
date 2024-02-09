import requests
import time

base_url = "https://api.transactions.com"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}  # Replace with your actual access token


# Test the /transactions/{userId} endpoint to get transaction history for a user (Success Scenario)
def test_get_transaction_history_success():
    user_id = "user123"  # Replace with an existing user ID

    start_time = time.time()
    response = requests.get(f"{base_url}/transactions/{user_id}", headers=headers)
    end_time = time.time()

    # Assert that the request was successful
    assert response.status_code == 200

    # Assert the response time is within acceptable limits (under 2 seconds)
    assert end_time - start_time < 2

    # Assert that the response contains transaction history data
    assert isinstance(response.json(), list)


# Test the /transactions/{userId} endpoint with non-existent user ID (Error Scenario)
def test_get_transaction_history_nonexistent_user():
    user_id = "non_existent_user"  # Replace with a non-existent user ID

    response = requests.get(f"{base_url}/transactions/{user_id}", headers=headers)

    # Assert that the API returns an error for non-existing user
    assert response.status_code == 404

    # Assert that the response contains an error message
    assert "error" in response.json()


# Test the /transactions/{userId} endpoint without proper authorization (Security Consideration)
def test_get_transaction_history_unauthorized():
    unauthorized_headers = {}  # No authorization token provided
    user_id = "user123"  # Replace with an existing user ID
    response = requests.get(f"{base_url}/transactions/{user_id}", headers=unauthorized_headers)

    # Assert that the API returns an error due to unauthorized access
    assert response.status_code == 401


# Test the /transactions endpoint to make a transaction (Success Scenario)
def test_post_transaction_success():
    transaction_data = {"from": "user123", "to": "user456", "amount": 100}
    response = requests.post(f"{base_url}/transactions", json=transaction_data, headers=headers)

    # Assert that the transaction was successful
    assert response.status_code == 201
    assert "id" in response.json()  # Assuming the response contains the ID of the created transaction


# Test the /transactions endpoint with invalid data (Error Scenario)
def test_post_transaction_invalid_data():
    transaction_data = {"from": "user123", "to": "user456", "amount": -100}  # Negative amount is invalid
    response = requests.post(f"{base_url}/transactions", json=transaction_data, headers=headers)

    # Assert that the API returns an error for invalid data
    assert response.status_code == 400
    assert "error" in response.json()  # Assuming the response contains an error message


# Test the /transactions endpoint without proper authorization (Security Consideration)
def test_post_transaction_unauthorized():
    unauthorized_headers = {}  # No authorization token provided
    transaction_data = {"from": "user123", "to": "user456", "amount": 100}
    response = requests.post(f"{base_url}/transactions", json=transaction_data, headers=unauthorized_headers)

    # Assert that the API returns an error due to unauthorized access
    assert response.status_code == 401


if __name__ == "__main__":
    # GET endpoint scenarios
    test_get_transaction_history_success()
    test_get_transaction_history_nonexistent_user()
    test_get_transaction_history_unauthorized()

    # POST endpoint scenarios
    test_post_transaction_success()
    test_post_transaction_invalid_data()
    test_post_transaction_unauthorized()
