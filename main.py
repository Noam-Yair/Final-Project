from User_Input import create_connection, select_all_items, search_for_all_users


def main():

    database = r"C:\sqlite\db\pythonsqlite.db"
    # create a database connection
    conn = create_connection("db.sqlite3")
    with conn:
        select_all_items(conn, "Item")
    search_for_all_users(conn)


if __name__ == '__main__':
    main()



