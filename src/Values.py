#!/usr/bin/env python
# coding: utf-8

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
TEN = 10
TWENTY = 20
TWENTYFOUR = 24
SIXTY = 60
HUNDRED = 100
THOUSEND = 1000
ONEHUNDREDTWENTYEIGHT = 128
SPACE = " "
EMPTYSTRING = ""

NULL_STRINGS = ["null", "NA", "nan", ""]

EXPERIMENTSFOLDER = "./experiments"
INPUTFOLDER = "in"
OUTPUTFOLDER = "out"
STAR = "*"

TASKLIST_INPUT_FOLDER = "in"
TASKLIST_INPUT_FILE_NAME = "input.csv"
TASKLIST_OUTPUT_FOLDER = "out"
TASKLIST_OUTPUT_FILE_NAME = "output.csv"

CSVFILE = ".csv"
NEWLINE = "\n"
APPENDTOFILE = "a"
WRITE = "w"

UTF8 = "utf8"
ASCII = "ascii"
IGNORE = 'ignore'
LITTLE = "little"

MODEL_RESULT_WORD_COLUMN = "word"

TOKENSTARTCHARS = "##"

DEFAULT_COLUMN_NAME = "column"

INPUTFILENAME = "input{}.csv"
OUTPUTFILENAME = "output{}.csv"

EVAL_RETURNVALUE = "{} [Value: {}, Class: {}, Method: {}]"

RETURNVALUE_stdMsg = "Everything went well."
RETURNVALUE_noLoggerCreated = "There is no Logger which can be used to log something."
RETURNVALUE_loggingError = "An error ({}) occured while logging."

LOGGER_replacingLogger = "The new singleton logger is replacing another logger."



DEFAULTCOLUMNS = "DefaultColumns"



DEFAULTCOLUMNS_setDocumentIDColumn = "setDocumentIDColumn"
DEFAULTCOLUMNS_setDocumentIDColumn_replacedValue = "The column of the document ID changed it's value from \"{}\" to \"{}\"."
DEFAULTCOLUMNS_setDocumentIDColumn_parameterIsNone = "The given parameter for the document ID column is None."
DEFAULTCOLUMNS_setDocumentIDColumn_setValue = "The value of the document ID column has been set to \"{}\"."

DEFAULTCOLUMNS_setSentenceIDColumn = "setSentenceIDColumn"
DEFAULTCOLUMNS_setSentenceIDColumn_replacedValue = "The column of the sentence ID changed it's value from \"{}\" to \"{}\"."
DEFAULTCOLUMNS_setSentenceIDColumn_parameterIsNone = "The given parameter for the sentence ID column is None."
DEFAULTCOLUMNS_setSentenceIDColumn_setValue = "The value of the sentence ID column has been set to \"{}\"."

DEFAULTCOLUMNS_setWordColumn = "setWordColumn"
DEFAULTCOLUMNS_setWordColumn_replacedValue = "The column of the words changed it's value from \"{}\" to \"{}\"."
DEFAULTCOLUMNS_setWordColumn_parameterIsNone = "The given parameter for the word column is None."
DEFAULTCOLUMNS_setWordColumn_setValue = "The value of the word column has been set to \"{}\"."

DEFAULTCOLUMNS_setLabelColumn = "setLabelColumn"
DEFAULTCOLUMNS_setLabelColumn_replacedValue = "The column of the label changed it's value from \"{}\" to \"{}\"."
DEFAULTCOLUMNS_setLabelColumn_parameterIsNone = "The given parameter for the label column is None."
DEFAULTCOLUMNS_setLabelColumn_setValue = "The value of the label column has been set to \"{}\"."

DEFAULTCOLUMNS_setWordIDColumn = "setWordIDColumn"
DEFAULTCOLUMNS_setWordIDColumn_replacedValue = "The column of the word ID changed it's value from \"{}\" to \"{}\"."
DEFAULTCOLUMNS_setWordIDColumn_parameterIsNone = "The given parameter for the word ID column is None."
DEFAULTCOLUMNS_setWordIDColumn_setValue = "The value of the word ID column has been set to \"{}\"."


