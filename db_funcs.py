import sqlite3

from app import db, User, Item, Search
from item import myItem
import sqlite3
from sqlite3 import Error
from parser1 import search_item
from Send_Mail import send_email


def insert_data():
    first_name = input("please enter your first name")
    last_name = input("please enter your last name")
    mail = input("please enter your email address")
    notify_input = input(
        "please enter 1 if you want to get notification every time an item is uploaded or 0 for once a day")
    # notify_input = check_input(notify_input, int)

    user = User(first_name=first_name, last_name=last_name, email=mail, notify=notify_input)
    db.session.add(user)
    db.session.commit()

    print("please enter the items you are looking for and the maximum price for each item")
    items_list = []
    while "*" != input("press * when finished"):
        item_name = input("enter the item name")
        item_price = input("maximum price for " + item_name)
        item = Item(name=item_name, max_price=item_price)
        items_list.append(item)
        db.session.add(item)
        db.session.commit()

    search = Search(user_id=user.id, items=items_list)
    db.session.add(search)
    db.session.commit()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_items(conn, table):
    """
    Query all rows in the tasks table
    :param table:
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    select = "SELECT * FROM " + str(table)
    cur.execute(select)

    rows = cur.fetchall()

    return rows


def search_for_all_users(conn):
    all_users = select_all_items(conn, "User")
    cur = conn.cursor()
    for user in all_users:
        search_id = "SELECT id FROM Search WHERE user_id = " + str(user[0])
        cur.execute(search_id)  # each user has one search
        search_id = cur.fetchall()
        if search_id:
            search_id = search_id[0]
            users_items = "SELECT item_id FROM search_item WHERE search_id = " + str(search_id[0])
            cur.execute(users_items)
            users_items = cur.fetchall()
            items = []
            for item in users_items:
                item_name = "SELECT name FROM Item WHERE id = "+str(item[0])
                item_price = "SELECT max_price FROM Item WHERE id = "+str(item[0])
                cur.execute(item_name)
                item_name = cur.fetchall()
                cur.execute(item_price)
                item_price = cur.fetchall()
                item_price = item_price[0][0]
                item_name = item_name[0][0]
                items.append(search_item(myItem(item_name, item_price)))

            send_email(items, user[3])


