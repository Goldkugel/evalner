#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os

from ReturnValue          import *
from Values               import *
from Configuration        import *
from Logger               import *
from DefaultColumns       import *

class Data(DefaultColumns):
    
    #
    __data = None

    """
    
    """
    def __init__(self):
        self.__data = None

    """
    
    """
    def addColumn(self, column, 
        columnName: str = DEFAULT_COLUMN_NAME) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DATA)
        ret.setMethodName(DATA_addColumn)

        if (column is not None):
            if (self.getData() is None):
                update = self.setData(pd.DataFrame(column, columns = [columnName]))
                if (update.getValue() == ZERO):
                    ret.setMessage(DATA_addColumn_columnAddedSuccessfully.
                        format(columnName))
                else:
                    if (update.getValue() > ZERO):
                        ret.setValue(ONE)
                        ret.setMessage(DATA_addColumn_warningsWhileAddingColumn.
                            format(columnName))
                    else:
                        ret.setValue(-TWO)
                        ret.setMessage(DATA_addColumn_errorsWhileAddingColumn.
                            format(columnName))
                    ret.addRoot(update)
            else:
                if (len(column) == len(self.getData())):
                    data = self.getData()

                    replace = columnName in data.columns

                    data[columnName] = column
                    update = self.setData(data)
                    if (update.getValue() == ZERO):
                        if (not replace):
                            ret.setMessage(DATA_addColumn_columnAddedSuccessfully.
                                format(columnName))
                        else:
                            ret.setValue(TWO)
                            ret.setMessage(DATA_addColumn_replacingColumn.
                                format(columnName))
                    else:
                        if (update.getValue() > ZERO):
                            ret.setValue(ONE)
                            ret.setMessage(DATA_addColumn_warningsWhileAddingColumn.
                                format(columnName))
                        else:
                            ret.setValue(-TWO)
                            ret.setMessage(DATA_addColumn_errorsWhileAddingColumn.
                                format(columnName))
                        ret.addRoot(update)
                else:
                    ret.setValue(-ONE)
                    ret.setMessage(DATA_addColumn_lengthsDoNotMatch.
                        format(columnName, len(self.getData()), len(columnName)))
        else:
            ret.setValue(THREE)
            ret.setMessage(DATA_addColumn_noColumnGiven.format(columnName))

        return ret
    
    """
    
    """
    def setData(self, data = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DATA)
        ret.setMethodName(DATA_setData)

        if (self.__data is not None):
            ret.setValue(ONE)
            ret.setMessage(DATA_setData_overwritingData)
        else:
            ret.setMessage(DATA_setData_setDataCompleted.
                foramt(len(self.getData().columns), len(self.getData())))

        self.__data = data

        return ret
    
    """
    
    """
    def loadCSVData(self, directory: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DATA)
        ret.setMethodName(DATA_loadCSVData)
        
        if (directory is not None and len(directory) > ZERO):
            if (os.path.isfile(directory)):
                self.__data = pd.read_csv(directory, keep_default_na = False,
                    low_memory = False)
                ret.setMessage(DATA_loadCSVData_loadedSuccessfully.
                    format(directory, len(self.getData().columns), 
                        len(self.getData())))
            else:
                ret.setValue(-ONE)
                ret.setMessage(DATA_loadCSVData_fileNotFound.
                    format(directory))
                ret.setCritical()
        else:
            ret.setValue(ONE)
            ret.setMessage(DATA_loadCSVData_invalidDirectory)
            ret.setCritical()
            
        return ret
    
    """
    
    """
    def writeCSVData(self, directory: str = None, mode: str = WRITE, 
        header: bool = True) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DATA)
        ret.setMethodName(DATA_writeCSVData)
        
        if (directory is not None and len(directory) > ZERO):
            if os.path.isfile(directory):
                ret.setValue(TWO)
                ret.setMessage(DATA_writeCSVData_fileFound.
                    format(directory))

            if self.getData() is not None:
                self.getData().to_csv(directory, index = False, mode = mode, 
                    header = header)
                if (ret.setValue() == ZERO):
                    ret.setMessage(DATA_writeCSVData_dataSaved.
                        format(directory))
            else:
                ret.setValue(THREE)
                ret.setMessage(DATA_writeCSVData_noDataToWrite.
                    format(directory))
        else:
            ret.setValue(ONE)
            ret.setMessage(DATA_writeCSVData_invalidDirectory)

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

        ret.setClassName(DATA)
        ret.setMethodName(DATA_setRow)
        
        if (rowIndex is not None and 
            rowIndex >= ZERO and 
            rowIndex < self.getRowCount()):
            self.getData().loc[rowIndex] = elements
            self.getData().sort_index().reset_index(drop = True)
            ret.setMessage(DATA_setRow_successfullySet.format(rowIndex))
        else:
            ret.setValue(-ONE)
            ret.setMessage(DATA_setRow_invalidIndex.
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
