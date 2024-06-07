#!/usr/bin/env python
# coding: utf-8


# In[ ]:


from Values import *
from ReturnValue import *


# In[ ]:


def deleteDocuments(data, index, resultData, resultValue, args) -> ReturnValue:
    ret = ReturnValue(ZERO)

    # Check if the main parameters are all given.
    if (data.getData() is not None and data.getDocumentIDColumn() is not None):
        row = pd.DataFrame(
            data = [data.getData().iloc[index]], 
            columns = data.getData().columns
        ).reset_index(drop = True)

        resultValue[index] = ZERO

        if (row is not None and args is not None and 
            row[data.getDocumentIDColumn()][ZERO] in args):
            row = None
            resultValue[index] = ONE

        resultData[index] = row

    else:
        resultValue[index] = -ONE
        ret.setValue(ONE)
        ret.setMessage()

    return ret


# In[ ]:


def deleteSentences(data, index, resultData, resultValue, args) -> ReturnValue:
    ret = ReturnValue(ZERO)

    # Check if the main parameters are all given.
    if (data.getData() is not None and data.getSentenceIDColumn() is not None):
        row = pd.DataFrame(
            data = [data.getData().iloc[index]], 
            columns = data.getData().columns
        ).reset_index(drop = True)

        resultValue[index] = ZERO
        
        if (row is not None and args is not None and 
            row[data.getSentenceIDColumn()][ZERO] in args):
                row = None
                resultValue[index] = ONE

        resultData[index] = row

    else:
        resultValue[index] = -ONE
        ret.setValue(ONE)
        ret.setMessage()

    return ret


# In[ ]:


def deleteNaN(data, index, resultData, resultValue, args) -> ReturnValue:
    ret = ReturnValue(ZERO)

    # Check if the main parameters are all given.
    if (data.getData() is not None and data.getWordColumn() is not None):
        row = pd.DataFrame(
            data = [data.getData().iloc[index]], 
            columns = data.getData().columns
        ).reset_index(drop = True)

        resultValue[index] = ZERO

        remove = all(row.isna()[data.getWordColumn()])

        if (row is None or remove):
                row = None
                resultValue[index] = ONE
        
        resultData[index] = row
    else:
        resultValue[index] = -ONE
        ret.setValue(ONE)
        ret.setMessage()

    return ret


# In[ ]:


def deleteCharacters(data, index, resultData, resultValue, args) -> ReturnValue:
    ret = ReturnValue(ZERO)

    # Check if the main parameters are all given.
    if (data.getData() is not None and data.getWordColumn() is not None):
        row = pd.DataFrame(
            data = [data.getData().iloc[index]], 
            columns = data.getData().columns
        ).reset_index(drop = True)

        resultValue[index] = ZERO

        if (row is not None):
            word = row[data.getWordColumn()][ZERO]

            if (word is not None and args is not None):

                for character in args:
                    word = word.replace(character, EMPTYSTRING)

                if (row[data.getWordColumn()][ZERO] != word):
                    row.loc[ZERO, data.getWordColumn()] = word
                    resultValue[index] = ONE

        resultData[index] = row
            
    else:
        resultValue[index] = -ONE
        ret.setValue(ONE)
        ret.setMessage()

    return ret


# In[ ]:


def deleteWords(data, index, resultData, resultValue, args) -> ReturnValue:
    ret = ReturnValue(ZERO)

    # Check if the main parameters are all given.
    if (data.getData() is not None and data.getWordColumn() is not None):
        row = pd.DataFrame(
            data = [data.getData().iloc[index]], 
            columns = data.getData().columns
        ).reset_index(drop = True)

        resultValue[index] = ZERO

        if (row is not None):
            word = row[data.getWordColumn()][ZERO]

            if (word is not None and args is not None and word in args):
                row = None
                resultValue[index] = ONE

        resultData[index] = row
             
    else:
        resultValue[index] = -ONE
        ret.setValue(ONE)
        ret.setMessage()

    return ret


# In[ ]:


