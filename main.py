from db_funcs import create_connection, select_all_items, search_for_all_users, insert_data
import schedule
import time


def main():
    # insert_data()
    database = r"C:\sqlite\db\pythonsqlite.db"
    # create a database connection
    conn = create_connection("db.sqlite3")
    with conn:
        select_all_items(conn, "Item")
    schedule.every(12).hours.do(search_for_all_users, conn)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()



