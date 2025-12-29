from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSettings(BaseSettings):
    host: str = Field(description="The host address for the application.")
    port: int = Field(description="The port number for the application.")
    SQLALCHEMY_DATABASE_URI: str = Field(description="Database connection URI")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = Field(
        description="Sets if it should track the modificaiton", default=False
    )
    SECRET_KEY: str = Field(description="Flask's secret key")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


env = EnvSettings()  # type: ignore
