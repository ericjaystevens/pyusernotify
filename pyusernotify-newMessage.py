import argparse
import re
import os.path

### Handle Arguments

parser = argparse.ArgumentParser(description="Create a new message type")
parser.add_argument("-n","--name", required=True, help="Desired name of new message")
parser.add_argument("-f","--from", required=True, help="From address")
parser.add_argument("-t","--template", required=True, help="Path to template markdown file")
parser.add_argument("-v","--verbose", help="Increaser verbosity")
args = parser.parse_args()

def main():
    if (not validateArgs(args)):
        return False
    
def validateArgs(args):
    FROM = args
    if (not args.name.isalnum()):
        print("Name paramater must be alpha numberic only!")
        return False

    print(args)    
    #FROM = args.from
    #if not re.match(r"[^@]+@[^@]+\.[^@]+",FROM):
        #print("Use a valid email address!")
        #return False

    if (os.path.isfile(args.template)):
        Print("No file found at template path")
        return False

main()