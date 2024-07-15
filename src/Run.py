#!/usr/bin/env python
# coding: utf-8

from Values                              import *
from Utils                               import *
from Logger                              import *
from Task                                import *
from TaskList                            import *
from ReturnValue                         import *
from Data                                import *
from ProcessFile                         import *

"""

"""
class Run:

    __runName = None

    __experimentName = None

    __tasklist = None

    __processFile = None

    def __init__(self) -> None:
        self.__tasklist = TaskList()
        self.__processFile = ProcessFile()

    def setRunName(self, runName: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        return ret
    
    def setExperimentName(self, experimentName: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        return ret
    
    def setInputFile(self, inputFile: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        return ret
    
    def getRunName(self) -> str:
        return self.__runName
    
    def getExperimentName(self) -> str:
        return self.__experimentName
    
    def checkDirectories(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        return ret
    
    def createDirectories(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        return ret
    
    def clean(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        return ret
    
    def getTaskList(self) -> TaskList:
        return self.__tasklist
    
    def getNextAvailableRunName(self) -> str:
        ret = ""

        return ret
    
    def startRun(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        return ret
    
    def __prepareData(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        return ret
    
    