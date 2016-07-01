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
                if line:
                    name = line[0]
                    email = line[1]
                    templatePath = line[2]
                    message = pyUserMessage.pyUserMessage(name, email, templatePath)

    def remove(self,name):
        f = open(csvPath,"r")
        lines = f.readlines()
        f.close

        f = open(csvPath,"w")
        for line in lines:
            nameFromLine = line.split(",")[0]
            if name != nameFromLine:
                f.write(line)
        f.close()

    def get(self,name):
        f = open(csvPath,"r")
        lines = f.readlines()

        for line in lines:
            nameFromLine = line.split(",")[0]
            if name == nameFromLine:
                email = line[1]
                templatePath = line[2]
                message = pyUserMessage.pyUserMessage(name, email, templatePath)
                f.close()
                return message
        
        f.close()
            	
