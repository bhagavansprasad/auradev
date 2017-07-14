import logging
import logging.handlers

LOG_FILENAME = '/tmp/logging_rotatingfile_example.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20, backupCount=5)

handler.setLevel(logging.CRITICAL)

my_logger.addHandler(handler)
my_logger.debug("Message with %s, %s", "test string1", "test string2")
