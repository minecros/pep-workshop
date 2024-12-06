import requests
from pytest_check import check


def test_invalid(env_config, user_config, env_config_booking_url):
    response: requests.Response = requests.get(url=env_config_booking_url)
    print(response.text)

    with check:
        assert response.status_code == 200


def test_bad_method(env_config_booking_url):
    response: requests.Response = requests.post(url=env_config_booking_url)
    assert response.status_code == 500


def test_valid_response(env_config_booking_url):
    response: requests.Response = requests.get(url=env_config_booking_url)
    with check:
        assert (response.json())["bookingid"][0] == 67
