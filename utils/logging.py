import logging
from logging.handlers import TimedRotatingFileHandler

class Log():
 
   # create logger
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)

   # creating a file handler and setting level to debug
    fileHandler = TimedRotatingFileHandler('API.LOG',backupCount = 7, when='D', interval=2)
    fileHandler.setLevel(logging.DEBUG)


    # create  and set formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)
    # add fileHander to logger
    log.addHandler(fileHandler)