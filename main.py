from database import run_query_1, run_query_2, run_query_3, multiple_create, upsert_user


def main():
    rows = run_query_1()
    # Print the results
    print(type(rows))
    for row in rows:
        print(f"ID: {row.id}, Name: {row.name}, Email: {row.email}")

    rows = run_query_2()
    # Print the results
    print(type(rows))
    for row in rows:
        print(f"ID: {row.id}, Name: {row.name}, Email: {row.email}")

    rows = run_query_3()
    # Print the results
    print(rows)


# try:
#     multiple_create()
# except Exception as e:
#     print(e)

try:
    upsert_user(4, 'John Doe', 'john.doe@example.com')
except Exception as e:
    print(e)


if __name__ == '__main__':
    main()
