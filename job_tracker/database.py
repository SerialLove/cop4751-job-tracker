import mysql.connector

def get_db():
    """Establishes and returns a connection to the MySQL job_tracker database."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='job_tracker'
    )