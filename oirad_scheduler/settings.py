from pydantic import AnyUrl, BaseSettings, Field
from sqlalchemy.engine.url import make_url


class Settings(BaseSettings):
    LOG_LEVEL: str = "DEBUG"
    LOG_FORMAT: str = (
        "{level} {time:YYYY-MM-DD HH:mm:ss} {name}:{function}-{message} | {extra}"
    )

    class Config:
        env_file_encoding = "utf8"
        env_file = ".env"
        extra = "ignore"


class DatabaseSettings(BaseSettings):
    user: str = Field(
        ...,
        description="Database username",
    )
    password: str = Field(
        ...,
        description="Database password",
    )
    url: AnyUrl = Field(
        ...,
        description="Database URL (DSN)",
    )

    @property
    def full_url_sync(self) -> str:
        """
        URL (DSN) path with user, password, and sync driver
        """
        url = make_url(self.url)
        url = url.set(
            drivername="postgresql",
            username=self.user,
            password=self.password,
        )
        return str(url)

    @property
    def full_url_async(self) -> str:
        """
        URL (DSN) path with user, password, and async driver
        """
        url = make_url(self.url)
        url = url.set(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password,
        )
        return str(url)

    class Config:
        env_prefix = "database_"
        env_file_encoding = "utf8"
        env_file = ".env"
        extra = "ignore"


settings = Settings()
database_settings = DatabaseSettings()
