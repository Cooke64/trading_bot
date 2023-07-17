import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Settings:
    TRAIDER_TOKEN: str = os.environ.get("TRAIDER_TOKEN")
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")


settings = Settings()
