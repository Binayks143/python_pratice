#importing required packages
from datetime import datetime
import inspect
import logging
#from logging.handlers import RotatingFileHandler
from concurrent_log_handler import ConcurrentRotatingFileHandler as crf

#Configuring the log file name
file_name=r'G:\logs\vAnalytics_'
file_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
my_path = file_name+file_time

#defining the logger function and default log level is DEBUG
def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logLevel)

    #this line helps to generate multiple log files when the log file limit exceeds 20mb
    my_handler = crf("{0}.log".format(my_path), mode='a', maxBytes=20*1024*1024)
    my_handler.setLevel(logLevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s- %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    my_handler.setFormatter(formatter)
    logger.addHandler(my_handler)
    return logger