### sqlalchemy
https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_connecting_to_database.htm
https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html

## create_engine()
Engine class connects a Pool and Dialect together to provide a source of database connectivity and behavior.
An object of Engine class is instantiated using the create_engine() function.


## TextClause - text()
https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.text
The advantages text() provides over a plain string are backend-neutral support for bind parameters, 
per-statement execution options, as well as bind parameter and result-column typing behavior, 
allowing SQLAlchemy type constructs to play a role when executing a statement that is specified literally. 
The construct can also be provided with a .c collection of column elements, allowing it to be embedded in other 
SQL expression constructs as a subquery.

Bind parameters are specified by name, using the format :name. E.g.:
t = text("SELECT * FROM users WHERE id=:user_id")
result = connection.execute(t, {"user_id": 12})

## Getting a Connection
>>> from sqlalchemy import text

>>> with engine.connect() as conn:
...     result = conn.execute(text("select 'hello world'"))
...     print(result.all())

## Getting a Connection using Session:
>>> from sqlalchemy.orm import Session

>>> stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
>>> with Session(engine) as session:
...     result = session.execute(stmt, {"y": 6})
...     for row in result:
...         print(f"x: {row.x}  y: {row.y}")