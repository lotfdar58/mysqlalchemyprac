import json

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from user import User

# Database connection configuration
db_config = {
    'username': 'postgres',
    'password': '123',
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres'
}

# Connection string
connection_string = f"postgresql+psycopg2://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

# Create an engine
engine = create_engine(connection_string)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

def run_query_1():

    session = Session()
    try:
        rows = session.query(User).all()
        return rows
    finally:
        # Close the session
        session.close()


def run_query_2():
    # Create a session
    session = Session()

    try:
        query_string = "SELECT * FROM users"
        result = session.execute(text(query_string))
        # Fetch all results
        rows = result.fetchall()
        return rows
    finally:
        # Close the session
        session.close()


def run_query_3():
    # Create a session
    session = Session()

    try:
        query_string = "SELECT * FROM users"
        result = session.execute(text(query_string))
        # Fetch all results
        rows = result.fetchall()
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in rows]

        # Convert to JSON string
        json_data = json.dumps(data, default=str)  # default=str to handle datetime and other non-serializable types

        return json_data
    finally:
        # Close the session
        session.close()
