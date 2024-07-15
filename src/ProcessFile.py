#!/usr/bin/env python
# coding: utf-8

import os
import filecmp
import shutil

from Values                              import *
from Utils                               import *
from Logger                              import *
from Task                                import *
from ReturnValue                         import *
from Data                                import *

"""

"""
class ProcessFile:

    #
    __inputFile = None

    #
    __outputFile = None

    """
    
    """
    def setInputFile(self, inputFile: str = None) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(PROCESSFILE)
        ret.setMethodName(PROCESSFILE_setInputFile)

        if (inputFile is not None and len(inputFile) > ZERO):
            if (self.getInputFile() is not None and 
                len(self.getInputFile()) > ZERO):
                ret.setValue(ONE)
                ret.setMessage(PROCESSFILE_setInputFile_replacedValue.
                    format(self.getInputFile(), inputFile))
            else:
                ret.setMessage(PROCESSFILE_setInputFile_setValue.
                    format(inputFile))
            self.__inputFile = inputFile
        else:
            ret.setValue(-ONE)
            ret.setMessage(PROCESSFILE_setInputFile_parameterIsNotAllowed)

        return ret

    """
    
    """
    def setOutputFile(self, outputFile: str) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(PROCESSFILE)
        ret.setMethodName(PROCESSFILE_setOutputFile)

        if (outputFile is not None and len(outputFile) > ZERO):
            if (self.getOutputFile() is not None and 
                len(self.getOutputFile()) > ZERO):
                ret.setValue(ONE)
                ret.setMessage(PROCESSFILE_setOutputFile_replacedValue.
                    format(self.getOutputFile(), outputFile))
            else:
                ret.setMessage(PROCESSFILE_setOutputFile_setValue.
                    format(outputFile))
            self.__outputFile = outputFile
        else:
            ret.setValue(-ONE)
            ret.setMessage(PROCESSFILE_setOutputFile_parameterIsNotAllowed)

        return ret

    """
    
    """
    def getInputFile(self) -> str:
        return self.__inputFile
    
    """
    
    """
    def getOutputFile(self) -> str:
        return self.__outputFile
    
    """
    
    """
    def existsInputFile(self) -> bool:
        ret = False

        if (self.getInputFile() is not None):
            ret = os.path.isfile(self.getInputFile())

        return ret

    """
    
    """
    def existsOutputFile(self) -> bool:
        ret = False

        if (self.getOutputFile() is not None):
            ret = os.path.isfile(self.getOutputFile())

        return ret

    """
    Both src and dst need to be the entire filename of the files, including path.
    """
    def copyInputFile(self, directory: str = EMPTYSTRING, 
        overwrite: bool = False) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(PROCESSFILE)
        ret.setMethodName(PROCESSFILE_copyInputFile)

        if (self.getInputFile() is not None): 
            if (self.existsInputFile()):
                if (directory is not None and len(directory) > ZERO):
                    exists = os.path.isfile(directory)
                    if (exists and not overwrite):
                        ret.setValue(-ONE)
                        ret.setMessage(PROCESSFILE_copyInputFile_noOverwrite.
                            format(self.getInputFile(), directory))
                    else:
                        if (exists):
                            ret.setMessage(
                                PROCESSFILE_copyInputFile_overwriteWarning.
                                format(directory, self.getInputFile()))
                        else:
                            ret.setMessage(PROCESSFILE_copyInputFile_filecopied.
                                format(self.getInputFile(), directory))
                        shutil.copyfile(self.getInputFile(), directory)
                else:
                    ret.setValue(THREE)
                    ret.setMessage(
                        PROCESSFILE_copyInputFile_parameterIsNotAllowed)
            else:
                ret.setValue(TWO)
                ret.setMessage(PROCESSFILE_copyInputFile_inputFileNotExisting.
                    format(self.getInputFile()))
        else:
            ret.setValue(ONE)
            ret.setMessage(PROCESSFILE_copyInputFile_noInputFileAvailable)

        return ret
    
    """
    
    """
    def copyOutputFile(self, directory: str = EMPTYSTRING, 
        overwrite: bool = False) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(PROCESSFILE)
        ret.setMethodName(PROCESSFILE_copyOutputFile)

        if (self.getOutputFile() is not None): 
            if (self.existsOutputFile()):
                if (directory is not None and len(directory) > ZERO):
                    exists = os.path.isfile(directory)
                    if (exists and not overwrite):
                        ret.setValue(-ONE)
                        ret.setMessage(PROCESSFILE_copyOutputFile_noOverwrite.
                            format(self.getOutputFile(), directory))
                    else:
                        if (exists):
                            ret.setMessage(
                                PROCESSFILE_copyOutputFile_overwriteWarning.
                                format(directory, self.getOutputFile()))
                        else:
                            ret.setMessage(PROCESSFILE_copyOutputFile_filecopied.
                                format(self.getOutputFile(), directory))
                        shutil.copyfile(self.getOutputFile(), directory)
                else:
                    ret.setValue(THREE)
                    ret.setMessage(
                        PROCESSFILE_copyOutputFile_parameterIsNotAllowed)
            else:
                ret.setValue(TWO)
                ret.setMessage(PROCESSFILE_copyOutputFile_outputFileNotExisting.
                    format(self.getOutputFile()))
        else:
            ret.setValue(ONE)
            ret.setMessage(PROCESSFILE_copyOutputFile_noOutputFileAvailable)

        return ret
    """
    
    """
    def splitInputFile(self, directory: str = None, 
        prefix: str = None, splits: int = ONE) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(PROCESSFILE)
        ret.setMethodName(PROCESSFILE_splitInputFile)

        if (self.getInputFile() is not None):
            if (self.existsInputFile()):
                if (directory is not None and len(directory) > ZERO):
                    if (splits > ZERO):
                        inputData = Data()
                        load = inputData.loadCSVData(self.getInputFile())

                        if (load.getValue() == ZERO):
                            count = inputData.getRowCount() / splits

                            if (prefix is None):
                                prefix = EMPTYSTRING

                            for index in range(ZERO, splits):
                                fromIndex = math.floor(count * index)
                                toIndex = math.floor(count * (index + ONE))
                                
                                if (index == splits - ONE):
                                    toIndex = self.getRowCount()

                                d = inputData.getData().iloc[fromIndex:toIndex]
                                d.to_csv(
                                    os.path.join(
                                        directory, 
                                        prefix + INPUTFILENAME.format(
                                            str(index))
                                    ), 
                                    index = False
                                )

                            ret.setMessage(
                                PROCESSFILE_splitInputFile_inputFileSplitted.
                                format(count, directory))
                        else:
                            ret.setValue(-ONE)
                            ret.setMessage(
                                PROCESSFILE_splitInputFile_inputFileNotLoaded.
                                    format(self.getInputFile()))
                    else:
                        ret.setValue(FOUR)
                        ret.setMessage(
                            PROCESSFILE_splitInputFile_amountOfSplitsInvalid.
                            format(splits))
                else:
                    ret.setValue(THREE)
                    ret.setMessage(
                        PROCESSFILE_splitInputFile_parameterIsNotAllowed)
            else:
                ret.setValue(TWO)
                ret.setMessage(PROCESSFILE_splitInputFile_inputFileDoesNotExist)
        else:
            ret.setValue(ONE)
            ret.setMessage(PROCESSFILE_splitInputFile_inputFileNotAvailable)

        return ret

    """
    
    """
    def mergeOutputFile(self, directory: str = EMPTYSTRING, 
        prefix: str = EMPTYSTRING, overwrite: bool = False) -> ReturnValue:
        ret = ReturnValue(ZERO)

        ret.setClassName(PROCESSFILE)
        ret.setMethodName(PROCESSFILE_mergeOutputFile)

        if (self.getOutputFile() is not None):
            if (directory is not None and len(directory) > ZERO):
                if (overwrite or not self.existsOutputFile()):

                    files = os.listdir(directory)
                    if (len(files) > ZERO):
                        index = ZERO

                        while(index < len(files) and ret.getValue() >= ZERO):
                            file = files[index]
                            if (file.startswith(prefix)):
                                data = Data()
                                load = data.loadCSVData(file)

                                if (load.getValue() == ZERO):
                                    header = False
                                    open = APPENDTOFILE
                                    if (index == ZERO):
                                        open = WRITE
                                        header = True

                                    write = data.writeCSVData(
                                        self.getOutputFile(), open, 
                                        header = header)
                                    
                                    if (write.getValue() < ZERO):
                                        ret.setValue(-TWO)
                                        ret.setRoot(write)
                                        ret.setMessage(
                                            PROCESSFILE_mergeOutputFile_errorWhileWritingData.
                                            format(self.getOutputFile()))
                                        ret.setCritical()
                                    else:
                                        if (write.getValue() > ZERO and ret.getValue() == ZERO):
                                            ret.setValue(FIVE)
                                            ret.setMessage(
                                                PROCESSFILE_mergeOutputFile_warningWhileWritingData.
                                                format(self.getOutputFile()))
                                            ret.addRoot(write)
                                else:
                                    ret.setValue(-ONE)
                                    ret.setMessage(
                                        PROCESSFILE_mergeOutputFile_couldNotLoadData.
                                        format(file))
                                    ret.addRoot(load)
                    else:
                        ret.setValue(FOUR)
                        ret.setMessage(
                            PROCESSFILE_mergeOutputFile_noFilesToMerge)
                else:
                    ret.setValue(THREE)
                    ret.setMessage(
                        PROCESSFILE_mergeOutputFile_overwritingNotAllowed)
            else:
                ret.setValue(TWO)
                ret.setMessage(PROCESSFILE_mergeOutputFile_noOutputDataGiven)
        else:
            ret.setValue(ONE)
            ret.setMessage(PROCESSFILE_mergeOutputFile_noOutputDataGiven)

        return ret
    
    """
    
    """
    def equalInputFile(self, file: str) -> bool:
        ret = False

        if (self.getInputFile() is not None):
            if (self.existsInputFile()):
                if (file is not None and len(file) > ZERO):
                    ret = filecmp.cmp(self.getInputFile(), file)

        return ret