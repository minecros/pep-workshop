import requests

from src.configs import EnvConfig, UserConfig
import pytest


@pytest.fixture(scope="session")
def env_config() -> EnvConfig:
    """Environment variables (like url)"""
    return EnvConfig()


@pytest.fixture(scope="session")
def user_config() -> UserConfig:
    """AUsername and password for authentication"""
    return UserConfig()


@pytest.fixture(scope="module")
def token(env_config, user_config) -> str | None:
    response: requests.Response = requests.post(url=f"{env_config.url}/auth", json=user_config.model_dump())

    if response.status_code != 200:
        return None

    if "token" not in response.json():
        return None

    return response.json()["token"]
