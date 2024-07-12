#!/usr/bin/env python
# coding: utf-8

import logging
import math
from datetime                          import timedelta, datetime

from Values              import *

"""
This class is used to load a logger to format the output and enrich it
with standard information.

Since every script needs to utilitze at most one logger, this class is
a singleton.

Examples for all configuration possibilities of the logger the content 
of the logger configuration file:

"name": "execute"
"format": "[%(levelname)-8s] %(asctime)s: %(message)s"
"date_format": "%Y/%m/%d %H:%M:%S"
"level": "INFO"
  
How to use:

->  First: execute createLogger(...) to create the logger.
->  Second: execute getLogger(...) to get the logger.
"""
class Logger:
    
    # The unique logger.
    log = None

    # The logger of this object.
    logger = None
    
    # Which percent-period is used between printing the progress e.g. every FIVE
    # percent a print will be done.
    printPercentPeriod = FIVE / HUNDRED

    # This variables are used to print a progressbar. To do so see 
    # startPrintProgress(...) and printProgress(...).
    printProgressAmount = -1
    printProgressTime = None
    printProgressIndex = -1

    """
    
    """
    @staticmethod
    def setSingletonLogger(logger = None):
        ret = ZERO

        if Logger.log is not None:
            ret = ONE
        
        Logger.log = logger

        return ret

    """
    
    """
    @staticmethod
    def getSingletonLogger():
        return Logger.log
    
    """
    This method sets the percent period in which a print will
    be done. Use this method before using printProgress, which is
    used to print the progress of a task.
    
    percent: a value strict between 0 and 1
    return: ZERO if everything went well
        ONE if percent is lower than zero
        TWO if percent is bigger than one
    """
    def setPrintPercentPeriod(self, percent: float = 0.01) -> int: 
        ret = ZERO
        
        if percent > ZERO:
            if percent < ONE:
                self.printPercentPeriod = percent
            else:
                ret = TWO
        else:
            ret = ONE
            
        return ret
    
    """
    Creates the logger which has been created from the configuration. 
    Please make sure that the configuration contains the default values 
    in case they have not been specified. The logger is also used in 
    other parts of model creation. 
    
    loggerName: the name of the logger. Usually 
        "__name__" is used.
    loggerFormat: the format of the output of logs.
    loggerDateFmt: the format of the date which
        will be printet out at every log.
    loggerLevel: the logging level of the logger e.g.
        "INFO", "DEBUG", "ERROR", "CRITICAL", "NOTSET", "WARN" etc.
    return: ZERO if everything went well
        -ONE if loggerName is None
        -TWO if loggerFormat is None
        -THREE if loggerDateFmt is None
        -FOUR if loggerLevel is None
    """ 
    def createLogger(self, loggerName: str= None, loggerFormat: str = None, 
        loggerDateFmt: str = None, loggerLevel: str = None) -> int:
        ret = ZERO
        
        if loggerName is None:
            ret = -ONE
        else:
            if loggerFormat is None:
                ret = -TWO
            else:
                if loggerDateFmt is None:
                    ret = -THREE
                else: 
                    if loggerLevel is None:
                        ret = -FOUR
                    else:
                        self.logger = logging.getLogger(loggerName)
                        logging.basicConfig(
                            format  = loggerFormat,
                            datefmt = loggerDateFmt,
                            level   = loggerLevel
                        )          
            
        return ret
    
    """
    Returns the logger.
    
    return: the logger.
    """
    def getLogger(self):
        return self.logger
    
    """
    This method prints a debug message.
    
    message: the message which will be printed with the logger.
    return: ZERO if everything went well
        -ONE if no Logger could be found
        ONE  if no message was given
    """
    def printDebug(self, message: str = None) -> int: 
        ret = ZERO
        
        if message is not None:
            
            if self.logger is not None:
                self.logger.debug(message)
            else:
                ret = -ONE
        else:
            ret = ONE
            
        return ret
    
    """
    This method prints a info message.
    
    message: the message which will be printed with the logger.
    return: ZERO if everything went well,
        -ONE if no Logger could be found,
        ONE  if no message was given.
    """
    def printInfo(self, message: str = None) -> int: 
        ret = ZERO
        
        if message is not None:
            
            if self.logger is not None:
                self.logger.info(message)
            else:
                ret = -ONE
        else:
            ret = ONE
            
        return ret
        
    """
    This method prints a warning message.
    
    message: the message which will be printed with the logger.
    return: ZERO if everything went well,
        -ONE if no Logger could be found,
        ONE  if no message was given.
    """
    def printWarning(self, message: str = None) -> int: 
        ret = ZERO
        
        if message is not None:
            
            if self.logger is not None:
                self.logger.warn(message)
            else:
                ret = -ONE
        else:
            ret = ONE
            
        return ret
        
    """
    This method prints a error message.
    
    message: the message which will be printed with the logger.
    return: ZERO if everything went well,
        -ONE if no Logger could be found,
        ONE  if no message was given.
    """
    def printError(self, message: str = None) -> int: 
        ret = ZERO
        
        if message is not None:
            
            if self.logger is not None:
                self.logger.error(message)
            else:
                ret = -ONE
        else:
            ret = ONE
            
        return ret
        
        
    """
    This method prints a critical error message.
    
    message: the message which will be printed with the logger.
    return: ZERO if everything went well,
        -ONE if no Logger could be found,
        ONE  if no message was given.
    """
    def printCritical(self, message: str = None) -> int:  
        ret = ZERO
        
        if message is not None:
            
            if self.logger is not None:
                self.logger.critical(message)
            else:
                ret = -ONE
        else:
            ret = ONE
            
        return ret
    
    """
    
    """
    def startPrintProgress(self, amount: int = 1):
        ret = ZERO

        if (self.printProgressAmount != self.printProgressIndex):
            ret = ONE

        if (amount > ZERO):
            self.printProgressAmount = amount
            self.printProgressTime = datetime.now()
            self.printProgressIndex = 0
        else:
            ret = -ONE

        return ret

    """
    
    """
    def printProgress(self):
        ret = ZERO
        
        # Few checks before processing to make sure no error is thrown
        if self.printPercentPeriod > ZERO:
            if self.printProgressAmount > ZERO:
                if self.printProgressIndex >= ZERO:
                    if self.printProgressIndex < self.printProgressAmount:

                        self.printProgressIndex += ONE
                        
                        # Every <period> index a print needs to be done      
                        period = round((self.printProgressAmount * 
                                        self.printPercentPeriod))
                        
                        # Period needs to be at least one.
                        if period < ONE:
                            period = ONE
                        
                        # If currentIndex is dividable by period, a print will 
                        # take place if not, no print will be done.
                        if (self.printProgressIndex % period == ZERO or 
                            self.printProgressIndex == 
                            self.printProgressAmount):
                            
                            totalAmountLength   = len(str(
                                self.printProgressAmount))
                            
                            # Basic print string without estimated left 
                            # processing time. 
                            printString         = (("({:" + 
                                str(totalAmountLength) + 
                                "} | {:" + str(totalAmountLength) + "}) {:" + 
                                str(SIX) + "}% completed.").format(
                                    self.printProgressIndex, 
                                    self.printProgressAmount, 
                                    round((self.printProgressIndex * HUNDRED 
                                        * HUNDRED) 
                                        / self.printProgressAmount) / HUNDRED)
                                )
                            
                            # Adding estimated left processing time.
                            if (self.printProgressTime is not None and 
                                isinstance(self.printProgressTime, datetime)):
                            
                                now           = datetime.now()
                                residualTime  = timedelta(seconds = 
                                    ((self.printProgressAmount - 
                                    self.printProgressIndex) * 
                                    (now - 
                                    self.printProgressTime).total_seconds() 
                                    / self.printProgressIndex)).total_seconds()

                                days = ZERO
                                hours = ZERO
                                minutes = ZERO
                                seconds = ZERO

                                # Days are also printed in case of a huge taks.
                                if (residualTime > 0):
                                    days,    remainder  = divmod(residualTime, 
                                        SIXTY * SIXTY * TWENTYFOUR)
                                    hours,   remainder  = divmod(remainder, 
                                        SIXTY * SIXTY)
                                    minutes, seconds    = divmod(remainder, 
                                        SIXTY)

                                printString += (" [Residual Time: ~{:0" + 
                                    str(TWO) + 
                                    "} days, {:0" + str(TWO) + "}:{:0" + 
                                    str(TWO) + 
                                    "}:{:0" + str(TWO) + "}]").format(
                                        int(days),
                                        int(hours),
                                        int(minutes),
                                        int(seconds)
                                    )
                                
                            self.printInfo(printString)
                    else:
                        ret = -FOUR
                else:
                    ret = -THREE
            else:
                ret = -TWO
        else:
            ret = -ONE
            
        return ret

