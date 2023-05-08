from connections.index import ConnectToBase
from models.transaction import Transaction
import datetime
from apscheduler.schedulers.background import BlockingScheduler
from models.transaction import Transaction
import mysql 

sched = BlockingScheduler(timezone="Asia/Ho_Chi_Minh")

db = mysql.connector.connect(pool_name="ecom",pool_size=32,pool_reset_session=True,host='localhost',database='ecom',user='root',password='123456')
print("Init connection")

def updateMiss():
    print("update miss")
    current = datetime.datetime.now()
    db3 = mysql.connector.connect(pool_name='ecom')
    print("Connection db:", db3.connection_id)
    cursor3 = db3.cursor()

    sql2 = "SELECT * FROM ecom.transaction WHERE id IN (SELECT id FROM ecom.plan WHERE time_change < '"+ str(current) +"') AND status='pending'"
    cursor3.execute(sql2)
    transactions = cursor3.fetchall()
    print('len transactions',len(transactions))
    for e in transactions:
        cursor3.execute("UPDATE ecom.transaction SET  status ='settled' WHERE id = " + str(e[0]))
        db3.commit()
        new_obj = Transaction(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9])
        print(new_obj)
        
        sql = "INSERT INTO ecom.result (id,created_at,time_change,type,time_current) VALUES (" +str(new_obj.id)+",'" +str(new_obj.created_at)+ "','" +str(current)+ "','"+ str(new_obj.type) +"','"+ str(current) +"')"
        cursor3.execute(sql)
        db3.commit()
    cursor3.close()
    db3.close()

sched.add_job(updateMiss, 'interval', seconds=20)
            
sched.start()