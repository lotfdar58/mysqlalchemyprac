from database import run_query_1, run_query_2


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


if __name__ == '__main__':
    main()