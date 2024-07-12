#!/usr/bin/env python
# coding: utf-8

import os.path
import yaml

from Values import *

"""
This class is used to load the configuration of a process. It provides
a method to set a standard configuration which is an object. 
Methods to load a defined configuration from a file and to enrich the 
loaded configuration with values from the standard configuration if
they are not defined.

Since every configuration should be set in one config file, this class
is a so called singleton.

Example for the content of the config file:

logger:
  format: "[%(levelname)-8s] %(asctime)s: %(message)s"
  date_format: "%Y/%m/%d %H:%M:%S"
  level: "INFO"
  
How to use:

->  First: execute setStandardConfiguration(...) to provide the standard 
    configuration.
->  Second: execute loadConfiguration(...) to load and apply the
    configuration.
->  Last: execute getConfiguration(...) to get the configuration.
"""
class Configuration:
    
    # This is the standard configuration which contains all standard
    # values in case they are not provided by the configuration file.
    standardConfiguration = {}
    
    # The standard directory for configuration files.
    standardDirectory     = "./config/config.yaml"
    
    # This is the configuration which is already enriched with the
    # standard configuration.
    configuration         = None
    
    """
    This method returns the with standard value enriched configuration
    which has been loaded from the configuration file.
    
    return: the configuration in form of an object with key-value pairs.
    """
    @staticmethod
    def getConfiguration():
        return Configuration.configuration
    
    """
    Looking up the configuration and returning the settings.
    Usually this is done as the first step in any script.
    Prints are only being used in case of an error/warning
    since no logging has been configured.

    To create your file please use a similar fomat to:
    <paramname1>:
    <space><space><paramname2>: "This is a string"
    <space><space><paramname3>: 42
    <paramname4>:
    <space><space><paramname5>: ["A list", "of strings"]

    configfiledir: the path to the configuration file as string.
        (default: standard directory).
    openFor: open the configuration file with read or
        write options. (default: read only option)
    return: 0 if the configuration could be loaded, >0 for 
        warnings, <0 for errors:
         0: everything went well
        -1: directory is not a string
        -2: configuration file is not existing
        -3: no configuration could be loaded
         1: the standard directory for the configuration file
             is used.
         2: this warning should only happen if you execute 
             __applyConfiguration(...) by your own which
             you should not do.
    """
    @staticmethod
    def loadConfiguration(directory = None, openFor = "r"):
        ret = ZERO
        
        # If no directory is given, the standard directory will
        # be used.
        if directory is None:
            directory = Configuration.standardDirectory
            ret = ONE
        
        # Check if the file is existing.
        if os.path.isfile(directory):
            
            # <directory> needs to be a string. 
            if isinstance(directory, str):

                # The configuration file is opened.
                with open(directory, openFor) as configFile:
                    
                    # in this way no code which is contained in the file
                    # will be executed. Since data is a list and only the 
                    # first element is relevant to us, only the first 
                    # element is returned.
                    Configuration.configuration = list(yaml.safe_load_all(configFile))[0]
                    Configuration.__applyConfiguration(
                        Configuration.configuration, 
                        Configuration.standardConfiguration)
            else:
                ret = -ONE
        else:
            ret = -TWO
            
        return ret      
        
    """
    Recursive method which applies a given standard configuration to a
    configuration which has been loaded from a file. Parameters which 
    are loaded will not be replaced with the standard configuration. 
    Parameter sets which are not present in the configuration file will
    be created and all parameters will be copied.
    
    configuration: the configuration on which the standard configuration
        should be applied.
    standardConfiguration: the object where the standard configuration 
        is saved.
    return: 0 if the configuration could be loaded, >0 for warnings, <0
        for errors.
         0: everything went well
        -3: the given configuration is none.
         2: the standard configuration of the Configuration class is used
             because the given one was none.
    """
    @staticmethod
    def __applyConfiguration(configuration, standardConfiguration=None):
        ret = ZERO
        
        if configuration is not None:
            
            if standardConfiguration is None:
                standardConfiguration = Configuration.standardConfiguration
                ret = TWO
            
            # For each parameter in the standard configuration, check if
            # this parameter is also in the configuration, if not copy
            # the content.
            for param in standardConfiguration:
                
                # Is the parameter a set of parameters or a regular
                # parameter?
                if isinstance(standardConfiguration[param], dict):
                    
                    # If the parameter is not set in the configuration
                    # create it.
                    if param not in configuration:
                        configuration[param] = {};
                        
                    # Apply the same procedure to every parameter in the
                    # parameter set.
                    ret = Configuration.__applyConfiguration(
                        configuration[param], 
                        standardConfiguration[param])
                else:
                    # If the parameter is a regular parameter, copy the
                    # content if to the configuration if it is not
                    # existent in there
                    configuration.setdefault(
                        param, 
                        standardConfiguration[param])
            return configuration
        else:
            ret = -THREE
    
    """
    Function to set the standard configuration.
    
    standardConfiguration: an object with key value pairs containing the configuration.
    return: 0 if everything went well, -1 if standardConfiguration was none.
    """
    @staticmethod
    def setStandardConfiguration(standardConfiguration = None):
        ret = ZERO
        if standardConfiguration is not None:
            Configuration.standardConfiguration = standardConfiguration
        else:
            ret = -ONE
        return ret
        


# In[ ]:




