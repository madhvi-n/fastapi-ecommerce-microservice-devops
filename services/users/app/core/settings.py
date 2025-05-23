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

    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        print("Error: SECRET_KEY not set!")

    DEBUG = os.getenv("DEBUG", False)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    PREFIX = "/api/v1"
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
    GITHUB_REDIRECT_URI = os.getenv("GITHUB_REDIRECT_URI")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


settings = Settings()