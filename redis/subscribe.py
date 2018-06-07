import redis

r = redis.Redis(host='10.242.130.157')

p = r.pubsub()
p.subscribe(['test1', 'test2', 'test3'])
p.psubscribe(['foo*', 'bar?', 'foobar+'])

for item in p.listen():
    # if item['type'] == 'pmessage' or item['type'] == 'message':
    #     print "channel:%s,data:%s"%(item['channel'],item['data'])
    print item
