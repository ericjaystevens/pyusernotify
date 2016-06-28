#!/usr/bin/env python
import argparse
import re
import os.path
import csv

### Handle Arguments
def get_args():
    parser = argparse.ArgumentParser(description="Create a new message type")
    parser.add_argument("-m","--message", required=True, help="name of predefined message to send")
    parser.add_argument("-t","--toAddress", required=True, help="To address")
    parser.add_argument("-r","--replace", help="Dictionary of variables to replace in template")
    parser.add_argument("-v","--verbose", help="Increase verbosity")
    return parser.parse_args()

### Main ###
def pyusernotify(message,toAddress):

if __name__ == '__main__':
    args = get_args()
    pyusernotify_newMessage(args.message,args.toAddress)