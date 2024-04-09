#Use of custom_logger file is shown here

import logging
#import logging_pratice.custom_logger as cl
from logging_pratice import custom_logger_02 as cl

class logging_demo():
#By importing below line we can directly got the log as a new file from custom_logger file
#here custom logger is defiend as class level so one file all logs will come
    logtest=cl.customLogger(logging.DEBUG)

    def method1(self):
        self.logtest.debug("Debug message")
        self.logtest.error("Error message")
        self.logtest.info("Information message")
        self.logtest.warning("Warning message")
        self.logtest.critical("Critical message")

    def method2(self):
        #Here custom logger is defiend as method level
        m2log=cl.customLogger(logging.INFO)

        m2log.debug("Debug message")
        m2log.error("Error message")
        m2log.info("Information message")
        m2log.warning("Warning message")
        m2log.critical("Critical message")

    def method3(self):
        m3log=cl.customLogger(logging.INFO)

        m3log.debug("Debug message")
        m3log.error("Error message")
        m3log.info("Information message")
        m3log.warning("Warning message")
        m3log.critical("Critical message")

demo=logging_demo()
demo.method1()
demo.method2()
demo.method3()
