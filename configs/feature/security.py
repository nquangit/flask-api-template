from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class SecurityConfig(BaseSettings):
    """
    Secret Key configs
    """

    SECRET_KEY: Optional[str] = Field(
        description="Your App secret key will be used for securely signing the session cookie"
        "Make sure you are changing this key for your deployment with a strong key."
        "You can generate a strong key using `openssl rand -base64 42`."
        "Alternatively you can set it with `SECRET_KEY` environment variable.",
        default=None,
    )
