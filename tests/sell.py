import requests
import time

base_url = "https://api.sell.com"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}  # Replace with your actual access token


# Test the /sell endpoint to sell Tocos (Success Scenario)
def test_sell_tocos_success():
    sell_data = {"amount": 50}

    start_time = time.time()
    response = requests.post(f"{base_url}/sell", json=sell_data, headers=headers)
    end_time = time.time()

    # Assert that the Tocos sale was successful
    assert response.status_code == 201

    # Assert the response time is within acceptable limits (under 2 seconds)
    assert end_time - start_time < 2


# Test the /sell endpoint with more Tocos than available (Error Scenario)
def test_sell_tocos_exceeds_balance():
    sell_data = {"amount": 1000000}  # Attempt to sell more Tocos than available balance/ daily limit
    response = requests.post(f"{base_url}/sell", json=sell_data, headers=headers)

    # Assert that the API returns an error (bad request) due to exceeding balance/ daily limit
    assert response.status_code == 400


if __name__ == "__main__":
    test_sell_tocos_success()
    test_sell_tocos_exceeds_balance()