DEFAULTCOLUMNS_setColumns = "setColumns"
DEFAULTCOLUMNS_setColumns_warningsOccurred = "setColumns"
DEFAULTCOLUMNS_setColumns_errorsOccurred = "setColumns"



PROCESSFILE = "ProcessFile"



PROCESSFILE_setInputFile = "setInputFile"
PROCESSFILE_setInputFile_parameterIsNotAllowed = "The given input file has zero length."
PROCESSFILE_setInputFile_replacedValue = "The input file has been changed from \"{}\" to \"{}\"."
PROCESSFILE_setInputFile_setValue = "The value of the input file has been set to \"{}\"."

PROCESSFILE_setOutputFile = "setOutputFile"
PROCESSFILE_setOutputFile_parameterIsNotAllowed = "The given output file has zero length."
PROCESSFILE_setOutputFile_replacedValue = "The output file has been changed from \"{}\" to \"{}\"."
PROCESSFILE_setOutputFile_setValue = "The value of the output file has been set to \"{}\"."

PROCESSFILE_copyInputFile = "copyInputFile"
PROCESSFILE_copyInputFile_overwriteWarning = "The destination file \"{}\" has been overwritten with \"{}\"."
PROCESSFILE_copyInputFile_noOverwrite = "Could not copy input file \"{}\" to \"{}\" because the file is already existing in the destination."
PROCESSFILE_copyInputFile_filecopied = "The input file \"{}\" has been copied to \"{}\"."
PROCESSFILE_copyInputFile_inputFileNotExisting = "The input file \"{}\" is not existing."
PROCESSFILE_copyInputFile_parameterIsNotAllowed = "The directory has zero length."
PROCESSFILE_copyInputFile_noInputFileAvailable = "No input file given to copy."

PROCESSFILE_copyOutputFile = "copyOutputFile"
PROCESSFILE_copyOutputFile_overwriteWarning = "The destination file \"{}\" has been overwritten with \"{}\"."
PROCESSFILE_copyOutputFile_noOverwrite = "Could not copy output file \"{}\" to \"{}\" because the file is already existing in the destination."
PROCESSFILE_copyOutputFile_filecopied = "The output file \"{}\" has been copied to \"{}\"."
PROCESSFILE_copyOutputFile_inputFileNotExisting = "The output file \"{}\" is not existing."
PROCESSFILE_copyOutputFile_parameterIsNotAllowed = "The directory has zero length."
PROCESSFILE_copyOutputFile_noInputFileAvailable = "No output file given to copy."

PROCESSFILE_splitInputFile = "splitInputFile"
PROCESSFILE_splitInputFile_parameterIsNone = "The given directory is None."
PROCESSFILE_splitInputFile_amountOfSplitsInvalid = "The amount of splits ({}) is invalid."
PROCESSFILE_splitInputFile_inputFileDoesNotExist = "The input file \"{}\" does not exist."
PROCESSFILE_splitInputFile_inputFileNotLoaded = "The input file data from \"{}\" could not be loaded."
PROCESSFILE_splitInputFile_inputFileSplitted = "The input file has been splittet into {} files in \"{}\"."
PROCESSFILE_splitInputFile_inputFileNotAvailable = "There is no input file to split up."
PROCESSFILE_splitInputFile_parameterIsNotAllowed = "The directory has zero length."

PROCESSFILE_mergeOutputFile = "mergeOutputFile"
PROCESSFILE_mergeOutputFile_errorWhileWritingData = "An error occurred while writing data to \"{}\"."
PROCESSFILE_mergeOutputFile_warningWhileWritingData = "A warning occurred while writing data to \"{}\"."
PROCESSFILE_mergeOutputFile_couldNotLoadData = "Could not load data from file \"{}\"."
PROCESSFILE_mergeOutputFile_noOutputDataGiven = "No target file given."
PROCESSFILE_mergeOutputFile_noInputFilesGiven = "No files given to merge."
PROCESSFILE_mergeOutputFile_overwritingNotAllowed = "Merged file is already existing and can not be overwritten."
PROCESSFILE_mergeOutputFile_noFilesToMerge = "There are no files to merge."

