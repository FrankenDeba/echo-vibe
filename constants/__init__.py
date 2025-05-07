import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access them

debug = os.getenv("DEBUG") == "True"


PAI_API_KEY = os.getenv("PAI_API_KEY")
PAI_API_END_POINT = os.getenv("PAI_API_END_POINT")
REPORT_FORMAT = os.getenv("REPORT_FORMAT")

DB_USER= os.getenv("DB_USER")
DB_PASSWORD= os.getenv("DB_PASSWORD")
DB_HOST= os.getenv("DB_HOST")
DB_NAME= os.getenv("DB_NAME")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_LLM_MODEL = os.getenv("GROQ_LLM_MODEL")

LLM_SERVICE = os.getenv("LLM_SERVICE")