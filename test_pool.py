from mysql.connector import Error
from mysql.connector import pooling
from apscheduler.schedulers.background import BlockingScheduler
import random
import mysql
from models.transaction import Transaction
import datetime
sched = BlockingScheduler(timezone="Asia/Bangkok")
current = datetime.datetime.now()
db1 = mysql.connector.connect(pool_name="ecom",pool_size=10,pool_reset_session=True,host='localhost',database='ecom',user='root',password='123456')
cursor = db1.cursor()
sql = "SELECT * FROM ecom.transaction WHERE id IN (SELECT id FROM ecom.plan WHERE time_change < '"+ str(current) +"') AND status='pending'"
print(sql)
cursor.execute(sql)
transactions = cursor.fetchall()
print(len(transactions))
# transaction_dict = []
# for e in transaction:
#         transaction_dict.append(Transaction(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9]))