PROCESSFILE_compareInputFile = "compareInputFile"


TASKLIST_startingTask = "Starting Task \"{}\"."
TASKLIST_splittingDataForTask = "Splitting the data."
TASKLIST_overwritingInputData = "The new input data (\"{}\") is replacing another data (\"{}\")."
TASKLIST_noInputDataGiven = "The given input data is None."
TASKLIST_noExperimentNameSet = "There is no experiment name set. Please set one."
TASKLIST_noRunNameSet = "There is no run name set. Please set one."
TASKLIST_noExperimentFolderCreated = "The experiment folder is not created. Is this the right directory?"
TASKLIST_folderCreatedForThisExperiment = "A folder for the experiment \"{}\" and the first run (\"{}\") was created."
TASKLIST_folderCreatedForThisRun = "A folder for the run \"{}\" has been created."
TASKLIST_inputFolderForRunCreated = "The input folder for the run \"{}\" has been created."
TASKLIST_outputFolderForRunCreated = "The output folder for the run \"{}\" has been created."
TASKLIST_noTaskInTaskList = "There are no tasks in the list."
TASKLIST_splitDataFailed = "Splitting of the input data (\"{}\") into pieces failed."
TASKLIST_START_createDirsWarning = "Warnings occurred while creating the directories."
TASKLIST_copyDataFailed = "Copying the data for the task \"{}\" in the input folder failed."
TASKLIST_taskFailed = "The task \"{}\" failed."
TASKLIST_failedToLoadData = "The data int \"{}\" could not be loaded."
TASKLIST_failedToSplitData = "The data \"{}\" could not be splitted."
TASKLIST_sourceAndTargetNotTheSameLength = "There amount of source files ({}) does not match the amount of target files ({})."
TASKLIST_createNewTaskNoFunction = "The given Function is not valid."
TASKLIST_createNewTaskNoArguments = "The given arguments are not valid."
TASKLIST_createNewTaskNoTaskName = "The task name \"{}\" is not a valid task name."
TASKLIST_SETRUNNAME_replaceRunName = "The run name \"{}\" will be repaced by \"{}\""
TASKLIST_SETRUNNAME_invalidRunName = "The given run name is not valid."
TASKLIST_SETCOLUMNS_noWordColumn = "The word column is mandatory."
TASKLIST_SETCOLUMNS_noLabelColumn = "The label column is mandatory."
TASKLIST_SETCOLUMNS_noWordIDColumn = "No word ID column set."
TASKLIST_SETCOLUMNS_noSentenceIDColumn = "No sentence ID column set."
TASKLIST_SETCOLUMNS_noDocumentIDColumn = "No document ID column set."
TASKLIST_START_couldNotCreateTasklistFolder = "Could not create the folder structure for the task list."
TASKLIST_START_couldNotCreateTaskFolder = "Could not create the folder structure for the task."
TASKLIST_START_errorWhileMergingOutput = "An error occurred while merging data int file \"{}\"."
TASKLIST_START_warningWhileMergingOutput = "A warning occurred while merging data into file \"{}\"."
TASKLIST_START_startingMerging = "Merging {} output files into \"{}\"."
TASKLIST_SETOUTPUTDATA_noOutputDataGiven = "The given output data is None."
TASKLIST_SETOUTPUTDATA_overwritingOutputData = "The new output data (\"{}\") is replacing another data (\"{}\")."


