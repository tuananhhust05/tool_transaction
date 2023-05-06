from connections.index import ConnectToBase
connection = ConnectToBase()

def DeleteTransaction():
    cursor = connection.cursor()
    cursor.execute("DELETE FROM ecom.transaction")
    connection.commit()
    print("Deleted transaction")