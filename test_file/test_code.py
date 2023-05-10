# import datetime
# from datetime import date
# today = date.today()
 
# print("hôm nay là ngày thứ", today.weekday() + 2, "trong tuần")
# print(datetime.datetime.now().day)
from apscheduler.schedulers.background import BlockingScheduler
sched = BlockingScheduler(timezone="Asia/Ho_Chi_Minh")
def StartToolChangeStatusTransaction():
    print('start')
sched.add_job(StartToolChangeStatusTransaction, 'cron', hour= 15, minute= '47')
sched.start()