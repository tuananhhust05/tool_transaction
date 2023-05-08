from mysql.connector import Error
from mysql.connector import pooling
from apscheduler.schedulers.background import BlockingScheduler
import random
import mysql
sched = BlockingScheduler(timezone="Asia/Bangkok")

db1 = mysql.connector.connect(pool_name="ecom",pool_size=10,pool_reset_session=True,host='localhost',database='ecom',user='root',password='123456')
cursor = db1.cursor()
def ChangeStatus():
   print("Change Status")
   #print(connection_pool.__dict__)
   db2 = mysql.connector.connect(pool_name='ecom')
   print("Connection db2:", db2.connection_id)
   
   cursor = db2.cursor()
   print('ChangeStatus')
   a = random.randint(10,499)
   cursor.execute("UPDATE ecom.transaction SET  status ='settled' WHERE id = " + str(a))
   db2.commit()

   cursor.close()
   db2.close()
   print("updated",a)

sched.add_job(ChangeStatus, 'interval', seconds=0.01)
            
sched.start()
