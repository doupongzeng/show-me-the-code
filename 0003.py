import redis
import string
import random

r= redis.Redis(host='localhost', port=6379, decode_responses=True)

base_str = string.ascii_letters+string.digits

for i in range(20):
    #random.sample 返回 list，所以要组合成一个字符串
    #利用join对一个可迭代对象进行插入指定字符
    ss = ''.join(random.sample(base_str, 12))
    r.set('name'+str(i), ss)

for i in range(20):
    print('name'+str(i)+': ' + r.get('name'+str(i)))