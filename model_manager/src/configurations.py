import os

class DBConfigurations:
    postgres_username = os.getenv("POSTGRES_USER")
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    postgres_port = int(os.getenv("POSTGRES_PORT", 5432))
    postgres_db = os.getenv("POSTGRES_DB")
    postgres_server = os.getenv("POSTGRES_SERVER")
    sql_alchemy_database_url = (
        f"postgresql://{postgres_username}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"
    )

class APIConfigurations:
    title = os.getenv("API_TITLE", "Model Manager")
    description = os.getenv("API_DESCRIPTION", "Machine learning model management system")
    version = os.getenv("API_VERSION", "0.1")
