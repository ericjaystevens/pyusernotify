import pyUserMessage
csvPath =".\messages.csv"
import csv
import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class pyUserMessages:
    def __init__(self):
        self.messages = []
        #for each message in csv append to messages
        with open(csvPath) as csvfile:
            csvfileReader = csv.reader(open(csvPath))
            for line in csvfileReader:
                if line and (len(line) == 3) :
                    name = line[0]
                    email = line[1]
                    templatePath = line[2]
                    message = pyUserMessage.pyUserMessage(name, email, templatePath)
                    self.messages.append(message)
            

    def remove(self,name):
        f = open(csvPath,"r")
        lines = f.readlines()
        f.close()

        f = open(csvPath,"w")
        for line in lines:
            nameFromLine = line.split(",")[0]
            if name != nameFromLine:
                f.write(line)
        f.close()

    def get(self,name):
        for message in self.messages:
            if name == message.name:
                return message

    def add(self,message):
        nameInUse = False
        for existingMessage in self.messages:
            if existingMessage.name == message.name:
                nameInUse = True
        if (nameInUse):
            raise ValueError("message.name is already in use")
        else:
            entry = message.name + "," + message.email + "," + message.templatePath + "\n"
            logging.debug("writing to " + csvPath + " " + entry)
            f = open(csvPath,"a")
            f.write(entry)
            f.close()
            
            
          	
