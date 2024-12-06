from src.configs import EnvConfig
import pytest


@pytest.fixture(scope="session")
def env_config_auth_url(env_config) -> str:
    """Environment variables (like url)"""
    return f"{env_config.url}/auth"
