import threading
import time
import logging
import random
import Queue

logging.basicConfig(filename='fun_thread.out',
                    level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

BUF_SIZE = 100
q = Queue.Queue(BUF_SIZE) # built-in wait and notify

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1,10)
                q.put(item)
                logging.debug('Putting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                logging.debug('Getting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return

if __name__ == '__main__':

    c = [ConsumerThread(name='consumer'+str(i)) for i in range(20)]
    p = [ProducerThread(name='producer'+str(i)) for i in range(20)]

    combined = list(zip(c, p))
    combined = [_ for pair in combined for _ in pair]
    if len(c) > len(p):
        combined += c[len(p):]
    elif len(p) > len(c):
        combined += p[len(c):]

    for entity in combined:
        entity.start()
        time.sleep(0)
