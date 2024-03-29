from connections.index import ConnectToBase
from models.transaction import Transaction
import datetime
from apscheduler.schedulers.background import BlockingScheduler

import pymysql
from models.transaction import Transaction
import mysql 

sched = BlockingScheduler(timezone="Asia/Bangkok")
# Thứ 7 và chủ nhật không chuyển 
# Không chuyển vào số phút chia 7 dư 6 và chia hết cho 1 => cách từ 2 đến 4 phút 
db = mysql.connector.connect(pool_name="ecom",pool_size=10,pool_reset_session=True,host='localhost',database='ecom',user='root',password='123456')

def ChangeStatus(obj,time):
    print("Change Status")
    db2 = mysql.connector.connect(pool_name='ecom')
    print("Connection db:", db2.connection_id)
    cursor2 = db2.cursor()
    print('ChangeStatus')
    cursor2.execute("UPDATE ecom.transaction SET  status ='settled' WHERE id = " + str(a))
    db2.commit()

    cursor2.execute("UPDATE ecom.transaction SET  status ='settled' WHERE id = " + str(obj.id))
    db2.commit()
    sql = "INSERT INTO ecom.result (id,created_at,time_change,type) VALUES (" +str(obj.id)+",'" +str(obj.created_at)+ "','" +str(time)+ "','"+ str(obj.type) +"')"
    
    cursor2.execute(sql)
    db2.commit()
    cursor2.close()
    db2.close()
    print("updated",obj.id)


def StartToolChangeStatusTransaction():
    connection = ConnectToBase()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM ecom.plan")
    cursor.execute("DELETE FROM ecom.result")
    connection.commit()
    print("Deleted test")

    cursor.execute("SELECT * FROM ecom.transaction ORDER BY created_at")
    record = cursor.fetchall()
    for e in record:
        obj = Transaction(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9])
        created_at = obj.created_at
        minute = created_at.minute
        remain = minute % 7 
        if (obj.type == "ATM_CARD"):
           time_add = 2
           if(remain == 4):
               time_add = time_add + 2
           if(remain == 5):
               time_add = time_add + 1
           time = created_at + datetime.timedelta(minutes=time_add)
           sql = "INSERT INTO ecom.plan (id,created_at,time_change,type) VALUES (" +str(obj.id)+",'" +str(created_at)+ "','" +str(time)+ "','ATM_CARD')"
           cursor.execute(sql)
           connection.commit()
           print("Inserted plan",obj.id)
           # schedule
           sched.add_job(ChangeStatus, 'date', run_date=time, args=[obj,time])
            
        if(obj.type == "CREDIT_CARD"):
            time_add = 6
            if(remain == 0): time_add = 8 
            if(remain == 1): time_add = 7
            time = created_at + datetime.timedelta(minutes=time_add)
            sql = "INSERT INTO ecom.plan (id,created_at,time_change,type) VALUES (" +str(obj.id)+",'" +str(created_at)+ "','" +str(time)+ "','CREDIT_CARD')"
            cursor.execute(sql)
            connection.commit()
            print("Inserted plan",obj.id)
            
            # schedule
            sched.add_job(ChangeStatus, 'date', run_date=time, args=[obj,time])
    sched.start()
            






        
