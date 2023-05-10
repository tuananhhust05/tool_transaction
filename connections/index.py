from mysql.connector import Error
from mysql.connector import pooling
from models.transaction import Transaction
connection_pool = pooling.MySQLConnectionPool(    
                                                  pool_name="defaultdb",
                                                  pool_size=32,
                                                  pool_reset_session=True,
                                                  host='transaction-settelement-do-user-14024736-0.b.db.ondigitalocean.com',
                                                  port = 25060,
                                                  database='defaultdb',
                                                  user='doadmin',
                                                  password='AVNS_1idCLtitiPObeaO1A5s'
                                            )

connection_object = connection_pool.get_connection()

def ConnectToBase():
    if connection_object.is_connected():
        print("Connected")
        return connection_object
    else:
        return False