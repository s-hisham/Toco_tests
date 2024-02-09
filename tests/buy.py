import requests
import time

base_url = "https://api.buy.com"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}  # Replace with your actual access token


# Test the /buy endpoint to buy Tocos (Success Scenario)
def test_buy_tocos_success():
    buy_data = {"amount": 100, "currency": "USD"}

    start_time = time.time()
    response = requests.post(f"{base_url}/buy", json=buy_data, headers=headers)
    end_time = time.time()

    # Assert that the Tocos purchase was successful
    assert response.status_code == 201

    # Assert the response time is within acceptable limits (under 2 seconds)
    assert end_time - start_time < 2


# Test the /buy endpoint with negative scenario
def test_buy_tocos_insufficient_funds():
    buy_data = {"amount": 1000000, "currency": "USD"}  # Attempt to buy more than available funds/ more than daily limit
    response = requests.post(f"{base_url}/buy", json=buy_data, headers=headers)

    # Assert that the API returns an error (bad request) due to insufficient funds/ limit exceeding
    assert response.status_code == 400


if __name__ == "__main__":
    test_buy_tocos_success()
    test_buy_tocos_insufficient_funds()
