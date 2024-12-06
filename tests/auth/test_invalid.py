import requests
from pytest_check import check


def test_invalid(env_config, user_config, env_config_auth_url):
    # url: str = f"{env_config.url}/auth"
    # url = env_config.url
    json: dict[str, str] = {
        "username": user_config.username,
        "password": str(user_config.password + "a"),
    }
    response: requests.Response = requests.post(url=env_config_auth_url, json=json)
    with check:
        assert "reason" in response.json()
    with check:
        assert response.status_code == 200
    print(response.json())
