import Queue
 
class Task(object):
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
        
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
 
q = Queue.PriorityQueue()
 
q.put( Task(100, 'a not agent task') )
q.put( Task(5, 'a highly agent task') )
q.put( Task(10, 'an important task') )
 
while not q.empty():
    cur_task = q.get()
    print 'process priority:', cur_task.priority
    print 'process task    :', cur_task.name
 
