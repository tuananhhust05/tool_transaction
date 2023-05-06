from connections.index import ConnectToBase
from models.transaction import Transaction
from models.result import Result
import datetime


def StartTestResult():
    connection = ConnectToBase()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM ecom.transaction")
    record_transaction = cursor.fetchall()
    record_transaction_dict = []
    for e in record_transaction:
        record_transaction_dict.append(Transaction(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9]))
    
    cursor.execute("SELECT * FROM ecom.result")
    record_result = cursor.fetchall()
    record_result_dict = []
    for e in record_result:
        record_result_dict.append(Result(e[0],e[1],e[2]))
    
    count_true = 0
    count_false = 0
    for obj in record_transaction_dict:
        plan = []
        for e in record_result_dict:
            if( e.id == obj.id):
                plan.append(e)
        if(len(plan) > 0) :
            result_ele = plan[0]
            time_result_change = result_ele.time_change
            time_insert = obj.created_at
            remain_created = time_insert.minute % 7

            if(obj.type == 'ATM_CARD'):
                time_add = 2
                if(remain_created == 4): time_add= 4
                if(remain_created == 5): time_add= 3
                
                if( time_insert + datetime.timedelta(minutes=time_add) == time_result_change):
                    count_true = count_true + 1
                else:
                    count_false = count_false + 1

            if(obj.type == 'CREDIT_CARD'):
                time_add = 6
                if(remain_created == 0): time_add = 8 
                if(remain_created == 1): time_add = 7
                
                if( time_insert + datetime.timedelta(minutes=time_add) == time_result_change):
                    count_true = count_true + 1
                else:
                    count_false = count_false + 1

        else:
            count_false = count_false + 1

    exact_rate = count_true / (count_true + count_false) * 100
    print(count_true,count_false)
    print('exact_rate result',exact_rate)