TASK_SETSTANDARDFILES_invalidFileCount = "The file count for task \"{}\" need to be set and be greater than zero."
TASK_SETSTANDARDFILES_couldNotAddFile = "The standard files could not be added to the task \"{}\"."
TASK_SETTASKNAME_taskNameNotValid = "The given task name is not valid."
TASK_SETTASKNAME_taskNameReplaced = "The task name \"{}\" will be replaced by \"{}\"."
TASK_SETFUNCTION_functionNotValid = "The given function for task \"{}\" is not valid."
TASK_SETFUNCTION_functionReplaced = "The function \"{}\" will be replaced by \"{}\"."
TASK_SETFUNCTION_functionNotCallable = "The given function for task \"{}\" is not callable."
TASK_SETARGUMENTS_argumentsReplaced = "The arguments will be replaced in task \"{}\"."
TASK_SETARGUMENTS_argumentsNotValid = "The arguments are not valid for task \"{}\"."
TASK_CREATEFOLDERS_experimentNameNotValid = "The experiment name is not valid."
TASK_CREATEFOLDERS_runNameNotValid = "The run name is not valid."
TASK_CREATEFOLDERS_foldersNotExisting = "The folder for the run \"{}\" could not be found."
TASK_CREATEFOLDERS_taskNameNotValid = "The task name is not valid."
TASK_CREATEFOLDERS_taskNameFolderCreated = "The folder for the task \"{}\" has been created."
TASK_CREATEFOLDERS_inputFolderCreated = "The input folder for the task \"{}\" has been created."
TASK_CREATEFOLDERS_outputFolderCreated = "The output folder for the task \"{}\" has been created."
TASK_CREATEFOLDERS_outputAndInputFolderCreated = "The input and output folder for the task \"{}\" has been created."
TASK_CHECKDIRSANDFILES_experimentNameNotValid = "The experiment name is not valid."
TASK_CHECKDIRSANDFILES_runNameNotValid = "The run name is not valid."
TASK_CHECKDIRSANDFILES_taskNameNotValid = "The task name is not valid."
TASK_CHECKDIRSANDFILES_inputFileNotExists = "Some input files for task \"{}\" are missing."
TASK_CHECKDIRSANDFILES_outputDirNotExists = "The output directory for task \"{}\" is not existing."
TASK_CHECKDIRSANDFILES_outputFileExists = "Some output files for task \"{}\" are existing."
TASK_ADDFILE_parametersNotValid = "Input or output file is not valid."
TASK_ADDFILE_experimentNameNotValid = "The experiment name is not valid."
TASK_ADDFILE_runNameNotValid = "The run name is not valid."
TASK_ADDFILE_taskNameNotValid = "The task name is not valid."
TASK_START_nothingToDo = "There are no input files to process for task \"{}\"."
TASK_START_columnWordNotSet ="The column <word> is not set for task \"{}\"."
TASK_START_columnLabelNotSet ="The column <label> is not set for task \"{}\"."
TASK_START_directoryAndFileCheckFailed = "Error while checking files and directories for task \"{}\"."
TASK_START_skippingTask = "Task \"{}\" was skipped."
TASK_START_overwritingOutput = "Task \"{}\" has overwritten a stored output."
TASK_START_unknownWarning = "An unknown warning occured while starting task \"{}\"."

SINGLEPROCESSINGFUNCTION_returnValueNotZero = "Processing row {} in task \"{}\" returned {}. Message: \"\""



DATA = "Data"


DATA_addColumn = "addColumn"
DATA_addColumn_columnAddedSuccessfully = "The column \"{}\" has been added to the data."
DATA_addColumn_warningsWhileAddingColumn = "Warnings occurred while adding the column \"{}\"."
DATA_addColumn_errorsWhileAddingColumn = "Errors occurred while adding the column \"{}\"."
DATA_addColumn_lengthsDoNotMatch = "Could not add column \"{}\" to data since the dimensions do not match ({} (data) vs. {} (new column))."
DATA_addColumn_replacingColumn = "Column \"{}\" has been replaced in data."
DATA_addColumn_noColumnGiven = "No column data given for column \"{}\"."

DATA_setData = "setData"
DATA_setData_overwritingData = "The stored data is overwritten."
DATA_setData_setDataCompleted = "The data (cols: {}, rows: {}) has been set successfully."

DATA_loadCSVData = "loadCSVData"
DATA_loadCSVData_invalidDirectory = "The given file directory is not valid."
DATA_loadCSVData_fileNotFound = "The given file \"{}\" could not be found."
DATA_loadCSVData_loadedSuccessfully = "The data in \"{}\" could be loaded successfully (cols: {}, rows: {})."

DATA_writeCSVData = "writeCSVData"
DATA_writeCSVData_invalidDirectory = "The given file directory is not valid."
DATA_writeCSVData_fileFound = "The given file \"{}\" has been overwritten."
DATA_writeCSVData_noDataToWrite = "There is no data which could be written to \"{}\"."
DATA_writeCSVData_dataSaved = "The data has been written to file \"{}\"."


