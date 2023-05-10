from connections.index import ConnectToBase
from models.transaction import Transaction
import datetime
from apscheduler.schedulers.background import BlockingScheduler
from models.transaction import Transaction
import mysql 
import redis
sched = BlockingScheduler(timezone="Asia/Ho_Chi_Minh")

db = mysql.connector.connect(                     
                                pool_name="defaultdb",
                                pool_size=32,
                                pool_reset_session=True,
                                host='transaction-settelement-do-user-14024736-0.b.db.ondigitalocean.com',
                                port = 25060,
                                database='defaultdb',
                                user='doadmin',
                                password='AVNS_1idCLtitiPObeaO1A5s'
                            )
print("Init connection")
r = redis.Redis(host='localhost', port=6379, db=1)
print("Init connection redis")
def updateMiss():
    print("update miss")
    connection = mysql.connector.connect(pool_name='defaultdb')
    print("Connection db:", connection.connection_id)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM defaultdb.settlement ORDER BY created_date")
    record = cursor.fetchall()
    for e in record:
            print(e[0])
            obj = Transaction(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10])
            created_at = obj.created_date 

            if (obj.type == "ATM_CARD"):
                if(r.get(str(obj.id)) == None):
                    time = created_at + datetime.timedelta(days=1)
                    if(time.day == datetime.datetime.now().day):
                        if(obj.status == 'pending'):
                                cursor.execute("UPDATE defaultdb.settlement SET  status ='settled', settle_date='"+ str(time)+"' WHERE id = " + str(obj.id))
                                connection.commit()
                                print('remain')
                r.delete(str(obj.id))
                
            if(obj.type == "CREDIT_CARD"):
                if(r.get(str(obj.id)) == None):
                    time = created_at + datetime.timedelta(days=1)
                    if(time.day == datetime.datetime.now().day):
                        if(obj.status == 'pending'):
                                cursor.execute("UPDATE defaultdb.settlement SET  status ='settled', settle_date='"+ str(time)+"' WHERE id = " + str(obj.id))
                                connection.commit()
                                print('remain')
                r.delete(str(obj.id)) 
    cursor.close()
    connection.close()

sched.add_job(updateMiss, 'cron', hour= 17, minute= '17')
            
sched.start()