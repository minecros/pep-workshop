import requests
from pytest_check import check


def test_valid(env_config, user_config, env_config_auth_url):
    # url: str = f"{env_config.url}/auth"
    # json: dict[str, str] = {"username": user_config.username, "password": str(user_config.password.get_secret_value())}
    # response: requests.Response = requests.post(url=url, json=json)
    response: requests.Response = requests.post(url=env_config_auth_url, json=user_config.model_dump())
    with check:
        assert "token" in response.json()
    with check:
        assert response.status_code == 200
    print(response.json())
