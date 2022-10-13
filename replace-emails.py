#!/usr/bin/python3
#author: TWolfis
#file: replace-emails.py
#function: replaces emails in /etc/nagios/generic/contacts.cfg

import sys 
import re 
import argparse 

def GetEmails(filename):
    try:
        with open(filename,"r") as file:
            for line in file:
                if re.search("email",line):
                    print(line)
    except PermissionError:
        print("Not allows to open ",filename)
        sys.exit()

def ReplaceEmails(filename,replacementEmail):
    """Replace all emails in file with replacement Email"""
    replacementConfig = ""

    try:
        with open(filename,"r") as file:
            for line in file:
                #look for lines that contain an email address that are not comments
                if re.search("email",line) and line[0] != "#":
                    line = line.replace(line,replacementEmail)
                    replacementConfig = replacementConfig + line + "\n"

                #Also add any line that has no email defined to the list since those do not have to be replaced
                else:
                    replacementConfig = replacementConfig + line
        return replacementConfig

    except PermissionError:
        print("Not allows to open ",filename)
        sys.exit()

def WriteNewConfig(replacementConfig, filename):
    try:
        with open(filename, "w") as file:
            file.write(replacementConfig)
    except PermissionError:
        print("Not allowed to open ",filename)
        sys.exit()    

if __name__ == "__main__":
    
    contactsFile= "/etc/nagios/generic/contacts.cfg"

    #the spaces are needed to please my autism 
    replaceEmail = 8*" "+"email"+27*" "

    parser = argparse.ArgumentParser(description=f"Replace emails in {contactsFile} prints out new configuration to terminal")
    parser.add_argument("-r","--replace",help= f"Force replacement of emails in {contactsFile} with the replacement email",action="store_true")
    parser.add_argument("-c","--current",help=f"Print out email addresses in {contactsFile}",action="store_true")
    parser.add_argument("-e,","--email",help="Overwrite default replacement email with specified email", type=str)

    args = parser.parse_args()

    if args.email:
        replaceEmail += args.email
    else:
        replaceEmail += "twolfis@mcx.nl"

   
    if args.current:
        GetEmails(contactsFile)
        sys.exit()
    
    if args.replace:
        WriteNewConfig(ReplaceEmails(contactsFile,replaceEmail),contactsFile)
        sys.exit()
       
    print(ReplaceEmails(contactsFile,replaceEmail))