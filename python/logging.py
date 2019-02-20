# ref https://www.youtube.com/watch?v=g8nQ90Hk328&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=17
# simple logging so no need to print this and that ! : ) 
# just change level to WANRING/INFO after Dev/Test, then will log fine

import logging

# create and config logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="D:\\github\\walter-repo\\Python\\Lumberjack.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = "a")

logger = logging.getLogger()

'''
logger.info("test logger first message")
print(logger.level)
logger.info("test logger 2nd  message")

# 5 logging levels below: 
logger.debug("this is debug test message")
logger.info("this is info test messgae")
logger.warning("This is warning test")
logger.error("this is error level")
logger.critical("this is critical")
'''

def test(a,b,c):
    sum = a + b + c
    logger.info("input arguments to function test({0},{1},{2})".format(a,b,c))
    logger.info("return result is sum = {0}".format(sum))
    return sum

logging.debug("before calling test function")
a = test(1,2,3)
print(a)
