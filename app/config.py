import os


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./avito_clone.db")
API_V1_PREFIX = "/api/v1"
