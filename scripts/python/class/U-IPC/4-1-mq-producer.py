# producer.py
from baseplate.message_queue import MessageQueue

# If the queue doesn't already exist, we'll create it.
mq = MessageQueue("/baseplate-testing", max_messages=1, max_message_size=1)
message = "1"
mq.put(message)
print("Put Message: %s" % message)
