import logging
import logging.config
import inspect


class customLogger():

    def log_utility(loglevel=logging.DEBUG):
        # Mention logger name
        loggername = inspect.stack()[1][3]
        # Create logger instance
        logger = logging.getLogger(loggername)
        # Set log level (info/warn/error etc)
        logger.setLevel(loglevel)

        # Step2: create console and set level
        lhandler = logging.FileHandler("logs.txt","a+")
        lhandler.setLevel(loglevel)

        # Step3: define message format
        formatter = logging.Formatter('%(name)s: %(asctime)s: %(levelname)s: %(message)s\n\r',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        # Step4: assign formatter to console
        lhandler.setFormatter(formatter)

        # Step5: assign console to logger
        logger.addHandler(lhandler)
        return logger







