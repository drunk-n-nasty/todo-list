from dataclasses import dataclass
import os 
from dotenv import load_dotenv
load_dotenv()

@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    allow_origins: list[str]

def get_settings():
    return Settings(
        DATABASE_URL = os.getenv('DATABASE_URL'),
        allow_origins = os.getenv('allow_origins')
    )

