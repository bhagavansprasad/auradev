import time
# producer.py
from baseplate.message_queue import MessageQueue

# If the queue doesn't already exist, we'll create it.
mq = MessageQueue("/test4", max_messages=5, max_message_size=3)

i = 1

while True:
    message = str(i) 
    mq.put(message)
    print("Put Message: %s" % message)
    i += 1
    #time.sleep(1)
