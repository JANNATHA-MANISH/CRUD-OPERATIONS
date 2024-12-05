import os
from dotenv import load_dotenv

# Load environment variables from .env file (optional but recommended for sensitive data)
load_dotenv()

# Environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
SSL_CERT_PATH = os.getenv("SSL_CERT_PATH", "")
SSL_KEY_PATH = os.getenv("SSL_KEY_PATH", "")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
