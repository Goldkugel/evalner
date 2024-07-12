#!/usr/bin/env python
# coding: utf-8

from Values      import * 
from Logger      import *
from ReturnValue import *
from Data        import *

from transformers          import AutoTokenizer
from transformers          import AutoModelForTokenClassification
from transformers          import pipeline

import pandas as pd
import os

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
            sentenceWords = sentenceWords[data.getWordColumn()].reset_index(drop = True)

            for wordIndex in range(ZERO, len(sentenceWords)):
                sentenceWords[wordIndex] = str(sentenceWords[wordIndex])
            
            ret[sentenceIndex] = concat(sentenceWords, 
                noPreSpaceCharacters, noPostSpaceCharacters)

            Logger.getSingletonLogger().printProgress()

    return ret

def diffWord(data, words, prints = FIVE, offSet = ZERO):
    ret = ReturnValue(ZERO)

    if (data is not None and words is not None and data.getData() is not None 
        and data.getWordColumn() is not None):
            
        now = datetime.now()
        length = len(data.getData())

        Logger.getSingletonLogger().startPrintProgress(length)

        for index in range(offSet, length):
            
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

            Logger.getSingletonLogger().printProgress()
    else:
        Logger.getSingletonLogger().printWarning(diffWordsNotPossible)
        ret.setValue(ONE)
    
    return ret


def applyModel(model, sentences, file):

    if (not os.path.isfile(file)):

        modelResults = [None] * len(sentences)

        Logger.getSingletonLogger().startPrintProgress(len(sentences))

        for sentenceIndex, sentence in enumerate(sentences):
            modelResults[sentenceIndex] = model(sentence)
            Logger.getSingletonLogger().printProgress()

        header = True
        mode = WRITE

        Logger.getSingletonLogger().startPrintProgress(len(sentences))

        for modelResultIndex in range(ZERO, len(modelResults)):
            res = pd.DataFrame(modelResults[modelResultIndex])

            res[MODEL_RESULT_WORD_COLUMN] = res[MODEL_RESULT_WORD_COLUMN].astype(str)

            res.to_csv(
                file, 
                index = False, 
                mode = mode, 
                header = header
            ) 

            if header:
                header = False
                mode = APPENDTOFILE
            
        Logger.getSingletonLogger().printProgress()

def removeWords(data: Data = None, wordList: list = None) -> ReturnValue:
    ret = ReturnValue(ZERO)

    if (data is not None 
        and data.getWordColumn() is not None 
        and wordList is not None 
        and len(wordList) >= ONE):

        df = data.getData()
        filter= df[data.getWordColumn()].isin(wordList)
        df = df[~filter].reset_index(drop = True)
        data.setData(df)

    else:
        ret.setValue(-ONE)

    return ret
