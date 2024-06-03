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
engine = create_engine(connection_string, echo=False)

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


def multiple_create():
    session = Session()
    try:
        query_string = "INSERT INTO  users values (4, 'gg', 'aa.ik@yahooo.com')"
        session.execute(text(query_string))

        query_string = "INSERT INTO  users values (4,'ff', 'bb.ik@yahooo.com')"
        session.execute(text(query_string))

        # Commit the transaction if all queries succeed
        session.commit()
        return "Transaction committed successfully"
    except Exception as e:
        # Rollback the transaction if any query fails
        session.rollback()
        raise RuntimeError(f"Transaction failed: {str(e)}")
    finally:
        session.close()


def upsert_user(user_id, name, email):
    session = Session()
    try:
        query_string = """
            INSERT INTO users (id, name, email)
            VALUES (:user_id, :name, :email)
            ON CONFLICT (id)
            DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email
        """
        session.execute(text(query_string), {'user_id': user_id, 'name': name, 'email': email})
        session.commit()
        return "Upsert operation committed successfully"
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Upsert operation failed: {str(e)}")
    finally:
        session.close()
