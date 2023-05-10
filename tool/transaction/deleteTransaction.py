from connections.index import ConnectToBase
connection = ConnectToBase()

def DeleteTransaction():
    cursor = connection.cursor()
    cursor.execute("DELETE FROM defaultdb.settlement")
    connection.commit()
    print("Deleted transaction")