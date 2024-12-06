import pydantic_settings
from pydantic import SecretStr


class UserConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(env_prefix="QA_", env_file=".env", frozen=True, extra="ignore")

    username: str = ""
    password: str = ""


class EnvConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_ENV_", env_file=".env", frozen=True, extra="ignore"
    )

    url: str = ""
