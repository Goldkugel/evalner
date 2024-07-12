#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import os
import math
from datetime             import timedelta, datetime

from ReturnValue          import *
from Values               import *
from Configuration        import *
from Logger               import *

class Data:
    
    __data = None
    
    __documentIDColumn = None
    
    __sentenceIDColumn = None
    
    __wordIDColumn = None
    
    __wordColumn = None
    
    __labelColumn = None

    """
    
    """
    def __init__(self):
        self.__data = None
        self.__documentIDColumn = None
        self.__sentenceIDColumn = None
        self.__wordIDColumn = None
        self.__wordColumn = None
        self.__labelColumn = None

    """
    
    """
    def addColumn(self, column, columnName = "column") -> ReturnValue:
        ret = ReturnValue(ZERO)

        if (self.__data is None):
            self.__data = pd.DataFrame(column, columns = [columnName])
        else:
            if (len(column) == len(self.__data)):
                self.__data[columnName] = column
            else:
                ret.setValue(-ONE)

        return ret
    
    def setData(self, data = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if (self.__data is not None):
            ret.setValue(ONE)

        self.__data = data

        return ret

    """
    
    """
    def getDocumentIDColumn(self) -> str:
        return self.__documentIDColumn
    
    """
    
    """
    def getSentenceIDColumn(self) -> str:
        return self.__sentenceIDColumn
    
    """
    
    """
    def getWordIDColumn(self) -> str:
        return self.__wordIDColumn
    
    """
    
    """
    def getWordColumn(self) -> str:
        return self.__wordColumn
    
    """
    
    """
    def getLabelColumn(self) -> str:
        return self.__labelColumn
    
    """
    
    """
    def setDocumentIDColumn(self, documentIDColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)
        
        if documentIDColumn is not None:
            self.__documentIDColumn = documentIDColumn
        else:
            ret.setValue(-ONE)
            ret.setMessage(DATA_SETDOCUMENTIDCOLUMN_invalidColumnName)
        
        return ret
    
    """
    
    """
    def setSentenceIDColumn(self, sentenceIDColumn:str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)
        
        if sentenceIDColumn is not None:
            self.__sentenceIDColumn = sentenceIDColumn
        else:
            ret.setValue(-ONE)
            ret.setMessage(DATA_SETSENTENCEIDCOLUMN_invalidColumnName)
        
        return ret
        
    """
    
    """
    def setWordIDColumn(self, wordIDColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)
        
        if wordIDColumn is not None:
            self.__wordIDColumn = wordIDColumn
        else:
            ret.setValue(-ONE)
            ret.setMessage(DATA_SETWORDIDCOLUMN_invalidColumnName)
        
        return ret

    """
    
    """
    def setWordColumn(self, wordColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)
        
        if wordColumn is not None:
            self.__wordColumn = wordColumn
        else:
            ret.setValue(-ONE)
            ret.setMessage(DATA_SETWORDCOLUMN_invalidColumnName)
            ret.setCritical()
        
        return ret
        
    """
    
    """
    def setLabelColumn(self, labelColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)
        
        if labelColumn is not None:
            self.__labelColumn = labelColumn
        else:
            ret.setValue(-ONE)
            ret.setMessage(DATA_SETLABELCOLUMN_invalidColumnName)
            ret.setCritical()
        
        return ret

    
    """
    
    """
    def loadCSVData(self, directory: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)
        
        if directory is not None:
            if (os.path.isfile(directory)):
                self.__data = pd.read_csv(directory, keep_default_na = False,
                    low_memory = False)
            else:
                ret.setValue(-ONE)
                ret.setMessage(DATA_LOADCSVDATA_fileNotFound.
                    format(directory))
                ret.setCritical()
        else:
            ret.setValue(ONE)
            ret.setMessage(DATA_LOADCSVDATA_invalidDirectory)
            ret.setCritical()
            
        return ret
    
    """
    
    """
    def writeCSVData(self, directory: str = None, mode: str = WRITE, 
        header: bool = True) -> ReturnValue:
        ret = ReturnValue(ZERO)
        
        if directory is not None:
            if os.path.isfile(directory):
                ret.setValue(TWO)
                ret.setMessage(DATA_WRITECSVDATA_fileFound.
                    format(directory))

            if self.getData() is not None:
                self.getData().to_csv(directory, index = False, mode = mode, 
                    header = header)
            else:
                ret.setValue(THREE)
                ret.setMessage(DATA_WRITECSVDATA_noDataToWrite.
                    format(directory))
        else:
            ret.setValue(ONE)
            ret.setMessage(DATA_WRITECSVDATA_invalidDirectory)

        return ret
    
    """
    
    """
    def getColumns(self) -> list:
        ret = list()
        
        if self.getData() is not None:
            ret = list(self.getData().columns)
            
        return ret
       
    """
    
    """
    def getRowCount(self) -> int:
        ret = ZERO
        
        if self.getData() is not None:
            ret = len(self.getData())
        
        return ret
     
    """
    
    """    
    def getColumnCount(self) -> int:
        ret = ZERO
        
        if self.getData() is not None:
            ret = len(self.getData().columns)
            
        return ret
    
    """
    
    """
    def getLabels(self) -> list:
        ret = list()
        
        if self.getData() is not None and self.getLabelColumn() is not None:
            ret = self.getData()[self.getLabelColumn()].unique().tolist()
            
        return ret
            
    """
    
    """
    def getLabelCount(self, label: str = None) -> int:
        return len(self.getData()[self.getData()[self.getLabelColumn()] == label])
    
    """
    
    """
    def getRow(self, rowIndex: int = ZERO):
        ret = None
        
        if rowIndex >= ZERO and rowIndex < self.getRowCount():
            ret = self.getData().loc[rowIndex]
        
        return ret
    
    """
    
    """
    def setRow(self, rowIndex: int = None, elements = None) -> ReturnValue:
        ret = ReturnValue(ZERO)
        
        if rowIndex >= ZERO and rowIndex < self.getRowCount():
            self.getData().loc[rowIndex] = elements
            self.getData().sort_index().reset_index(drop = True)
        else:
            ret.setValue(-ONE)
            ret.setMessage(DATA_SETROW_invalidIndex.
                format(rowIndex))
            
        return ret
    
    """
    
    """
    def getSentence(self, sentenceID: int = ZERO):
        ret = None
        
        if self.getData() is not None and self.getSentenceIDColumn() is not None:
            ret = self.getData().loc[self.getData()[self.getSentenceIDColumn()] == sentenceID, :]
        
        return ret
    """
    
    """
    def getDocument(self, documentID: int = ZERO):
        ret = None
        
        if self.getData() is not None and self.getDocumentIDColumn() is not None:
            ret = self.getData().loc[self.getData()[self.getDocumentIDColumn()] == documentID, :]
        
        return ret
    
    """
    
    """
    def getData(self):
        return self.__data
    
    """
    
    """
    def clone(self):
        ret = Data()
        ret.__data = self.getData().copy(deep = True)
        ret.setDocumentIDColumn(self.getDocumentIDColumn())
        ret.setLabelColumn(self.getLabelColumn())
        ret.setSentenceIDColumn(self.getSentenceIDColumn())
        ret.setWordColumn(self.getWordColumn())
        ret.setWordIDColumn(self.getWordIDColumn())        
        return ret
    
    """
    
    """
    def splitUp(self, files: list = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if (self.getData() is not None and self.getRowCount() > len(files)):
            if (files is not None and len(files) > ZERO):
                count = self.getRowCount() / len(files)

                for index in range(ZERO, len(files)):
                    fromIndex = math.floor(count * index)
                    toIndex = math.floor(count * (index + 1))
                    
                    if index == len(files) - 1:
                        toIndex = self.getRowCount()

                    d = self.getData().iloc[fromIndex:toIndex]
                    d.to_csv(files[index], index = False)
            else:
                ret.setValue(TWO)
                ret.setMessage(DATA_SPLITUP_noFileSpecified)
        else:
            ret.setValue(ONE)
            ret.setMessage(DATA_SPLITUP_noDataToSplit)

        return ret
    

