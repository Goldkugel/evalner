#!/usr/bin/env python
# coding: utf-8


# In[ ]:


from Values import *


# In[2]:


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
    def addRoot(self, ret = None) -> int:
        if (ret is not None):
            self.__roots.append(ret)

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

        if (self.__isCritical):
            logger.printCritical(EVAL_RETURNVALUE.
                format(self.getMessage(), self.getValue()))
        else:
            if (self.__isDebug):
                logger.printDebug(EVAL_RETURNVALUE.
                    format(self.getMessage(), self.getValue()))
            else:
                if (self.__value < ZERO):
                    logger.printError(EVAL_RETURNVALUE.
                        format(self.getMessage(), self.getValue()))
                else:
                    if (self.__value > ZERO):
                        logger.printWarning(EVAL_RETURNVALUE.
                            format(self.getMessage(), self.getValue()))
                    else:
                        logger.printInfo(EVAL_RETURNVALUE.
                            format(self.getMessage(), self.getValue()))

        for root in self.__roots:
            root.log()

    """
    
    """
    def eval(self):
        if (self.getValue() != ZERO):
            self.log()

