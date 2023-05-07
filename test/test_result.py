from connections.index import ConnectToBase
from models.transaction import Transaction
from models.result import Result
import datetime

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

def StartTestResult():
    connection = ConnectToBase()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM ecom.transaction")
    record_transaction = cursor.fetchall()
    record_transaction_dict = []
    converted_transaction = 0
    for e in record_transaction:
        obj = Transaction(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9])
        if(obj.status == "settled"): 
            converted_transaction = converted_transaction + 1
        record_transaction_dict.append(obj)
    
    cursor.execute("SELECT * FROM ecom.result")
    record_result = cursor.fetchall()
    record_result_dict = []

    time_current_true = 0
    time_difference_average = 0 
    time_difference_sum = 0 
    count_diff = 0
    for e in record_result:
        record_result_dict.append(Result(e[0],e[1],e[2],e[4]))
        if(e[2] == e[4]): 
            time_current_true = time_current_true + 1
        else: 
            difference = e[4] - e[2]
            time_difference_sum = time_difference_sum + difference.total_seconds()
            count_diff = count_diff + 1
    if (count_diff != 0): time_difference_average= time_difference_sum / count_diff
    print('số lịch sử ghi nhận',len(record_result))
    print('tỷ lệ ghi nhận lịch sử',len(record_result) /len(record_transaction) * 100 )
    print('số transaction chuyển đổi đúng hạn',time_current_true)
    print('tỷ lệ transaction chuyển đổi đúng theo kế hoạch trên tổng số transaction',time_current_true/len(record_transaction) * 100)
    print('độ lệch trung bình những transaction có lịch sử nhưng sai thời gian thực thi',time_difference_average,'giây')
    print('số transaction đã convert',converted_transaction)