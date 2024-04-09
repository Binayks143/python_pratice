"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""

import logging

#logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s")
#logging.error("This is error")

#Changing the logs time formate
logging.basicConfig(format="%(asctime)s : %(message)s",
                    datefmt='%d-%m-%Y %H:%M:%S')

#%p for am and pm

logging.warning("This is Warning")