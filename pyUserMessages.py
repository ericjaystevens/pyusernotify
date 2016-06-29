import pyUserMessage
csvPath =".\messages.csv"
import csv

class pyUserMessages:
    def __init__(self):
        self.messages = []
        #for each message in csv append to messages
        with open(csvPath,'rt', encoding="ascii") as csvfile:
            messages = csv.reader(csvfile,delimiter=',',quotechar='|')
            for line in messages:
                name = line[0]
                email = line[1]
                templatePath = line[2]
                message = pyUserMessage.pyUserMessage(name, email, templatePath)
