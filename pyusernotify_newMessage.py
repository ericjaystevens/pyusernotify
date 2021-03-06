#!/usr/bin/env python
import argparse
import re
import pyUserMessage as msg
import pyUserMessages as msgs
import textwrap
import os

ds =".\messages.csv"

### Handle Arguments
def get_args():
    parser = argparse.ArgumentParser(
        description="Create a new message type", 
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
        Examples
        --------
        pyusernotify_newMessage.py --name accountNotify --fromAddress admin@acme.com --tempalte .\message.mkd
      
    ''')
    )
    parser.add_argument("-n","--name", required=True, help="Desired name of new message")
    parser.add_argument("-f","--fromAddress", required=True, help="From address")
    parser.add_argument("-t","--template", required=True, help="Path to template markdown file")
    parser.add_argument("-v","--verbose", help="Increase verbosity")
    return parser.parse_args()

### Main Function ###
def pyusernotify_newMessage(name, fromAddress, template):
    print("entered new message named" + name)
    message = msg.pyUserMessage(name,fromAddress,template)
    messages = msgs.pyUserMessages()
    messages.add(message)    
    
def validateArgs(args):
    if (not args.name.isalnum()):
        raise ValueError("Name paramater must be alpha numberic only!")
   
    if not re.match(r"[^@]+@[^@]+\.[^@]+",args.fromAddress):
        raise ValueError("Use a valid email address!")

    if (not os.path.isfile(args.template)):
        raise ValueError("No file found at template path")

if __name__ == '__main__':
    args = get_args()
    validateArgs(args)
    pyusernotify_newMessage(args.name,args.fromAddress,args.template)