import json

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

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


def run_query_1():
    with Session(engine) as session:
        try:
            rows = session.query(User).all()
            return rows
        except Exception as e:
            raise RuntimeError(f"Transaction failed: {str(e)}")


def run_query_2():
    with Session(engine) as session:
        try:
            query_string = "SELECT * FROM users"
            result = session.execute(text(query_string))
            # Fetch all results
            rows = result.fetchall()
            return rows
        except Exception as e:
            raise RuntimeError(f"Transaction failed: {str(e)}")


def run_query_3():
    with Session(engine) as session:
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
        except Exception as e:
            raise RuntimeError(f"Transaction failed: {str(e)}")


def multiple_create():
    with Session(engine) as session:
        try:
            query_string = "INSERT INTO  users values (7, 'gg', 'aa.ik@yahooo.com')"
            session.execute(text(query_string))

            query_string = "INSERT INTO  users values (6,'ff', 'bb.ik@yahooo.com')"
            session.execute(text(query_string))
            session.commit()

            return "Transaction committed successfully"
        except Exception as e:
            raise RuntimeError(f"Transaction failed: {str(e)}")


def upsert_user(user_id, name, email):
    with Session(engine) as session:
        try:
            query_string = """
                INSERT INTO users (id, name, email)
                VALUES (:user_id, :name, :email)
                ON CONFLICT (id)
                DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email
            """
            session.execute(text(query_string), {'user_id': user_id, 'name': name, 'email': email})
            session.commit()
        except Exception as e:
            raise RuntimeError(f"Upsert operation failed: {str(e)}")
