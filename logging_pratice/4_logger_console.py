import logging

class LoggerConsoleDemo():
    def consolelogger(self):
    #Create  a logger
        #logger=logging.getLogger('sample_log')  #---> gives same log name
        #oR #Below code will give class name INSTEAD OF GIVEN NAME
        logger=logging.getLogger(LoggerConsoleDemo.__name__)
        logger.setLevel(logging.ERROR)

        #Create a console handler and set the level
        consolehandler=logging.StreamHandler()
        consolehandler.setLevel(logging.ERROR)

        # Creat a formatter

        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

        #Add formatter to console
        consolehandler.setFormatter(formatter)

        # Add the formatter to logger
        logger.addHandler(consolehandler)

        # logging message
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")
log1=LoggerConsoleDemo()
log1.consolelogger()