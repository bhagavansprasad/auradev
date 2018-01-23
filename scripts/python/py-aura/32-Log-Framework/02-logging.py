import logging
import sys

'''
Level	Numeric value
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0
'''

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug   ('1. This is a debug message')
logging.info    ('2. This is an info message')
logging.warning ('3. This is a warning message')
logging.error   ('4. This is an error message')
logging.critical('5. This is a critical error message')
