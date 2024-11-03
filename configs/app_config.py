from pydantic_settings import SettingsConfigDict
import os

from configs.deploy import DeploymentConfig
from configs.feature import SecurityConfig
from configs.middleware import DatabaseConfig
from configs.oauth import GoogleOAuthConfig

class RobokiHomeConfig(DeploymentConfig, SecurityConfig, DatabaseConfig, GoogleOAuthConfig):
    """
    Roboki Home configs
    """

    model_config = SettingsConfigDict(
        # read from dotenv format config file
        env_file=".env",
        env_file_encoding="utf-8",
        frozen=True,
        # ignore extra attributes
        extra="ignore",
    )
