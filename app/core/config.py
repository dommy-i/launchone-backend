import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "LaunchOne"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
