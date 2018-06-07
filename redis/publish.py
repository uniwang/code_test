import redis
import time
r = redis.Redis(host='10.242.130.157')
while True:
    time.sleep(1)
    r.publish('test1', 'hello')
    r.publish('test2', 'world')
    r.publish('foo', 'msg from foo')
    r.publish('foo1', 'msg from foo1')
    r.publish('foo2', 'msg from foo2')
    r.publish('bar', 'msg from bar')
    r.publish('bar2', 'msg from bar2')
    r.publish('bar3', 'msg from bar3')
    r.publish('foobar', 'msg from foobar')
    r.publish('foobar2', 'msg from foobar2')
    r.publish('foobar3', 'msg from foobar3')