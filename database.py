import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
required_settings = ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME"]


def get_connection():
    for setting in required_settings:
        value = os.getenv(setting)
        if not value:
            raise ValueError(f"Missing required environment variable: {setting}")     

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

    return connection

