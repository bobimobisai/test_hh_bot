from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    API_KEY: str

    @property
    def BOT_TOKEN_G(self):
        return self.BOT_TOKEN

    @property
    def API_KEY_G(self):
        return self.API_KEY

    model_config = SettingsConfigDict(env_file="venv/.env")


settings = Settings()
