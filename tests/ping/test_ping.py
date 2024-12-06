import requests
from pytest_check import check


def test_ping(env_config_ping_url):
    response: Request.response = requests.get(url=env_config_ping_url)

    with check:
        assert response.status_code == 201
    with check:
        assert response.text == "Created"
