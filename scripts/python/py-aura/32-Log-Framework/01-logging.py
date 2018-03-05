import logging
import logging.handlers

LOG_FILENAME = '/tmp/temp.log'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=100, backupCount=5)

my_logger.addHandler(handler)
my_logger.debug("Message with %s, %s", "test string1", "test string2")
