import watchdog.events 
import watchdog.observers 
import time 
from os import path
from environs import Env
from redis import Redis
from app.queue import redisQueue


basepath = path.dirname(__file__)
src_path = path.join(basepath, "app","folder_pass")


class Handler(watchdog.events.PatternMatchingEventHandler): 
    def __init__(self): 
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.nc'], 
                                                             ignore_directories=True, case_sensitive=False)   
    def on_created(self, event):         
        print("Watchdog received created event - % s." % event.src_path)
        rq = redisQueue(event.src_path)
        rq.connection(Redis()) 
        print(rq.lenght())
        rq.queue()

    def on_modified(self, event): 
        print("Watchdog received modified event - % s." % event.src_path) 
         
    def on_moved(self, event): 
        print("Watchdog received moved event - % s." % event.src_path) 
                
    def on_deleted(self, event): 
        print("Watchdog received deleted event - % s." % event.src_path) 



if __name__ == "__main__":   
    event_handler = Handler() 
    observer = watchdog.observers.Observer() 
    observer.schedule(event_handler, path=src_path, recursive=False) 
    observer.start() 
    try: 
        while True: 
            time.sleep(1) 
    except KeyboardInterrupt: 
        observer.stop() 
    observer.join() 