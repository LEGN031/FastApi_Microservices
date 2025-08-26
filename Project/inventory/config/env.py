import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

class Config:
    REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
    

    @property
    def REDIS_URL(self):
        return f"redis://default:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"
    
a = Config()