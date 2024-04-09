import logging
#default format
#logging.error("error message")

#Updated format
logging.basicConfig(format="%(levelname)s: %(message)s",level=logging.DEBUG)
logging.error("Formated error message")
logging.warning("Warning message")

#If we want to print in a file
#logging.basicConfig(filename="format_logs",format="%(levelname)s: %(message)s",level=logging.DEBUG)