DATA_setRow = "setRow"
DATA_setRow_invalidIndex = "The given index {} is out of range."
DATA_setRow_successfullySet = "The row at index {} has been set."







fileNotFoundError = "The file \"{}\" could not be found. Check for any errors and start again."
loadingDataInfo = "Loading data from \"{}\"."
loadedDataInfo = "Data loaded: {} rows in {} columns."
noFilePathWarning = "No file path given (\"{}\")."

documentIDColumnWarning = "No document ID column set (\"{}\"). Proceeding without."
sentenceIDColumnWarning = "No sentence ID column set (\"{}\"). Proceeding without."
wordIDColumnWarning = "No word ID column set (\"{}\"). Proceeding without. Consider adding a column manually."

setWordColumnError = "Error setting the word column: {}."

setLabelColumnError = "Error settting the word column: {}."

processStarted = "Process \"{}\" started with PID {} using data from \"{}\" and storing the result in \"{}\"."
functionNoSuccess = "Function \"{}\" returned value {}."
writeResultToFile = "Writing result to file {}."
processEnded = "Process \"{}\" ended, results have been stored in \"{}\""
copyDataForNextTask = "Copy data for next task."


checkDirectoriesAndFiles = "Check directories and files for task \"{}\"."
errorCheckDirectoriesAndFiles = "Error ({}) while checking directories and files for process \"{}\"."
overwriteOutputFiles = "Overwriting output files for task \"{}.\""
skippingTask = "Skipping task \"{}\"."
splittingDataForTask = "Splitting the data."
int
#calcSplitDataAmountInfo = "Amount of splits at column \"{}\" with string \"{}\" are being calculated."
#splitDataAmountInfo = "Amount of splits at column \"{}\" with string \"{}\" are {}."
#removeRows = "Amount of removed rows: {}."
#correctedTags = "Amount of tags which have been corrected {}."

deletingDocuments = "Deleting {} documents."
deletingDocumentsNotPossible = "Could not delete the documents because the parameters are not correct."
deletedAmountDocuments = "Deleted {} words."

deletingSentences = "Deleting {} sentences."
deletingSentencesNotPossible = "Could not delete the sentences because the parameters are not correct."
deletedAmountSentences = "Deleted {} words."

deletingNaNWords = "Deleting {} NaN words."
deletingNaNWordsNotPossible = "Could not delete the NaN words because the parameters are not correct."
deletedAmountNaN = "Deleted {} words with NaN."

deletingWords = "Deleting {} words matching \"{}\"."
deletingWordsNotPossible = "Could not delete the words matching \"{}\" because the parameters are not correct."
deletedAmountWords = "Deleted {} words matching \"{}\"."

deletingConnectedDocuments = "Deleting all documents which are containing deleted elements."
deletingConnectedSentences = "Deleting all sentences which are containing deleted elements."

deletingConnectedDocumentsNotPossible = "Could not delete the connected documents because the parameters are not correct."
deletingConnectedSentencesNotPossible = "Could not delete the connected sentences because the parameters are not correct."

splittingAt = "Splitting input words at \"{}\"."
splittingAtNotPossible = "Splitting input words at \"{}\" not possible because the parameters are not correct."
splittedAtAmount = "{} new words added."

adjustingBIOFormat = "Adjusting BIO-format."
adjustedBIOFormat = "Adjusted {} BIO elements."
adjustingBIOFormatNotPossible = "Could not adjust BIO format because the parameters are not correct."

replacingBIOFormat = "Replacing BIO format (\"{}\" -> \"{}\", \"{}\" -> \"{}\", \"{}\" -> \"{}\")"
replacingBIOFormatNotPossible = "Could not replace BIO format because the parameters are not correct."
replacedBIOFormat = "BIO format has been replaced."

diff = "\"{}\" ?= \"{}\""
diffWordEqual = "\"{}\" == \"{}\""
diffWordNotEqual = "\"{}\" != \"{}\""
diffWordsNotPossible = "Checking differences not possible because the parameters are not correct."

