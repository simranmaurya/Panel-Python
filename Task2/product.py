import sqlite3

CREATE_TABLE_QUERY = "CREATE TABLE if not exists product_table (Product TEXT,Quantity INT,Price INT);"
INSERT_INTO_TABLE_QUERY = "INSERT INTO product_table VALUES (?,?,?);"
SELECT_ALL_QUERY = "SELECT * from product_table;"
# GET_COLUMN_QUERY = "PRAGMA table_info(Student);"

pdata = [('Purse',1,500),
         ('Belt',2,100),
         ('Watch',1,400),
         ('Boot',3,400)]

# connection = sqlite3.connect("data.db")
# cursor = connection.cursor()
# cursor.execute(CREATE_TABLE_QUERY)
# cursor.executemany(INSERT_INTO_TABLE_QUERY,pdata)
# data = cursor.execute(SELECT_ALL_QUERY).fetchall()
# # print(data)
# connection.close()

def connect():
    return sqlite3.connect("data.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE_QUERY)

def insert_val(connection):
    with connection:
        connection.executemany(INSERT_INTO_TABLE_QUERY,pdata)

def get_all(connection):
    with connection:
        return connection.execute(SELECT_ALL_QUERY).fetchall()

# def get_columns(connection):
#     with connection:
#         connection.row_factory = sqlite3.Row
#         cursor = connection.execute('select * from product_table')
#         row = cursor.fetchone()
#         names = row.keys()
#         return names

def disconnect(connection):
    connection.close()
