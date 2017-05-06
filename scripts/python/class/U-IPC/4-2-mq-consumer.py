# consumer.py
from baseplate.message_queue import MessageQueue

mq = MessageQueue("/baseplate-testing", max_messages=1, max_message_size=1)
# Unless a `timeout` kwarg is passed, this will block until
# we can pop a message from the queue.
message = mq.get()
print("Get Message: %s" % message)
