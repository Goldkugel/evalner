#!/usr/bin/env python
# coding: utf-8


# In[ ]:


from Values import *


# In[ ]:


def concat(elements, noPreConcatString = [], noPostConcatString = []):
    ret = None
    
    previousElement = EMPTYSTRING
    if elements is not None:
        ret = EMPTYSTRING
    
        for index, element in enumerate(elements):
            
            if (element not in noPreConcatString and 
                previousElement not in noPostConcatString and index > 0):
                ret += SPACE
            
            ret += element
            previousElement = element
    
    return ret


# In[ ]:


def createSentences(data, noPreSpaceCharacters, noPostSpaceCharacters):
    ret = None

    if (data.getSentenceIDColumn() is not None and 
        data.getWordColumn() is not None):
        
        sentenceIDs = data.getData()[data.getSentenceIDColumn()].unique()
        ret = [EMPTYSTRING] * len(sentenceIDs)

        Logger.getSingletonLogger().startPrintProgress(len(sentenceIDs))
        
        for sentenceIndex, sentenceID in enumerate(sentenceIDs):
            sentenceWords = data.getData()[data.getData()[data.
                getSentenceIDColumn()] == sentenceID]
            sentenceWords = sentenceWords[data.getWordColumn()]
            
            ret[sentenceIndex] = concat(sentenceWords, 
                noPreSpaceCharacters, noPostSpaceCharacters)

            Logger.getSingletonLogger().printProgress()

    return ret


# In[ ]:


def diffWord(data, words, prints = FIVE):
    ret = ReturnValue(ZERO)

    if (data is not None and words is not None and data.getData() is not None 
        and data.getWordColumn() is not None):
            
        now = datetime.now()
        length = len(data.getData())

        Logger.getSingletonLogger().startPrintProgress(length)

        for index in range(ZERO, length):
            
            row = data.getData().loc[index]

            if index < len(words) and row[data.getWordColumn()] != words[index]:

                Logger.printInfo("Difference found.")
                fromIndex = index - prints
                if (fromIndex < ZERO):
                    fromIndex = ZERO
                toIndex = index + prints
                if (toIndex > len(data.getData())):
                    toIndex = len(data.getData())

                for printIndex in range(fromIndex, toIndex):
                    if printIndex == index:
                        Logger.getSingletonLogger().printInfo(printIndex)
                    Logger.getSingletonLogger().printInfo(diff.format(
                        data.getData()[data.getWordColumn()][printIndex], 
                        words[printIndex]))
                break

            Logger.printProgress()
    else:
        Logger.getSingletonLogger().printWarning(diffWordsNotPossible)
        ret.setValue(ONE)
    
    return ret

