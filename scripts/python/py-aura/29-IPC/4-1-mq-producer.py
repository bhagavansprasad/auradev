# producer.py
from baseplate.message_queue import MessageQueue

# If the queue doesn't already exist, we'll create it.
mq = MessageQueue("/baseplate-testing", max_messages=5, max_message_size=10)
message = "hai"
print(("Put Message: %s" % message))
mq.put(message)
