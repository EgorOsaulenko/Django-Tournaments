from pydantic_settings import BaseSettings, SettingsConfigDict

class  Settings(BaseSettings):
    engine: str
    name: str
    user: str
    password: str
    host: str
    port: int


    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()