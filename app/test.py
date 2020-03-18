from redis import Redis
from queue import redisQueue
from module_movefile import movefile

''' 
rq = redisQueue("/home/darel/app/redis-queue/era5land_at_metars_2018.nc")
rq.connection(Redis()) 
print(rq.lenght())
rq.queue()


rq = redisQueue("/home/darel/app/redis-queue/era5land_at_metars_2017.nc")
rq.connection(Redis()) 
print(rq.lenght())
rq.queue()

rq = redisQueue("/home/darel/app/redis-queue/era5land_at_metars_2016.nc")
rq.connection(Redis()) 
print(rq.lenght())
rq.queue()

rq = redisQueue("/home/darel/app/redis-queue/era5land_at_metars_2015.nc")
rq.connection(Redis()) 
print(rq.lenght())
rq.queue()
'''

def qt(path):
    rq = redisQueue(path)
    rq.connection(Redis()) 
    print(rq.lenght())
    rq.queue()