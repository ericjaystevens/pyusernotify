#!/usr/bin/env python
import argparse
import re
import os.path
import csv
ds =".\messages.csv"

### Handle Arguments
def get_args():
    parser = argparse.ArgumentParser(description="Create a new message type")
    parser.add_argument("-n","--name", required=True, help="Desired name of new message")
    parser.add_argument("-f","--fromAddress", required=True, help="From address")
    parser.add_argument("-t","--template", required=True, help="Path to template markdown file")
    parser.add_argument("-v","--verbose", help="Increaser verbosity")
    return parser.parse_args()

### Main Function ###
def pyusernotify_newMessage(name, fromAddress, template):
    print("entered new message named" + name)
    testIfnameExists(name)
    ds = getDataStore()
    ds.write( '\n' + name + "," + fromAddress + "," + template )
    
    
    
def validateArgs(args):
    if (not args.name.isalnum()):
        raise ValueError("Name paramater must be alpha numberic only!")
   
    if not re.match(r"[^@]+@[^@]+\.[^@]+",args.fromAddress):
        raise ValueError("Use a valid email address!")

    if (not os.path.isfile(args.template)):
        raise ValueError("No file found at template path")

def testIfnameExists(name):
    return

def getDataStore():
    ofile = open(ds,"a")
    return ofile

if __name__ == '__main__':
    args = get_args()
    validateArgs(args)
    pyusernotify_newMessage(args.name,args.fromAddress,args.template)