def replaceBIOFormat(data, index, resultData, resultValue, args) -> ReturnValue:
    ret = ReturnValue(ZERO)

    # Check if the main parameters are all given.
    if (data.getData() is not None and data.getLabelColumn() is not None):
        row = pd.DataFrame(
            data = [data.getData().iloc[index]], 
            columns = data.getData().columns
        ).reset_index(drop = True)

        resultValue[index] = ZERO

        if (row is not None):
            label = row[data.getLabelColumn()][ZERO]
            
            if (args is not None and args[ZERO] is not None and 
                label is not None and label in args[ZERO].keys()):
                row.loc[ZERO, data.getLabelColumn()] = args[ZERO][label]
                resultValue[index] = ONE
            
        resultData[index] = row
    else:
        resultValue[index] = -ONE
        ret.setValue(ONE)
        ret.setMessage()

    return ret


# In[6]:


"""
This function splits the word in <data.getData()> on index <rowIndex> at every 
encounter of <splitString>. The result is a data frame which has the same 
columns as <data.getData()> having the splits of the word and the <splitString> as 
single rows in the column <data.wordColumn> saved in results.

Example:

The string "Low-and-Middle-Income" if splitted at the character "-" will result
in a data frame with seven rows containing "Low", "-", "and", "-", "Middle", 
"-", and "Income" as words. Every other entry of that row will be copied.

The created data frame will be stored in the given parameter <results> at 
<rowIndex>, therefore <results> needs to have the same size as <data.getData()>.
Additionally, the data in <results> is always copy of the data.  

data: an object of the type Data where the words are stored.
results: a list with the same length as <data.getData()> where the results are
    stored. The element contained in this list on the given index is 
    overwritten.
rowIndex: an index between zero an the length of <data.getData()>. The word which 
    will be splitted is located on this index.
splitString: the string where the word will be splitted. 
return: zero if everything went well,
    one if one of the parameters or needed variables in the parameters is None,
    two, if <rowIndex> is negative, larger than the length of <data.getData()>, or
        <result> and <data.getData()> have not the same length.
    three, if the row is None,
    four, if the word is None
"""
def splitAtIndex(data, index, resultData, resultValue, args) -> ReturnValue:
    ret = ReturnValue(ZERO)
    resultValue[index] = -ONE

    # Check if the main parameters are all given.
    if (data.getData() is not None and data.getWordColumn() is not None 
        and args is not None):

        columns = data.getData().columns
        row = data.getData().iloc[index]
        row = (pd.DataFrame(data = [row], columns = columns).
            reset_index(drop = True))
        columns = row.columns

        if (row is not None):

            word = str(row[data.getWordColumn()][ZERO])
            splitString = args[ZERO]

            # Check if there is a string which could be splitted.
            if (word is not None and splitString is not None):

                # If the string is shorter or has the same length as 
                # <splitString>, there is nothing to do and the row is just
                # copied.
                if (len(word) > len(splitString)):
                    splits = word.split(splitString)
                    count = len(splits)

                    # If there is more than just one split, an extra data
                    # frame needs to be created and filled with the
                    # data.
                    if (count > ONE):

                        # Doubling the splits.
                        splits = list(itertools.chain.from_iterable(
                            zip(splits, splits)))
                        
                        count = count * TWO
                        
                        # Replace every second element with the 
                        # <splitString>.
                        splits[ONE::TWO] = (splitString * 
                            math.floor(count / TWO))
                        
                        # Remove the last <splitString>, since it was never
                        # there.
                        splits = splits[ZERO:count - ONE]

                        count = count - ONE

                        # Create the new data frame containing the same
                        # data as <row>. 
                        resultData[index] = pd.DataFrame(
                            data = [row.iloc[ZERO]] * count, 
                            columns = columns).reset_index(drop = True)
                        
                        # Replacing the strings in the column
                        # <data.wordColumn> with the splits.
                        resultData[index][data.getWordColumn()] = splits
                        resultValue[index] = ONE
                    else:
                        resultData[index] = row
                        resultValue[index] = ZERO
                else:
                    resultData[index] = row
                    resultValue[index] = ZERO
            else:
                ret.setValue(THREE)
                ret.setMessage()
        else:
            ret.setValue(TWO)
            ret.setMessage()
    else:
        ret.setValue(ONE)
        ret.setMessage()

    return ret

