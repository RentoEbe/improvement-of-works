# We operate the table of thawing in movixdb.db
import sqlite3

def save_data_of_thawing_in_database(db_pass, date, weekday, loaf, sausage):
    con = sqlite3.connect(db_pass)
    cursor = con.cursor()
    create_thawing_table_query = """
    CREATE TABLE IF NOT EXISTS Thawing(date INTEGER PRIMARY KEY NOT NULL, Weekday INTEGER, Loaf INTEGER,  Sausage INTEGER);
    """
    insert_thawing_query = "INSERT INTO Thawing VALUES (?, ?, ?, ?)"


    try:
        cursor.execute(create_thawing_table_query)
        cursor.execute(insert_thawing_query, (date, weekday, loaf, sausage))
    except sqlite3.Error as e:
        print("sqlite3 error occured", e)
        con.rollback() #commit前のpendingのsql文を無かったことにする(元の状態に戻す)
    else:
        con.commit()

