import redis

r = redis.Redis(host='localhost', port=6379, db=1)
# a=1 
# r.set('hello', 'world') 
# r.set('hello2', 'world') 
# r.set(str(a), 'True') 
# print(r.get('1'))
# value = r.get('hello')
# arr_id = []
# def CheckContain(id):
#     for ele in arr_id:
#         if(str(ele) == str(id)):
#             return 1
#     return 0 

for key in r.keys():
    id = key.decode("utf-8")
    print(id)
    # r.delete(id)
    # arr_id.append(id)
print(len(r.keys()))
# print(CheckContain(1))


# print(r.get('hello')) 
# print(r.get('1'))
# check = r.get('1')
# if(r.get('1') == None):
#     print('0')
