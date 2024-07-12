#!/usr/bin/env python
# coding: utf-8

import multiprocessing
import pandas as pd
import os
import shutil
import filecmp

from Values                              import *
from Utils                               import *
from Data                                import *
from MultiprocessFunctions               import *
from Logger                              import *
from Task                                import *
from ReturnValue                         import *

"""

"""
class TaskList:

    # Variables used to save the name of the run and the experiment 
    __runName = None
    __experimentName = None
    
    # The most important column names are listed here, they will be given
    # as input to the data (Data.ipynb) object. This variables are also static.
    __wordColumn = None
    __labelColumn = None
    __wordIDColumn = None
    __documentIDColumn = None
    __sentenceIDColumn = None
    
    # List of task.
    __taskList = list()

    # The input data.
    __inputData = None

    # The output data.
    __outputData = None

    """
    
    """
    def __init__(self):
        self.__runName = None
        self.__experimentName = None
        self.__wordColumn = None
        self.__wordIDColumn = None
        self.__labelColumn = None
        self.__documentIDColumn = None
        self.__sentenceIDColumn = None
        self.__taskList = list()
        self.__inputData = None
        self.__outputData = None

    """
    
    """
    def setOutputData(self, outputData: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if (outputData is not None):
            if (self.__outputData is not None):
                ret.setValue(ONE)
                ret.setMessage(TASKLIST_SETOUTPUTDATA_overwritingOutputData.
                    format(outputData, self.__outputData))
            self.__outputData = outputData
        else:
            ret.setValue(-ONE)
            ret.setMessage(TASKLIST_SETOUTPUTDATA_noOutputDataGiven)
            ret.setCritical()

        return ret

    """
    
    """
    def setInputData(self, inputData: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if (inputData is not None):
            if (self.__inputData is not None):
                ret.setValue(ONE)
                ret.setMessage(TASKLIST_overwritingInputData.
                    format(inputData, self.__inputData))
            self.__inputData = inputData
        else:
            ret.setValue(-ONE)
            ret.setMessage(TASKLIST_noInputDataGiven)
            ret.setCritical()

        return ret
    
    """
    
    """
    def getInputFile(self) -> str:
        return self.__inputData

    """
    
    """
    def getTaskList(self) -> list:
        return self.__taskList
    
    """
    
    """
    def getTask(self, index: int = ZERO) -> Task:
        ret = None

        if index >= ZERO and index < len(self.getTaskList()):
            ret = self.getTaskList()[index]

        return ret

    """
    
    """
    def getRunName(self) -> str:
        return self.__runName
    
    """
    
    """
    def getExperimentName(self) -> str:
        return self.__experimentName
    
    """
    
    """
    def createFolders(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if self.getExperimentName() is not None:
            if self.getRunName() is not None:

                checkPath = os.path.join(EXPERIMENTSFOLDER)
                if os.path.isdir(checkPath):
                    checkPath = os.path.join(checkPath, 
                        self.getExperimentName())
                    
                    if not os.path.isdir(checkPath):
                        os.mkdir(checkPath)
                        ret.setValue(ONE)
                        ret.setMessage(TASKLIST_folderCreatedForThisExperiment.
                            format(self.getExperimentName(), self.getRunName()))

                    checkPath = os.path.join(checkPath, self.getRunName())
                    if not os.path.isdir(checkPath):
                        os.mkdir(checkPath)
                        if (ret.getValue() == ZERO):
                            ret.setValue(TWO)
                            ret.setMessage(TASKLIST_folderCreatedForThisRun.
                                format(self.getRunName()))
                            
                    checkPathInputFolder = os.path.join(checkPath, TASKLIST_INPUT_FOLDER)
                    checkPathOutputFolder = os.path.join(checkPath, TASKLIST_OUTPUT_FOLDER)

                    if not os.path.isdir(checkPathInputFolder):
                        os.mkdir(checkPathInputFolder)
                        if (ret.getValue() == ZERO):
                            ret.setValue(THREE)
                            ret.setMessage(TASKLIST_inputFolderForRunCreated.
                                format(self.getRunName()))
                            
                    if not os.path.isdir(checkPathOutputFolder):
                        os.mkdir(checkPathOutputFolder)
                        if (ret.getValue() == ZERO):
                            ret.setValue(FOUR)
                            ret.setMessage(TASKLIST_outputFolderForRunCreated.
                                format(self.getRunName()))

                else:
                    ret.setValue(-THREE)
                    ret.setMessage(TASKLIST_noExperimentFolderCreated)
                    ret.setCritical()
            else:
                ret.setValue(-TWO)
                ret.setCritical()
                ret.setMessage(TASKLIST_noRunNameSet)
                
        else:
            ret.setValue(-ONE)
            ret.setCritical()
            ret.setMessage(TASKLIST_noExperimentNameSet)

        return ret 

    """
    
    """
    def start(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if (len(self.getTaskList()) > ZERO):

            createDirs = self.createFolders()
            if (createDirs.getValue() >= ZERO):

                if (createDirs.getValue() > ZERO):
                    ret.addRoot(createDirs)
                    ret.setValue(TWO)
                    ret.setMessage(TASKLIST_START_createDirsWarning)

                index = ZERO
                while(index < len(self.getTaskList()) and 
                    ret.getValue() >= ZERO):
                    task = self.getTask(index = index)

                    createDirs = task.createFolders()
                    if (createDirs.getValue() >= ZERO):
                        createDirs.eval()

                        Logger.getSingletonLogger().printInfo(
                                TASKLIST_startingTask.format(task.getTaskName()))

                        # First Task
                        if (index == ZERO):

                            # Check if input file has the same content as 
                            # the file stored in the 

                            Logger.getSingletonLogger().printInfo(
                                TASKLIST_splittingDataForTask)
                            
                            split = self.splitInputData(task.getInputFileList())

                            if (split.getValue() < ZERO):
                                ret.setValue(-THREE)
                                ret.setMessage(TASKLIST_splitDataFailed.
                                    format(task.getTaskName()))
                                ret.setCritical()
                                ret.addRoot(split)
                        else:
                            Logger.getSingletonLogger().printInfo(
                                copyDataForNextTask)

                            copy = self.copyData(
                                self.getTask(index - ONE).getOutputFileList(), 
                                task.getInputFileList())
                            
                            if (copy.getValue() != ZERO):
                                ret.setValue(-FOUR)
                                ret.setCritical()
                                ret.setMessage(TASKLIST_copyDataFailed.
                                    format(task.getTaskName()))
                                ret.addRoot(copy)

                        
                        doTask = task.start()

                        if (doTask.getValue() < ZERO):
                            ret.setValue(-FIVE)
                            ret.setCritical()
                            ret.setMessage(TASKLIST_taskFailed.
                                format(task.getTaskName()))
                            ret.addRoot(doTask)
                        else:
                            doTask.eval()
                            task.join()

                            if (index == len(self.getTaskList()) - ONE):

                                Logger.getSingletonLogger().printInfo(
                                    TASKLIST_START_startingMerging.format(
                                    len(task.getOutputFileList()), 
                                    self.__outputData))

                                merge = self.mergeOutputData(task.
                                    getOutputFileList())
                                
                                if (merge.getValue() < ZERO):
                                    ret.setValue(-SIX)
                                    ret.setMessage(
                                        TASKLIST_START_errorWhileMergingOutput.
                                        format(self.__outputData))
                                    ret.setCritical()
                                    ret.addRoot(merge)
                                else:
                                    if (merge.getValue() > ZERO):
                                        ret.setValue(THREE)
                                        ret.setMessage(
                                            TASKLIST_START_warningWhileMergingOutput.
                                            format(self.__outputData))
                                        ret.addRoot(merge)

                    else:
                        ret.setValue(-TWO)
                        ret.setMessage(TASKLIST_START_couldNotCreateTaskFolder.
                            format(task.getTaskName()))
                        ret.setCritical()
                        ret.addRoot(createDirs)

                    index += ONE
            else:
                ret.setValue(-ONE)
                ret.addRoot(createDirs)
                ret.setMessage(TASKLIST_START_couldNotCreateTasklistFolder)
        else:
            ret.setValue(ONE)
            ret.setMessage(TASKLIST_noTaskInTaskList)
        return ret

    """
    
    """
    def splitInputData(self, files: list = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        data = Data()
        load = data.loadCSVData(self.__inputData)

        if (load.getValue() == ZERO):
            split = data.splitUp(files)
            if (split.getValue() != ZERO):
                ret.setValue(-TWO)
                ret.setCritical()
                ret.setMessage(TASKLIST_failedToSplitData.
                    format(self.getInputData()))
                ret.addRoot(split)
        else:
            ret.setValue(-ONE)
            ret.setCritical()
            ret.setMessage(TASKLIST_failedToLoadData.
                format(self.getInputData()))
            ret.addRoot(load)

        return ret
    
    """
    
    """
    def mergeOutputData(self, files: list = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if (files is not None):

            if (self.__outputData is not None):

                index = ZERO
                while(index < len(files) and ret.getValue() >= ZERO):
                    file = files[index]
                    data = Data()
                    load = data.loadCSVData(file)

                    if (load.getValue() == ZERO):

                        header = False
                        open = APPENDTOFILE
                        if (index == ZERO):
                            open = WRITE
                            header = True

                        write = data.writeCSVData(self.__outputData, open, 
                            header = header)
                        
                        if (write.getValue() < ZERO):
                            ret.setValue(-THREE)
                            ret.setRoot(write)
                            ret.setMessage(TASKLIST_MERGEOUTPUTDATA_errorWhileWritingData.
                                format(self.__outputData))
                            ret.setCritical()
                        else:
                            if (write.getValue() > ZERO and index == ZERO):
                                ret.setValue(TWO)
                                ret.setMessage(TASKLIST_MERGEOUTPUTDATA_warningWhileWritingData.
                                    format(self.__outputData))
                                ret.addRoot(write)

                    else:
                        ret.setValue(-ONE)
                        ret.setCritical()
                        ret.setMessage(TASKLIST_MERGEOUTPUTDATA_couldNotLoadData.
                            format(file))
                        ret.addRoot(load)
                    
                    index += ONE
            else:
                ret.setValue(-TWO)
                ret.setCritical()
                ret.setMessage(TASKLIST_MERGEOUTPUTDATA_noOutputDataGiven)

        else:
            ret.setValue(ONE)
            ret.setMessage(TASKLIST_MERGEOUTPUTDATA_noInputFilesGiven)

        return ret

    
    def getInputData(self) -> str:
        return self.__inputData
    
    """
    
    """
    def copyData(self, fromFiles: list, toFiles: list) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if (len(fromFiles) == len(toFiles)):
            for index in range(ZERO, len(fromFiles)):
                shutil.copy2(fromFiles[index], toFiles[index])
        else:
            ret.setValue(-ONE)
            ret.setCritical()
            ret.setMessage(TASKLIST_sourceAndTargetNotTheSameLength.
                format(len(toFiles), len(fromFiles)))

        return ret
    
    """
    
    """
    def newTask(self, taskName: str = None, 
            fun = None, *args:tuple) -> ReturnValue:
        ret = ReturnValue(ZERO)
        nTask = Task(self)
        
        retSetFun = nTask.setFunction(fun)
        if (retSetFun.getValue() != ZERO):
            ret.setValue(-ONE)
            ret.setMessage(TASKLIST_createNewTaskNoFunction)
            ret.addRoot(retSetFun)
        else:
            retSetArg = nTask.setArguments(args)

            if (retSetArg.getValue() != ZERO):
                ret.setValue(-TWO)
                ret.setMessage(TASKLIST_createNewTaskNoArguments)
                ret.addRoot(retSetArg)
            else:
                retSetTaskName = nTask.setTaskName(taskName)

                if (retSetTaskName.getValue() != ZERO):
                    ret.setValue(-THREE)
                    ret.setMessage(TASKLIST_createNewTaskNoTaskName.
                        format(taskName))
                    ret.addRoot(retSetTaskName)
                else:
                    self.getTaskList().append(nTask)
        
        return ret
    
    """
    
    """
    def getWordColumn(self) -> str:
        return self.__wordColumn
    
    """
    
    """
    def getWordIDColumn(self) -> str:
        return self.__wordIDColumn
    
    """
    
    """
    def getLabelColumn(self) -> str:
        return self.__labelColumn
    
    """
    
    """
    def getDocumentIDColumn(self) -> str:
        return self.__documentIDColumn
    
    """
    
    """
    def getSentenceIDColumn(self) -> str:
        return self.__sentenceIDColumn

    """
    Sets the name of the run.

    return: ZERO if everything went well,
        ONE if a previous name has been overwritten,
        -ONE if <runName> is None.
    """
    def setRunName(self, runName: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if runName is not None:
            if self.getRunName() is not None:
                ret.setValue(ONE)
                ret.setMessage(TASKLIST_SETRUNNAME_replaceRunName.
                    format(self.getRunName(), runName))
            self.__runName = runName
        else:
            ret.setValue(-ONE)
            ret.setMessage(TASKLIST_SETRUNNAME_invalidRunName)
            ret.setCrititcal()

        return ret
    
    """
    Returns the next possible name of the run. Runs are usually named with a
    number denoting the run number e.g. "00012". With this format it is easy to
    sort the folders. If the folder structure is different the return value
    might not have the same format as the names of the other folders.
    The return value is the suggested name for the run name and it is also 
    checked if the folder is not already created.
    
    return: None if the experiment name folder could not be found or the folder
            having as name the next suggested name exists already,
        not None the name of the next run.
    """
    def getNextRunName(self) -> str:
        ret = None

        # Check if the <EXPERIMENTSFOLDER> folder exists, if not, an error is
        # returned.
        # Check if the <experimentName> folder exists, if not, "1" is
        # returned.
        if os.path.isdir(EXPERIMENTSFOLDER) and self.getExperimentName() is not None:
            checkPath = os.path.join(EXPERIMENTSFOLDER, 
                self.getExperimentName())
            if os.path.isdir(checkPath):
                ret = len(next(os.walk(checkPath))[ONE]) + ONE

                if ret is not None and ret < TENTHOUSEND:
                    ret = ret.zfill(FIVE)

                    if os.path.isdir(os.path.join(checkPath, ret)):
                        ret = None
                else:
                    ret = None
        
        return ret
    
    """
    Sets the name of the experiment.

    return: ZERO if everything went well,
        ONE if a previous name has been overwritten,
        -ONE if <experimentName> is None.
    """
    def setExperimentName(self, experimentName: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if experimentName is not None:
            if self.getExperimentName() is not None:
                ret = ONE
            self.__experimentName = experimentName
        else:
            ret = -ONE

        return ret
    
    """
    This method sets the most important column names which will be given as 
    input to the data (Data.ipynb) object.

    All parameter are converted to strings.

    wordColumn: the name of the column in which the words are stored.
    labelColumn: the name of the column in which the labels or tags are stored.
    wordIDColumn: the name of the column in which the IDs of the words are
        stored. 
    documentIDColumn: the name of the column in which the IDs of the documents
        are stored, denoting sentences which belong together.
    sentenceIDColumn: the name of the column in which the IDs of the sentences
        are stored.
    return: ZERO if everything went well,
        -ONE if <wordColumn> was None or had zero length,
        -TWO if <labelColumn> was None or had zero length, 
        ONE if <wordIDColumn> was None or had zero length,
        TWO if <wordIDColumn> was None or had zero length,
        THREE if <documentIDColumn> was None or had zero length 
    """
    def setColumns( self, wordColumn: str, labelColumn: str, 
                    wordIDColumn: str = None, documentIDColumn: str = None, 
                    sentenceIDColumn: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        # <wordColumn> and <labelColumn> are essential for named entity
        # recognition and therefore need to be set.
        if wordColumn is not None or len(wordColumn) < ONE:
            self.__wordColumn = wordColumn
            if labelColumn is not None or len(labelColumn) < ONE:
                self.__labelColumn = labelColumn
                if wordIDColumn is not None or len(wordIDColumn) < ONE:
                    self.__wordIDColumn = wordIDColumn  
                    if sentenceIDColumn is not None or len(sentenceIDColumn) < ONE:
                        self.__sentenceIDColumn = sentenceIDColumn
                        if documentIDColumn is not None or len(documentIDColumn) < ONE:
                            self.__documentIDColumn = documentIDColumn
                        else:
                            ret.setValue(THREE)
                            ret.setMessage(TASKLIST_SETCOLUMNS_noDocumentIDColumn)
                    else:
                        ret.setValue(TWO)
                        ret.setMessage(TASKLIST_SETCOLUMNS_noSentenceIDColumn)
                else:
                    ret.setValue(ONE)
                    ret.setMessage(TASKLIST_SETCOLUMNS_noWordIDColumn)
            else:
                ret.setValue(-TWO)
                ret.setCritical()
                ret.setMessage(TASKLIST_SETCOLUMNS_noLabelColumn)
        else:
            ret.setValue(-ONE)
            ret.setMessage(TASKLIST_SETCOLUMNS_noWordColumn)
            ret.setCritical()

        return ret


# %%
