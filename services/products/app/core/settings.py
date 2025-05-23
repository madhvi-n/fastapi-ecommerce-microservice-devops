import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    ENV = os.getenv("ENV", "development")
    if ENV == "production":
        DATABASE_URL = os.getenv("DATABASE_URL")  # PostgreSQL in production
    else:
        DATABASE_URL = "sqlite:///./db.sqlite"
    if not DATABASE_URL:
        print("Error: DATABASE_URL not set!")

    PREFIX = "/api/v1"
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


settings = Settings()