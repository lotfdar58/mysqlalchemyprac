import json

from database import run_query_1, run_query_2, run_query_3, multiple_create, upsert_user, add_json


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
        upsert_user(4, 'John Do', 'john.do@example.com')
    except Exception as e:
        print(e)

    try:
        json_data = {
            "key1": "value1",
            "key2": "value2",
            "key3": [1, 2, 3]
        }
        # Convert JSON data to a string
        json_string = json.dumps(json_data)
        add_json(14, 'KK', 'kk.do@example.com', json_string)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
