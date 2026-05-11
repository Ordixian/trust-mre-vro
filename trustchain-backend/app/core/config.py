import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load the .env file from the root directory
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "TrustChain AI"
    VERSION: str = "1.0.0"
    APP_ENV: str = os.getenv("APP_ENV", "development")
    
    # Squad API Keys
    SQUAD_SECRET_KEY: str = os.getenv("SQUAD_SECRET_KEY")
    SQUAD_BASE_URL: str = "https://api-d.squadco.com" # Sandbox URL
    
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/trustchain")
    
    # File Uploads
    MAX_UPLOAD_SIZE: int = 5242880 # 5MB limit
    ALLOWED_EXTENSIONS: list = ["jpg", "jpeg", "png"]

    class Config:
        case_sensitive = True

# Global instance to be used across the app
settings = Settings()