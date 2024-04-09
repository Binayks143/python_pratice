import logging
import logging.config

class FileConfig():
    def file(self):
        # lOAD THE CONFIG FILE extension must be .conf
        logging.config.fileConfig("logging.conf")

        #create logger
        logger=logging.getLogger(FileConfig.__name__)

        #logging message
        logger.debug("Debug message")
        logger.error("This is error message")
        logger.critical("Critical message")


f1=FileConfig()
f1.file()

