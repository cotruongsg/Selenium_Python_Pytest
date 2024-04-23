import logging

class LoggerDemoConsole():
    def testlog(self):
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        hler = logging.StreamHandler()
        hler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s' , 
                    datefmt='%m/%d/%Y %H:%M:%S %p')
        
        hler.setFormatter(formatter)

        logger.addHandler(hler)

        logger.debug('Debug message')
        logger.warning("warning message")
        logger.info("info message")
        logger.error("error message")

demo = LoggerDemoConsole()
demo.testlog()