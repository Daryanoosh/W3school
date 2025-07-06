import csv
from db_connect import connect

# 1 - Insert from CSV using direct insert


def insert_from_csv(csv_file):
    conn = connect()
    cur = conn.cursor()
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("CALL upsert_user(%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Data from CSV inserted (upserted).")
    cur.close()
    conn.close()


# 2 - Insert from console using upsert
def insert_from_console():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    conn.commit()
    print("Inserted/Updated successfully.")
    cur.close()
    conn.close()


# 3 - Search with pattern
def search_by_pattern():
    conn = connect()
    cur = conn.cursor()
    pattern = input("Enter search pattern: ")
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


# 4 - Insert many users
def insert_many_users():
    conn = connect()
    cur = conn.cursor()
    n = int(input("How many users? "))
    users_data = []
    for _ in range(n):
        name = input("Name: ")
        phone = input("Phone: ")
        users_data.append([name, phone])

    # 1️⃣ Correct: call the PROCEDURE you created
    cur.execute("CALL insert_many_users(%s)", (users_data,))
    conn.commit()

    # 2️⃣ Fetch invalid entries logged by the procedure
    cur.execute("SELECT name, phone FROM invalid_phonebook_entries")
    invalid_rows = cur.fetchall()

    if invalid_rows:
        print("\nInvalid rows (skipped):")
        for row in invalid_rows:
            print(f"Name: {row[0]}, Phone: {row[1]}")
    else:
        print("\nAll rows inserted or updated successfully!")

    cur.close()
    conn.close()


# 5 - Paginated query
def get_paginated_results():
    conn = connect()
    cur = conn.cursor()
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


# 6 - Delete by name or phone
def delete_user():
    conn = connect()
    cur = conn.cursor()
    identifier = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_user(%s)", (identifier,))
    conn.commit()
    print("User deleted (if existed).")
    cur.close()
    conn.close()


# 7 - Main Menu
def main():
    while True:
        print("""
        1. Insert from console (upsert)
        2. Insert from CSV (upsert)
        3. Search by pattern
        4. Insert many users with validation
        5. Paginated query
        6. Delete by name or phone
        0. Exit
        """)
        choice = input("Choose option: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            csv_file = input("Enter CSV file path: ")
            insert_from_csv(csv_file)
        elif choice == '3':
            search_by_pattern()
        elif choice == '4':
            insert_many_users()
        elif choice == '5':
            get_paginated_results()
        elif choice == '6':
            delete_user()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
