import logging
import os

class customLogger:
    def __init__(self,name=__name__):
        self.__name = name
        self.logger = logging.getLogger(self.__name)
        self.logger.setLevel(logging.DEBUG)
        log_path = os.path.dirname(os.path.abspath(__file__))
        logname = log_path +'/'+'excuting.log'
        fh = logging.FileHandler(logname,mode='w',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    @property
    def log_utility(self):
        return self.logger

    # def log_utility(loglevel=logging.DEBUG):
        # # Mention logger name
        # loggername = inspect.stack()[1][3]
        # # Create logger instance
        # logger = logging.getLogger(loggername)
        # # Set log level (info/warn/error etc)
        # logger.setLevel(loglevel)
        #
        # # Step2: create console and set level
        # lhandler = logging.FileHandler("logs.txt","a+")
        # lhandler.setLevel(loglevel)
        #
        # # Step3: define message format
        # formatter = logging.Formatter('%(name)s: %(asctime)s: %(levelname)s: %(message)s\n\r',
        #                               datefmt='%m/%d/%Y %I:%M:%S %p')
        # # Step4: assign formatter to console
        # lhandler.setFormatter(formatter)
        #
        # # Step5: assign console to logger
        # logger.addHandler(lhandler)
        # return logger







