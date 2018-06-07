# encoding:utf-8
#To have launchd start redis now and restart at login: brew services start redis
#Or, if you don't want/need a background service you can just run: redis-server /usr/local/etc/redis.conf
# import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# r.set('name', 'junxi')
# print(r['name'])
# print(r.get('name'))
# print(type(r.get('name')))


# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(connection_pool=pool)
# r.set('name1', 'junxii')
# print(r['name1'])
# print(r.get('name1'))
# print(type(r.get('name1'))
#!/usr/local/bin/python                                                             
                                                                                    
import redis                                                                        
import time                                                                         
                                                                                    
class RedisQueue(object):                                                           
    def __init__(self, name, namespace, **redis_args):                              
        self.key = "%s:%s" % (namespace, name)                                      
        self.__db = redis.Redis(**redis_args)                                       
                                                                                    
    def qsize(self):                                                                
        return self.__db.llen(self.key)                                             
                                                                                    
    def empty(self):                                                                
        return self.qsize() == 0                                                    
                                                                                    
    def get(self, block=True, timeout=None):                                        
        if block:                                                                   
            item = self.__db.blpop(self.key, timeout=timeout)                       
        else:                                                                       
            item = self.__db.lpop(self.key)                                         
                                                                                    
        if item:                                                                    
            item = item[1]                                                          
        return item                                                                 
                                                                                    
    def put(self, item):                                                            
        self.__db.rpush(self.key, item)                                             
                                                                                    
    def get_nowait(self):                                                           
        return self.get(False)                                                      
                                                                                    
                                                                                    
r = RedisQueue('test', "liyang")                                                    
begin = time.clock()                                                                
for i in range(0, 100000):      
    r.put(str(i))                                                                
end = time.clock()                                                               
print end-begin                                                                  
                                                                                 
begin = time.clock()                                                             
for i in range(0, 100000):                                                       
    a = r.get()                                                                  
end = time.clock()                                                               
print end-begin