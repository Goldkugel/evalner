#!/usr/bin/env python
# coding: utf-8

from Values                              import *
from Utils                               import *
from ReturnValue                         import *

"""
This class manages the column names of data. It enables to set and modify the
column names of tabular data. The data itself is managed in another class.  
"""
class DefaultColumns:

    # The default column names are listed here. <wordColumn> and <labelColumn>
    # are mandatory.
    __wordColumn = None
    __labelColumn = None
    __wordIDColumn = None
    __documentIDColumn = None
    __sentenceIDColumn = None

    """
    Initalization. All values are set to None. 
    """
    def __init__(self):
        self.__wordColumn = None
        self.__labelColumn = None
        self.__wordIDColumn = None
        self.__documentIDColumn = None
        self.__sentenceIDColumn = None

    """
    Sets all the columns names.

    wordColumn: the name of the column in which the words are stored.
    labelColumn: the name of the column in which the labels are stored.
    wordIDColumn: the name of the column in which the words IDs are
        stored. 
    sentenceIDColumn: the name of the column in which the sentece IDs are
        stored.
    documentIDColumn: the name of the column in which the document IDs are
        stored.
    """
    def setColumns(self, 
        wordColumn: str = None, 
        labelColumn: str = None, 
        wordIDColumn: str = None, 
        sentenceIDColumn: str = None, 
        documentIDColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DEFAULTCOLUMNS)
        ret.setMethodName(DEFAULTCOLUMNS_setColumns)

        returnValues = [
            self.setWordColumn(wordColumn = wordColumn),
            self.setLabelColumn(labelColumn = labelColumn),
            self.setWordIDColumn(wordIDColumn = wordIDColumn),
            self.setSentenceIDColumn(sentenceIDColumn = sentenceIDColumn),
            self.setDocumentIDColumn(documentIDColumn = documentIDColumn)
        ]

        for retVal in returnValues:
            if (retVal.getValue() != ZERO):
                if (retVal.getValue() < ZERO):
                    ret.setValue(-ONE)
                    ret.setMessage(DEFAULTCOLUMNS_setColumns_errorsOccurred)
                else:
                    if (ret.getValue() == ZERO):
                        ret.setValue(ONE)
                        ret.setMessage(
                            DEFAULTCOLUMNS_setColumns_warningsOccurred)
                ret.addRoot(retVal)          

        return ret

    """
    This method sets the column name in which the document IDs are stored. A 
    document ID column is not mandatory because there might be some datasets
    which are not differentiating between documents and therefore do not have
    any column which has a similar meaning. 

    documentIDColumn: the name of the column in which the document IDs are
        stored.
    return: a ReturnValue object storing the return value and a message. Please
        look up the documentation of the ReturnValue class for more information.
        ZERO: everything went well,
        ONE:  the given parameter is None or completely missing,
        TWO:  the document ID column has already been set and has been 
            overwritten with the given column name. 
    """
    def setDocumentIDColumn(self, documentIDColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DEFAULTCOLUMNS)
        ret.setMethodName(DEFAULTCOLUMNS_setDocumentIDColumn)

        if (documentIDColumn is not None and len(documentIDColumn) > ZERO):
            if (self.__documentIDColumn is not None and 
                len(self.__documentIDColumn) > ZERO):
                ret.setValue(TWO)
                ret.setMessage(DEFAULTCOLUMNS_setDocumentIDColumn_replacedValue.
                    format(self.__documentIDColumn, documentIDColumn))
            else:
                ret.setMessage(DEFAULTCOLUMNS_setDocumentIDColumn_setValue.
                    format(documentIDColumn))
            self.__documentIDColumn = documentIDColumn
        else:
            ret.setValue(ONE)
            ret.setMessage(DEFAULTCOLUMNS_setDocumentIDColumn_parameterIsNone)

        return ret
    
    """
    This method sets the column name in which the sentence IDs are stored. A 
    sentence ID column is not mandatory because there might be some datasets
    which are not differentiating between sentences and therefore do not have
    any column which has a similar meaning. 

    sentenceIDColumn: the name of the column in which the sentece IDs are
        stored.
    return: a ReturnValue object storing the return value and a message. Please
        look up the documentation of the ReturnValue class for more information.
        ZERO: everything went well,
        ONE:  the given parameter is None or completely missing,
        TWO:  the sentence ID column has already been set and has been 
            overwritten with the given column name. 
    """
    def setSentenceIDColumn(self, sentenceIDColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DEFAULTCOLUMNS)
        ret.setMethodName(DEFAULTCOLUMNS_setSentenceIDColumn)

        if (sentenceIDColumn is not None and len(sentenceIDColumn) > ZERO):
            if (self.__sentenceIDColumn is not None and 
                len(self.__sentenceIDColumn) > ZERO):
                ret.setValue(TWO)
                ret.setMessage(DEFAULTCOLUMNS_setSentenceIDColumn_replacedValue.
                    format(self.__sentenceIDColumn, sentenceIDColumn))
            else:
                ret.setMessage(DEFAULTCOLUMNS_setSentenceIDColumn_setValue.
                    format(sentenceIDColumn))
            self.__sentenceIDColumn = sentenceIDColumn
        else:
            ret.setValue(ONE)
            ret.setMessage(DEFAULTCOLUMNS_setSentenceIDColumn_parameterIsNone)

        return ret
    
    """
    This method sets the column name in which the word IDs are stored. A 
    word ID column is not mandatory because there might be some datasets
    which are not differentiating between words and therefore do not have
    any column which has a similar meaning. 

    wordIDColumn: the name of the column in which the words IDs are
        stored.
    return: a ReturnValue object storing the return value and a message. Please
        look up the documentation of the ReturnValue class for more information.
        ZERO: everything went well,
        ONE:  the given parameter is None or completely missing,
        TWO:  the word ID column has already been set and has been 
            overwritten with the given column name. 
    """
    def setWordIDColumn(self, wordIDColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DEFAULTCOLUMNS)
        ret.setMethodName(DEFAULTCOLUMNS_setWordIDColumn)

        if (wordIDColumn is not None and len(wordIDColumn) > ZERO):
            if (self.__wordIDColumn is not None and 
                len(self.__wordIDColumn) > ZERO):
                ret.setValue(TWO)
                ret.setMessage(DEFAULTCOLUMNS_setWordIDColumn_replacedValue.
                    format(self.__wordIDColumn, wordIDColumn))
            else:
                ret.setMessage(DEFAULTCOLUMNS_setWordIDColumn_setValue.
                    format(wordIDColumn))
            self.__wordIDColumn = wordIDColumn
        else:
            ret.setValue(ONE)
            ret.setMessage(DEFAULTCOLUMNS_setWordIDColumn_parameterIsNone)

        return ret
    
    """
    This method sets the column name in which the labels are stored. A 
    label column is mandatory because in named entity recognition tasks there
    is always an entity to recognise for each word. 

    labelColumn: the name of the column in which the labels are stored.
    return: a ReturnValue object storing the return value and a message. Please
        look up the documentation of the ReturnValue class for more information.
        ZERO: everything went well,
        -ONE: the given parameter is None or completely missing,
        ONT:  the label column has already been set and has been overwritten 
            with the given column name. 
    """
    def setLabelColumn(self, labelColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DEFAULTCOLUMNS)
        ret.setMethodName(DEFAULTCOLUMNS_setLabelColumn)

        if (labelColumn is not None and len(labelColumn) > ZERO):
            if (self.__labelColumn is not None and 
                len(self.__labelColumn) > ZERO):
                ret.setValue(ONE)
                ret.setMessage(DEFAULTCOLUMNS_setLabelColumn_replacedValue.
                    format(self.__labelColumn, labelColumn))
            else:
                ret.setMessage(DEFAULTCOLUMNS_setLabelColumn_setValue.
                    format(labelColumn))
            self.__labelColumn = labelColumn
        else:
            ret.setValue(-ONE)
            ret.setMessage(DEFAULTCOLUMNS_setLabelColumn_parameterIsNone)

        return ret
    
    """
    This method sets the column name in which the words are stored. A word 
    column is mandatory because in named entity recognition tasks there are 
    always words which needs to be processed.

    wordColumn: the name of the column in which the words are stored.
    return: a ReturnValue object storing the return value and a message. Please
        look up the documentation of the ReturnValue class for more information.
        ZERO: everything went well,
        -ONE: the given parameter is None or completely missing,
        ONE:  the word column has already been set and has been overwritten 
            with the given column name. 
    """
    def setWordColumn(self, wordColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(DEFAULTCOLUMNS)
        ret.setMethodName(DEFAULTCOLUMNS_setWordColumn)

        if (wordColumn is not None and len(wordColumn) > ZERO):
            if (self.__wordColumn is not None and 
                len(self.__wordColumn) > ZERO):
                ret.setValue(ONE)
                ret.setMessage(DEFAULTCOLUMNS_setWordColumn_replacedValue.
                    format(self.__wordColumn, wordColumn))
            else:
                ret.setMessage(DEFAULTCOLUMNS_setWordColumn_setValue.
                    format(wordColumn))
            self.__wordColumn = wordColumn
        else:
            ret.setValue(-ONE)
            ret.setMessage(DEFAULTCOLUMNS_setWordColumn_parameterIsNone)

        return ret
    
    """
    Returns the word column name or None if it has not been set.

    return: a string with the name.
    """
    def getWordColumn(self) -> str:
        return self.__wordColumn
    
    """
    Returns the word ID column name or None if it has not been set.

    return: a string with the name.
    """
    def getWordIDColumn(self) -> str:
        return self.__wordIDColumn
    
    """
    Returns the label column name or None if it has not been set.

    return: a string with the name.
    """
    def getLabelColumn(self) -> str:
        return self.__labelColumn
    
    """
    Returns the document ID column name or None if it has not been set.

    return: a string with the name.
    """
    def getDocumentIDColumn(self) -> str:
        return self.__documentIDColumn
    
    """
    Returns the sentence ID column name or None if it has not been set.

    return: a string with the name.
    """
    def getSentenceIDColumn(self) -> str:
        return self.__sentenceIDColumn