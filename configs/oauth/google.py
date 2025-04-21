from pydantic_settings import BaseSettings
from pydantic import Field, computed_field
from typing import Optional


class GoogleOAuthConfig(BaseSettings):
    GOOGLE_CLIENT_ID: Optional[str] = Field(
        description="Google OAuth Client ID",
        default=None,
    )

    GOOGLE_CLIENT_SECRET: Optional[str] = Field(
        description="Google OAuth Client Secret",
        default=None,
    )

    GOOGLE_DISCOVERY_URL: Optional[str] = Field(
        description="Google OAuth Discovery URL",
        default=None,
    )

    @computed_field
    @property
    def GOOGLE_CLIENT_IDS(self) -> list[str] | None:
        if self.GOOGLE_CLIENT_ID:
            return self.GOOGLE_CLIENT_ID.split(",")
        else:
            return None
