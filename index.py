import mysql.connector
import datetime
from datetime import date
from apscheduler.schedulers.background import BlockingScheduler
import mysql 
import redis
from datetime import date

# env 
import os
from dotenv import load_dotenv
load_dotenv()
host = os.environ.get('HOST')
print(host)


sched = BlockingScheduler(timezone="Asia/Ho_Chi_Minh")
db = mysql.connector.connect(                     
                                pool_name=os.environ.get('pool_name'),
                                pool_size=int(os.environ.get('pool_size')),
                                pool_reset_session=bool(os.environ.get('pool_reset_session')),
                                host=os.environ.get('host'),
                                port = int(os.environ.get('port')),
                                database=os.environ.get('database'),
                                user=os.environ.get('user'),
                                password=os.environ.get('password')
                            )
print("Init connection")

r = redis.Redis(host='localhost', port=6379, db=1)
print('Conneced redis')

class Transaction:
    def __init__ (self, id,status,amount,fee_settlement,fee_refund,received_amount,settle_date,created_date,creator_id,stripe_id,type):
        self.id = id
        self.status = status
        self.amount = amount
        self.fee_settlement = fee_settlement
        self.fee_refund = fee_refund
        self.received_amount = received_amount
        self.settle_date = settle_date
        self.created_date = created_date
        self.creator_id = creator_id
        self.stripe_id = stripe_id
        self.type = type 

day_atm = int(os.environ.get('day_atm'))
day_credit = int(os.environ.get('day_credit'))

def StartToolChangeStatusTransaction():
    today = date.today()
    week_day = today.weekday() + 2
    if(week_day <7):
        connection = mysql.connector.connect(pool_name='defaultdb')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM defaultdb.plan")
        cursor.execute("DELETE FROM defaultdb.result")
        connection.commit()
        print("Deleted test")

        cursor.execute("SELECT * FROM defaultdb.settlement ORDER BY created_date")
        record = cursor.fetchall()
        for e in record:
            obj = Transaction(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10])
            created_at = obj.created_date 

            if (obj.type == "ATM_CARD"):
                time = created_at + datetime.timedelta(days=day_atm)
                sql = "INSERT INTO defaultdb.plan (id,created_date,time_change,type) VALUES (" +str(obj.id)+",'" +str(created_at)+ "','" +str(time)+ "','ATM_CARD')"
                cursor.execute(sql)
                connection.commit()
                print("Inserted plan",obj.id)
                if(time.day == datetime.datetime.now().day):
                   cursor.execute("UPDATE defaultdb.settlement SET  status ='settled', settle_date='"+ str(time)+"' WHERE id = " + str(obj.id))
                   connection.commit()
                   r.set(str(obj.id), 'True') 
                
            if(obj.type == "CREDIT_CARD"):
                time = created_at + datetime.timedelta(days=day_credit)
                sql = "INSERT INTO defaultdb.plan (id,created_date,time_change,type) VALUES (" +str(obj.id)+",'" +str(created_at)+ "','" +str(time)+ "','CREDIT_CARD')"
                cursor.execute(sql)
                connection.commit()
                print("Inserted plan",obj.id)
                if(time.day == datetime.datetime.now().day):
                   cursor.execute("UPDATE defaultdb.settlement SET  status ='settled', settle_date='"+ str(time)+"' WHERE id = " + str(obj.id))
                   connection.commit()
                   r.set(str(obj.id), 'True') 
        cursor.close()
        connection.close()
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
                    time = created_at + datetime.timedelta(days=day_atm)
                    if(time.day == datetime.datetime.now().day):
                        if(obj.status == 'pending'):
                                cursor.execute("UPDATE defaultdb.settlement SET  status ='settled', settle_date='"+ str(time)+"' WHERE id = " + str(obj.id))
                                connection.commit()
                                print('remain')
                r.delete(str(obj.id))
                
            if(obj.type == "CREDIT_CARD"):
                if(r.get(str(obj.id)) == None):
                    time = created_at + datetime.timedelta(days=day_credit)
                    if(time.day == datetime.datetime.now().day):
                        if(obj.status == 'pending'):
                                cursor.execute("UPDATE defaultdb.settlement SET  status ='settled', settle_date='"+ str(time)+"' WHERE id = " + str(obj.id))
                                connection.commit()
                                print('remain')
                r.delete(str(obj.id)) 
    cursor.close()
    connection.close()
sched.add_job(StartToolChangeStatusTransaction, 'cron', hour= 21, minute= '21')
sched.add_job(updateMiss, 'cron', hour= 17, minute= '15')
sched.start()







