import datetime
import random
from connections.index import ConnectToBase
connection = ConnectToBase()

def VerifyMinuteSet():
    currentDateAndTime = datetime.datetime.now() # Đúng giờ GMT +7 
    currentminute= currentDateAndTime.minute
    startminute = ((currentminute//7) +1) * 7 + 3
    endminute = startminute + 6
    if(endminute >59):
        startminute = 1
        endminute = 7
    miniute_set = random.randint(startminute,endminute)
    return miniute_set

def ChooseTime():
    current = datetime.datetime.now()
    minute = VerifyMinuteSet()
    time_choose = current.replace(minute=minute, hour=current.hour, second=random.randint(0,59), year=current.year, month=current.month, day=current.day)
    millis = random.randint(0,59)
    time_choose = time_choose + datetime.timedelta(milliseconds=millis)
    if(minute <8):
        time_choose = time_choose + datetime.timedelta(hours=1)
    return time_choose

def InsertTransaction():
    cursor = connection.cursor()
    for i in range(4000):
        time = ChooseTime() 
        time = time + datetime.timedelta(days=-1)         
        sql = "INSERT INTO defaultdb.settlement (status,amount,fee_settlement,fee_refund,received_amount,settle_date,created_date,creator_id,stripe_id,type) VALUES ('pending',1,1,1,1,'" +str(time)+ "','" +str(time)+ "',1,1,'ATM_CARD')"
        cursor.execute(sql)
        connection.commit()
        print("Ineserted",i)
    for i in range(1000):
        i = 4000 + i
        time = ChooseTime()
        time = time + datetime.timedelta(days=-2) 
        sql = "INSERT INTO defaultdb.settlement (status,amount,fee_settlement,fee_refund,received_amount,settle_date,created_date,creator_id,stripe_id,type) VALUES ('pending',1,1,1,1,'" +str(time)+ "','" +str(time)+ "',1,1,'CREDIT_CARD')"
        cursor.execute(sql)
        connection.commit()
        print("Ineserted",i)
