#!/usr/bin/env python
# coding: utf-8

from Values               import *
from Logger               import *

"""

"""
class ReturnValue:

    #
    __message = None

    #
    __value = ZERO

    #
    __isCritical = False

    #
    __isDebug = False

    #
    __className = None

    #
    __methodName = None

    #
    __roots = list()

    """
    
    """
    def __init__(self, value: int = ZERO, message: str = RETURNVALUE_stdMsg):
        self.setValue(value)
        self.setMessage(message)
        self.__isCritical = False
        self.__isDebug = False
        self.__roots = list()

    """
    
    """
    def setClassName(self, className: str = None):
        self.__className = className

    """
    
    """
    def setMethodName(self, methodName: str = None):
        self.__methodName = methodName

    """

    """
    def getClassName(self) -> str:
        return self.__className
    
    """
    
    """
    def getMethodName(self) -> str:
        return self.__methodName

    """
    
    """
    def addRoot(self, root = None) -> int:
        if (root is not None):
            self.__roots.append(root)

    """
    
    """
    def isCritical(self) -> bool:
        return self.__isCritical
    
    """
    
    """
    def isDebug(self) -> bool:
        return self.__isDebug
    
    """
    
    """
    def getValue(self) -> int:
        return self.__value
    
    """
    
    """
    def getMessage(self) -> str:
        return self.__message

    """
    
    """
    def setValue(self, value: int = ZERO):
        self.__value = value

    """
    
    """
    def setMessage(self, message: str = None):
        self.__message = message

    """
    
    """
    def setCritical(self, isCritical: bool = True):
        self.__isCritical = isCritical
    
    """
    
    """
    def setDebug(self, isDebug: bool = True):
        self.__isDebug = isDebug

    

    """
    
    """
    def log(self):
        logger = Logger.getSingletonLogger()

        if (self.isCritical()):
            logger.printCritical(EVAL_RETURNVALUE.
                format(self.getMessage(), self.getValue(), self.getClassName(), 
                    self.getMethodName()))
        else:
            if (self.isDebug()):
                logger.printDebug(EVAL_RETURNVALUE.
                    format(self.getMessage(), self.getValue(), 
                        self.getClassName(), self.getMethodName()))
            else:
                if (self.getValue() < ZERO):
                    logger.printError(EVAL_RETURNVALUE.
                        format(self.getMessage(), self.getValue(), 
                            self.getClassName(), self.getMethodName()))
                else:
                    if (self.getValue() > ZERO):
                        logger.printWarning(EVAL_RETURNVALUE.
                            format(self.getMessage(), self.getValue(), 
                                self.getClassName(), self.getMethodName()))
                    else:
                        logger.printInfo(EVAL_RETURNVALUE.
                            format(self.getMessage(), self.getValue(), 
                                self.getClassName(), self.getMethodName()))

        for root in self.__roots:
            root.log()

    """
    
    """
    def eval(self):
        if (self.getValue() != ZERO):
            self.log()

