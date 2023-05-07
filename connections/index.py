from mysql.connector import Error
from mysql.connector import pooling
from models.transaction import Transaction
connection_pool = pooling.MySQLConnectionPool(    
                                                  pool_name="ecom",
                                                  pool_size=32,
                                                  pool_reset_session=True,
                                                  host='localhost',
                                                  database='ecom',
                                                  user='root',
                                                  password='123456'
                                            )

connection_object = connection_pool.get_connection()

def ConnectToBase():
    if connection_object.is_connected():
        print("Connected")
        return connection_object
    else:
        return False