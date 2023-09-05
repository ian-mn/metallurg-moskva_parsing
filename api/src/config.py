from pydantic import Field
from pydantic_settings import BaseSettings


class PGSettings(BaseSettings):
    host: str = Field("db", env="DB_HOST")
    port: int = Field(5432, env="DB_PORT")
    password: str = Field("1234qwer", env="DB_PASSWORD")
    user: str = Field("parser", env="DB_USER")
    dbname: str = Field("parsing", env="DB_NAME")


class APISettings(BaseSettings):
    project_name: str = Field("parsing", env="PROJECT_NAME")
