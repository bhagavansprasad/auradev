# consumer.py
from baseplate.message_queue import MessageQueue

mq = MessageQueue("/test4", max_messages=5, max_message_size=3)
# Unless a `timeout` kwarg is passed, this will block until
# we can pop a message from the queue.

while True:
	message = mq.get()
	print("Get Message: %s" % message)
