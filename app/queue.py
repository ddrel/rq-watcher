from redis import Redis
from rq import Queue
from os import path
from app.module_extractcsv import extractcsv
from app.module_movefile import movefile
import os
from environs import Env

class redisQueue:
    env = Env()
    env.read_env()
    file_path=""
    isleapyear=False    
    q=object
    
    def __init__(self, path,isleapyear=False): 
        self.file_path = path
        self.isleapyear = isleapyear

    def connection(self,redis_conn):
        self.q = Queue(connection=redis_conn)

    def queue(self):
        print("queue >>> " + self.file_path)
        csv = extractcsv(self.file_path,isleapyear=self.isleapyear)
        job_csv = self.q.enqueue(csv.process,result_ttl=1,job_timeout="2h")

        dist_path = self.env.str("folder_processed")
        job_moved= self.q.enqueue(movefile,args=(self.file_path,dist_path), depends_on=job_csv,result_ttl=1,job_timeout="1h")
        return job_moved

    def lenght(self):
        return len(self.q)
