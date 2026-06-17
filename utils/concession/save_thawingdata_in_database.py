# We save data of thawing in database
import sqlite3

def save_data_of_thawing_in_database(date, weekday, loaf, sausage):
    con = sqlite3.connect("../../database/movixdb.db")
    cursor = con.cursor()
    create_thawing_table_query = """
    CREATE TABLE IF NOT EXISTS Thawing(date INTEGER PRIMARY KEY NOT NULL, Weekday INTEGER, Loaf INTEGER,  Sausage INTEGER);
    """
    insert_thawing_query = "INSERT INTO Sample VALUES (?, ?, ?, ?)"


    try:
        cursor.execute(create_thawing_table_query)
        cursor.execute(insert_thawing_query, (date, weekday, loaf, sausage))
    except sqlite3.Error as e:
        print("sqlite3 error occured", e)
        con.rollback() #commit前のpendingのsql文を無かったことにする(元の状態に戻す)
    else:
        con.commit()


save_data_of_thawing_in_database(20261023, 3, 3, 4)