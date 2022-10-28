#!/usr/bin/python3
#author: TWolfis
#file: ReplaceDirective.py
#function: replaces directives in /etc/nagios/generic/contacts.cfg

import sys 
import re 
import argparse 

def GetMatching(configFile,directive):
    print(f"Looking for {directive}")
    try:
        with open(configFile,"r") as file:
            for line in file:
                if re.search(directive,line):
                    print(line)
    except PermissionError:
        print("Not allows to open ",configFile)
        sys.exit()

def ReplaceConfig(configFile,directive,replacementDirective,equals=None):
    """Replace specified directive values file with replacement directive value"""
    replacementConfig = ""

    try:
        with open(configFile,"r") as file:
            for line in file:
                #look for lines that contain the given directive, trim lines to find comments that are not comments
                if re.search(directive,line) and line.strip()[0] != "#":

                    #if equals is set to a value and value is found in line
                    if equals and re.search(equals,line):
                        line = line.replace(line,replacementDirective)
                        replacementConfig = replacementConfig + line + "\n"
                    
                    #if equals is not set but directive is found in line
                    elif not equals :
                        line = line.replace(line,replacementDirective)
                        replacementConfig = replacementConfig + line + "\n" 
                    
                    #if equals is set but not found in line just add line to replacementConfig
                    else:
                        replacementConfig = replacementConfig + line
     
                #Also add any line that do not match the specified directive to the list since those do not have to be replaced
                else:
                    replacementConfig = replacementConfig + line
        return replacementConfig

    except PermissionError:
        print("Not allows to open ",configFile)
        sys.exit()

def WriteNewConfig(configFile,replacementConfig):
    try:
        with open(configFile, "w") as file:
            file.write(replacementConfig)
    except PermissionError:
        print("Not allowed to open ",configFile)
        sys.exit()    

if __name__ == "__main__":

    #default configuration file to search for directives    
    configFile= "/etc/nagios/generic/contacts.cfg"

    parser = argparse.ArgumentParser(description=f"Find and/or Replace directives in {configFile} by default print values for found directives for possible directives take a look at https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/objectdefinitions.html")
    parser.add_argument("directive",help=f"Print out found matches of directive",type=str)
    parser.add_argument("-r,","--replacement",help="Overwrites directive values with specified replacement", type=str)
    parser.add_argument("-e,","--equals",help="Overwrites directive that equals to given value with specified replacement", type=str)
    parser.add_argument("-f,","--file",help=f"Look for directive in file, default file is {configFile}", type=str)
    parser.add_argument("-w","--write",help= f"Overwrite directive with replacement directive replacement",action="store_true")

    #set variables used in program
    args = parser.parse_args()
    directive = args.directive 

    if args.file:
        configFile = args.file 

    if args.replacement:
        #format replacement directive so that output matches the indentation of the nagios configuration
        #example of format:
        #   host_name       example.com

        replaceDirective = "\t"+args.directive+"\t\t\t"+args.replacement

        #if equals is set call replacementConfig with equals
        if args.equals:
            print(ReplaceConfig(configFile,directive, replaceDirective, args.equals))
            print("done")
            sys.exit()
        else:
            replacementConfig = ReplaceConfig(configFile,directive, replaceDirective,None)

        #only write when explicitly specified to prevent unwanted overwrites of configuration files 
        if args.write:
            print(f"Overwritting {configFile}")
            WriteNewConfig(configFile,replacementConfig)
        else:
            #replacementConfig could also be redirected to an alternative config file 
            print(replacementConfig)
        sys.exit()
        
    #print(ReplaceConfig(configFile,replaceDirective))
    print(GetMatching(configFile,directive))
