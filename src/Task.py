#!/usr/bin/env python
# coding: utf-8

import multiprocessing
import pandas as pd
import os
import os.path

from Values                              import *
from Utils                               import *
from Data                                import *
from MultiprocessFunctions               import *
from Logger                              import *

"""
This class takes care of a task one can perform on one or multiple files.

By specifying the function which will be executed on each row of the files,
the additional arguments of the function, the name of the task, experiment, and
run as well as input and output file(s) the data in the input file is 
manipulated and written in the output file. 

On each row in the input file(s) the given function is performed with the given
additional arguments. The function can be a self developed function.

For each given input file a process will be created dealing with the data
manipulation. This class will take care of creating the directories, processes,
and managing the prints. Be sure, that a logger (Logger.ipynb) has been created
before performing tasks since it will be used for logging. 
"""
class Task:
    
    # The List of tasks where this task belongs to.
    __taskList = None

    # The name of the task. This name will be used to name folders and columns.
    __taskName = None

    # Just the names e. g. "data.csv", "biodata.csv", "labdata.csv" etc. 
    # These files need to be stored in:
    # ./<EXPERIMENTSFOLDER>/<experimentName>/<runName>/<taskName>/
    #   <INPUTFOLDER>/
    __inputFiles  = list()
    # These files need to be stored in:
    # ./<EXPERIMENTSFOLDER>/<experimentName>/<runName>/<taskName>/
    #   <OUTPUTFOLDER>/
    __outputFiles = list()

    # The function which will be applied to all rows of the input files.
    __fun = None
    # The additional arguments for the function.
    __args = None

    # If outputfiles are already available, should the task be skipped?
    __skipIfAlreadyDone = False

    # The list of processes which have been started.
    __processList = list()

    """
    
    """
    def __init__(self, taskList = None):
        self.__taskList = taskList
        self.__inputFiles = list()
        self.__outputFiles = list()
        self.__taskName = None
        self.__fun = None
        self.__args = None
        self.__skipIfAlreadyDone = False
        self.__processList = list()

    """
    
    """
    def setStandardFiles(self, fileCount: int = ONE) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if (fileCount >= ONE):
            index = ZERO
            while(index < fileCount and ret.getValue() == ZERO):
                addFile = self.addFile(INPUTFILENAME.format(index), OUTPUTFILENAME.format(index))
                if (addFile.getValue() < ZERO):
                    ret.setValue(-ONE)
                    ret.setMessage(TASK_SETSTANDARDFILES_couldNotAddFile.
                        format(self.__taskName))
                    ret.addRoot(addFile)
                index += ONE
        else:
            ret.setValue(ONE)
            ret.setMessage(TASK_SETSTANDARDFILES_invalidFileCount.
                format(self.__taskName))

        return ret

    """
    Sets the name of the task.

    return: ZERO if everything went well,
        ONE if a previous name has been overwritten,
        -ONE if <taskName> is None.
    """
    def setTaskName(self, taskName: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if taskName is not None:
            if self.__taskName is not None:
                ret.setValue(ONE)
                ret.setMessage(TASK_SETTASKNAME_taskNameReplaced.
                    format(self.__taskName, taskName))
            self.__taskName = str(taskName)
        else:
            ret.setValue(-ONE)
            ret.setMessage(TASK_SETTASKNAME_taskNameNotValid)
            ret.setCritical()

        return ret

    """
    
    """
    def setSkipIfAlreadyDone(self, skip: bool = False):
        self.__skipIfAlreadyDone = skip

    """
    
    """
    def getTaskList(self):
        return self.__taskList

    """
    
    """
    def getSkipIfAlreadyDone(self) -> bool:
        return self.__skipIfAlreadyDone
    
    """
    
    """
    def getTaskName(self) -> str:
        return self.__taskName
    
    """
    
    """
    def getInputFileList(self) -> list:
        return self.__inputFiles
    
    """
    
    """
    def getOutputFileList(self) -> list:
        return self.__outputFiles
    
    """
    
    """
    def getFunction(self):
        return self.__fun
    
    """
    
    """
    def getArguments(self) -> tuple:
        return self.__args
    
    """
    
    """
    def getInputFile(self, index: int = 0) -> str:
        ret = None

        if index >= ZERO and index < len(self.__inputFiles):
            ret = self.__inputFiles[index]

        return ret
    
    """
    
    """
    def getOutputFile(self, index: int = 0) -> str:
        ret = None

        if index >= ZERO and index < len(self.__outputFiles):
            ret = self.__outputFiles[index]

        return ret

    """
    Sets the function which will be executed on every row. This needs to be a
    function which accepts the following parameters:

    def somePersonalFunction(data, index, result, *args):

    <data> is an object of type "Data" (see Data.ipynb), <index> is the index of
    the row on which the task should be performed, <result> is an array which 
    contains a Data Frame on each index. <result> at index <index> contains the
    Data Frame which will replace the row in data at index <index>. <result> at 
    index <index> can and should be changed in the funtion 
    <somePersonalFunction>. If nothing is performed, please copy the row in the 
    <result> array. Please do not change anything in the <data> or any other 
    Data Frame in <result> but that on index <index>. <*args> are the 
    additional arguments given to the function <somePersonalFuntion> and is 
    usually a tuple, the function should return an integer value which will be 
    added to the data as column using the columnname <taskName>.  

    return: ZERO if everything went well,
        ONE if a function which was already set has been replaced,
        -ONE if the given funtion in the paramter list is None,
        -TWO if the <fun> is not callable.
    """
    def setFunction(self, fun = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if fun is not None:
            if callable(fun):
                if self.__fun is not None:
                    ret.setValue(ONE)
                    ret.setMessage(TASK_SETFUNCTION_functionReplaced.
                        format(self.__fun.__name__, fun.__name__))
                self.__fun = fun
            else:
                ret.setValue(-TWO)
                ret.setMessage(TASK_SETFUNCTION_functionNotCallable.
                    format(self.__taskName))
        else:
            ret.setValue(-ONE)
            ret.setMessage(TASK_SETFUNCTION_functionNotValid.
                format(self.__taskName))

        return ret
    
    """
    Sets the additional arguments which the function set with setFunction(...)
    will get as parameters.

    return: ZERO if everything went well,
        ONE if the given args are None,
        TWO if args has been overwritten.
    """
    def setArguments(self, args: tuple) -> ReturnValue:
        ret = ReturnValue(ZERO)

        if args is not None:
            if self.__args is not None:
                ret.setValue(TWO)            
                ret.setMessage(TASK_SETARGUMENTS_argumentsReplaced.
                    format(self.__taskName))
            self.__args = args
        else:
            ret.setValues(ONE)
            ret.setMessage(TASK_SETARGUMENTS_argumentsNotValid.
                format(self.__taskName))

        return ret
    
    """
    Creates the folder structure:

    ./<EXPERIMENTSFOLDER>/<experimentName>/<runName>/<taskName>/<INPUTFOLDER>/
    ./<EXPERIMENTSFOLDER>/<experimentName>/<runName>/<taskName>/<OUTPUTFOLDER>/

    if it does not exist the folder structure will be created.

    The creation will fail if the <EXPERIMENTSFOLDER> is not already created.

    return: ZERO if everything went well,
        ONE if the <taskName> folder needed to be created, addtitionally also
            the <OUTPUTFOLDER> and <INPUTFOLDER> were created, 
        TWO if the <INPUTFOLDER> needed to be created,
        THREE if the <OUTPUTFOLDER> needed to be created,
        -ONE if the <experimentName> is None,
        -TWO if the <runName> is None,
        -THREE if the <experiment>-folder, <experimentName>-folder or 
            <runName>-folder could not be found,
        -FOUR if the <taskName> is None.
    """
    def createFolders(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        # Check if experiment and run name is set.
        if self.getTaskList().getExperimentName() is not None:
            if self.getTaskList().getRunName() is not None:

                checkPath = os.path.join(
                    EXPERIMENTSFOLDER, 
                    self.getTaskList().getExperimentName(),
                    self.getTaskList().getRunName())

                # The folders up to the run-folder need to exist already
                if os.path.isdir(checkPath):
                    
                    # Task name needs to be set to check further folders.
                    if self.getTaskName() is not None:
                        # Check if the <runName> folder exists, if not, create 
                        # it.
                        checkPath = os.path.join(checkPath, self.getTaskName())
                        if not os.path.isdir(checkPath):
                            os.mkdir(checkPath)
                            if ret.getValue() == ZERO:
                                ret.setValue(ONE)
                                ret.setMessage(TASK_CREATEFOLDERS_taskNameFolderCreated.
                                    format(self.__taskName))

                        # Check if the <INPUTFOLDER> folder exists, if not, 
                        # create it.
                        inputFolder = os.path.join(checkPath, INPUTFOLDER)
                        if not os.path.isdir(inputFolder):
                            os.mkdir(inputFolder)
                            if ret.getValue() ==  ZERO:
                                ret.setValue(TWO)
                                ret.setMessage(TASK_CREATEFOLDERS_inputFolderCreated.
                                    format(self.__taskName))

                        # Check if the <OUTPUTFOLDER> folder exists, if not, 
                        # create it.
                        outputFolder = os.path.join(checkPath, OUTPUTFOLDER)
                        if not os.path.isdir(outputFolder):
                            os.mkdir(outputFolder)
                            if ret.getValue() ==  ZERO:
                                ret.setValue(THREE)
                                ret.setMessage(TASK_CREATEFOLDERS_outputFolderCreated.
                                    format(self.__taskName))
                            else:
                                ret.setValue(FOUR)
                                ret.setMessage(TASK_CREATEFOLDERS_outputAndInputFolderCreated.
                                    format(self.__taskName))
                    else:
                        ret.setValue(-FOUR)
                        ret.setMessage(TASK_CREATEFOLDERS_taskNameNotValid)
                        ret.setCritical()
                else:
                    ret.setValue(-THREE)
                    ret.setMessage(TASK_CREATEFOLDERS_foldersNotExisting)
                    ret.setCritical()
            else:
                ret.setValue(-TWO)
                ret.setMessage(TASK_CREATEFOLDERS_runNameNotValid)
                ret.setCritical()
        else:
            ret.setValue(-ONE)
            ret.setMessage(TASK_CREATEFOLDERS_experimentNameNotValid)
            ret.setCritical()

        return ret

    """
    Checks if the directory is prepared for the task. All input files need to 
    exist and, as a consequence, every directory needs to exist. Additionally,
    the output directory needs to exist, but if the output files exist a 
    warning will be returned. 

    return: ZERO if everything went well,
        -ONE if the <experimentName> folder does not exist,
        -TWO if the <runName> folder does not exist, 
        -THREE if the <taskName> folder does not exist,
        -FOUR if one of the input files does not exist,
        -FIVE if the output folder does not exist
        ONE if one of the output files does exist.
    """
    def checkDirsAndFiles(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        # Check if experiment, run, and task name is set.
        if (self.getTaskList().getExperimentName() is not None):
            if (self.getTaskList().getRunName() is not None):
                if (self.getTaskName() is not None):

                    # Is every input file available? If yes, also the folders
                    # do exist.
                    for inputFile in self.getInputFileList():
                        if (not os.path.isfile(inputFile)):
                            ret.setValue(-FOUR)
                            ret.setMessage(TASK_CHECKDIRSANDFILES_inputFileNotExists.
                                format(self.__taskName))
                            ret.setCritical()

                    # Chekc if the output folders exist and check if the
                    # output files do exist.
                    if ret.getValue() == ZERO:
                        outputFileDir = os.path.join(EXPERIMENTSFOLDER,
                                self.getTaskList().getExperimentName(), 
                                self.getTaskList().getRunName(), 
                                self.getTaskName(),
                                OUTPUTFOLDER)
                        
                        if (not os.path.isdir(outputFileDir)):
                            ret.setValue(-FIVE)
                            ret.setMessage(TASK_CHECKDIRSANDFILES_outputDirNotExists.
                                format(self.__taskName))
                            ret.setCritical()
                        else:
                            for outputFile in self.getOutputFileList():
                                if (ret.getValue() == ZERO and os.path.isfile(outputFile)):
                                    ret.setValue(ONE)
                                    ret.setMessage(TASK_CHECKDIRSANDFILES_outputFileExists.
                                        format(self.__taskName))
                else:
                    ret.setValue(-THREE)
                    ret.setMessage(TASK_CHECKDIRSANDFILES_taskNameNotValid)
                    ret.setCritical()
            else:
                ret.setValue(-TWO)
                ret.setMessage(TASK_CHECKDIRSANDFILES_runNameNotValid)
                ret.setCritical()
        else:
            ret.setValue(-ONE)
            ret.setMessage(TASK_CHECKDIRSANDFILES_experimentNameNotValid)
            ret.setCritical()

        return ret
    
    """
    Adds the input file and output file to the lists of input and output files.
    The given parameters are denoting only the file names, without any
    directory name as prefix e.g. "data.csv", "result.csv" etc. The directory
    name will be added to the file name in this method, therefore the 
    name of the experiment, the name of the run and the name of the task
    need to be set. 

    Checks regarding the existence of certain folder need to be done to make
    sure that everything is prepared when starting the task. 

    return: ZERO if everything went well,
        -ONE if the <inputFile> or <outputFile> is None, 
        -TWO if the <experimentName> is not set,
        -THREE if the <runName> is not set,
        -FOUR if the <taskName> is not set.
    """
    def addFile(self, inputFile: str = None, outputFile: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        # Check if input and output files are given.
        if inputFile is not None and outputFile is not None:
            # Check if the folder structure is as expected.
            if self.getTaskList().getExperimentName() is not None:    
                if self.getTaskList().getRunName() is not None:
                    if self.getTaskName() is not None:
                        inputFileDir = os.path.join(EXPERIMENTSFOLDER, 
                            self.getTaskList().getExperimentName(), 
                            self.getTaskList().getRunName(), 
                            self.getTaskName(), 
                            INPUTFOLDER, 
                            inputFile)
                        
                        outputFileDir = os.path.join(EXPERIMENTSFOLDER,
                            self.getTaskList().getExperimentName(), 
                            self.getTaskList().getRunName(), 
                            self.getTaskName(),
                            OUTPUTFOLDER, 
                            outputFile)

                        self.getInputFileList().append(inputFileDir)
                        self.getOutputFileList().append(outputFileDir)
                    else:
                        ret.setValue(-FOUR)
                        ret.setMessage(TASK_ADDFILE_taskNameNotValid)
                        ret.setCritical()
                else:
                    ret.setValue(-THREE)
                    ret.setMessage(TASK_ADDFILE_runNameNotValid)
                    ret.setCritical()
            else:
                ret.setValue(-TWO)
                ret.setMessage(TASK_ADDFILE_experimentNameNotValid)
                ret.setCritical()
        else:
            ret.setValue(-ONE)
            ret.setMessage(TASK_ADDFILE_parametersNotValid)
            ret.setCritical()

        return ret
    
    
    
    """
    If this column exists already it 
    will be overwritten. With the return value of <somePersonalFunction> it is 
    possible to track the changes in the data e.g. if the function changed a 
    row, ONE can be returned, if nothing changed, ZERO can be returned, if 
    some error occured TWO can be returned and so on.

    return: ZERO if everything went well,
        ONE if there are no input files,
        TWO if the task will be skipped because some output files have been 
            found, 
        -ONE if the directories or files are not available,
        -TWO if <wordColumn> or <labelColumn> are not set.
    """
    def start(self) -> ReturnValue:
        ret = ReturnValue(ZERO)

        # Check if there is something to do.
        if (self.getInputFileList() is not None and 
            len(self.getInputFileList()) > ZERO and
            self.getOutputFileList() is not None and
            len(self.getOutputFileList()) > ZERO):

            # Check if the files are available.
            check = self.checkDirsAndFiles()
            if (check.getValue() == ZERO or (check.getValue() > ZERO and 
                not self.getSkipIfAlreadyDone())):

                if (check.getValue() > ZERO):
                    ret.setValue(THREE)
                    ret.setMessage(TASK_START_overwritingOutput.
                        format(self.getTaskName()))

                # Check if there is enough information to do something.
                if (self.getTaskList().getWordColumn() is not None):
                    if (self.getTaskList().getLabelColumn() is not None):

                        count = len(self.getInputFileList())

                        # Start processes. 
                        for index in range(ZERO, count):

                            args = (self, index)

                            process = multiprocessing.Process(
                                target = singleProcessingFunction,
                                args = args
                            )
                            process.start()
                            self.__processList.append(process)
                    else:
                        ret.setValue(-THREE)
                        ret.addRoot(check)
                        ret.setCritical()
                        ret.setMessage(TASK_START_columnLabelNotSet.
                            format(self.getTaskName()))
                else:
                    ret.setValue(-TWO)
                    ret.addRoot(check)
                    ret.setCritical()
                    ret.setMessage(TASK_START_columnWordNotSet.
                        format(self.getTaskName()))
            else:
                ret.addRoot(check)
                if (check.getValue() < ZERO):
                    ret.setValue(-ONE)
                    ret.setMessage(TASK_START_directoryAndFileCheckFailed.
                        format(self.getTaskName()))
                    ret.setCritical()
                else:
                    if (check.getValue() == ONE):
                        ret.setValue(TWO)
                        ret.setMessage(TASK_START_skippingTask.
                            format(self.getTaskName()))
                    else:
                        ret.setValue(FOUR)
                        ret.setMessage(TASK_START_unknownWarning.
                            format(self.getTaskName()))
        else:
            ret.setValue(ONE)
            ret.setMessage(TASK_START_nothingToDo.
                format(self.getTaskName()))
            
        return ret
    
    """
    
    """
    def join(self):
        for process in self.__processList:
            process.join()


# In[5]:


"""
With this function one of the processes of a task starts it's work. As
parameters the function requires the task and the index of input and output
data. This function is not for general, but just for internal usage. Please
do not execute this function in your code. 
"""
def singleProcessingFunction(task: Task = None, fileindex: int = None):
    
    # First the data needs to be loaded.
    data = Data()

    Logger.getSingletonLogger().printInfo(loadingDataInfo.format(
        task.getInputFile(fileindex)))
    
    # Loading the data from the file. If an error occurs, the process will
    # be stopped. If a warning occurrs the process needs to be stopped 
    loadData = data.loadCSVData(task.getInputFile(fileindex))
    if (loadData.getValue() != ZERO):
        loadData.eval()
    else:
        # This varaibles are not necessary, therefore if the value is not set
        # the task can still be performed.
        data.setDocumentIDColumn(task.getTaskList().getDocumentIDColumn()). \
            eval()

        data.setSentenceIDColumn(task.getTaskList().getSentenceIDColumn()). \
            eval()

        data.setWordIDColumn(task.getTaskList().getWordIDColumn()).eval()

        # This two columns need to be set to perform the task.
        setWordColumn = data.setWordColumn(task.getTaskList().getWordColumn())
        setLabelColumn = data.setLabelColumn(task.getTaskList().getLabelColumn())

        if (setWordColumn.getValue() != ZERO):
            setWordColumn.eval()
        else: 
            if (setLabelColumn.getValue() != ZERO):
               setWordColumn.eval()
            else:
                #
                returnValue = [None] * (data.getRowCount())
                resultData  = [None] * (data.getRowCount())
                resultValue = [None] * (data.getRowCount()) 

                Logger.getSingletonLogger().printInfo(loadedDataInfo.format(
                    data.getRowCount(), data.getColumnCount()))
                Logger.getSingletonLogger().startPrintProgress(data.getRowCount())

                for index in range(ZERO, data.getRowCount()):
                    
                    returnValue[index] = task.getFunction()(
                        data, 
                        index, 
                        resultData, 
                        resultValue,
                        task.getArguments()
                    )
                    
                    if (resultData[index] is not None):
                        resultData[index].insert(data.getColumnCount(), 
                            task.getTaskName(),
                            [resultValue[index]] * len(resultData[index]), 
                            allow_duplicates = True)

                    if (returnValue[index].getValue() != ZERO):
                        val = ReturnValue(ONE)
                        val.setMessage(SINGLEPROCESSINGFUNCTION_returnValueNotZero.format
                            (index, task.getTaskName(), returnValue[index].getValue(), \
                            returnValue[index].getMessage()))
                        val.addRoot(returnValue[index])
                        val.eval()
                            
                    Logger.getSingletonLogger().printProgress()

                Logger.getSingletonLogger().printInfo(writeResultToFile.format(
                    task.getOutputFile(fileindex)))
                Logger.getSingletonLogger().startPrintProgress(data.getRowCount())

                # Empty file before using.
                open(task.getOutputFile(fileindex), WRITE).close()

                # Write all data frames one after the other, but just write the header of 
                # the first one. 
                with open(task.getOutputFile(fileindex), APPENDTOFILE) as file:
                    header = True
                    for res in resultData:
                        Logger.getSingletonLogger().printProgress()
                        if res is not None:
                            res.to_csv(file, header = header, index = False)
                            header = False

                Logger.getSingletonLogger().printInfo(processEnded.format(
                    task.getTaskName(), task.getOutputFile(fileindex)))


# In[4]:


def testProcessingFunction(data, index, resultData, resultValue, args) -> ReturnValue:
    ret = ReturnValue(ZERO)

    count = args[ZERO]
    if (count is None or count < ONE):
        count = TWO
        resultValue[index] = ONE
    else:
        resultValue[index] = ZERO

    resultData[index]  = pd.DataFrame(
        data = [data.getData().iloc[index]] * count,
        columns = data.getColumns()
    )

    return ret

