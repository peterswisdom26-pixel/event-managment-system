import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    DB_HOST = os.getenv("MYSQL_HOST")
    DB_USERNAME = os.getenv("MYSQL_USERNAME")
    DB_PASSWORD =  os.getenv("MYSQL_PASSWORD")
    DB_PORT = int(os.getenv("MYSQL_PORT"))
    DB_DATABASE_NAME = os.getenv("MYSQL_DB_NAME")
    # DB_HOST = "localhost"
    # DB_USERNAME = "root"
    # DB_PASSWORD =  "Femmy@4221"
    # DB_PORT = 3306
    # DB_DATABASE_NAME = "learning_platform"
