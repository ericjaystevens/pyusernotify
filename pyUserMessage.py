import smtplib
import configparser
import pyUserMessages as pums
from markdown2 import Markdown

configFile = "setup.ini"

class pyUserMessage:
    def __init__(self, name, email, templatePath):
        self.name = name
        self.email = email
        self.templatePath = templatePath

    def send(self,toAddress):
        config = configparser.ConfigParser()
        config.read(configFile)
        smtpServer = config['Default']['SmtpServer']

        sender = self.email

        receivers = toAddress
        message = self.getMessage()

        try:
            smtpObj = smtplib.SMTP(smtpServer)
            smtpObj.sendmail(sender, receivers, message)         
        except SMTPException:
            print("Error: unable to send email")

    def getMessage(self):
        msgAsMarkdown = ""
        subject = ""
        # for each line in file
        # set the first line to message 
        # put the rest into a long string
        f = open(self.templatePath,"r")
        lines = f.readlines()
        subject = lines[0]

        for line in lines:
            msgAsMarkdown = msgAsMarkdown + line
        
        markdowner = Markdown()
        message = markdowner.convert(msgAsMarkdown)
        return message

    def getSubject(self):
        msgAsMarkdown = ""
        subject = ""
        # for each line in file
        # set the first line to message 
        # put the rest into a long string
        with open(self.templatePath) as f:
            for i, l in enumerate(f):
                if(i==1):
                    subject = f[i]

        return subject
