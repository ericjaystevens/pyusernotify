import smtplib
import configparser
import pyUserMessages as pums
from markdown2 import Markdown
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mailer import Mailer
from mailer import Message

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

        receivers = toAddress
        msg = Message(From=self.email,To=toAddress)
        msg.Subject = self.getSubject()
        msg.Html = self.getMessage()
        mailer = Mailer(smtpServer)

        try:
            mailer.send(msg) #.send(msg)
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
            if not (line == lines[0]):
                msgAsMarkdown = msgAsMarkdown + line
        
        markdowner = Markdown()
        message = markdowner.convert(msgAsMarkdown)
        f.close()
        return message

    def getSubject(self):
        f = open(self.templatePath,"r")
        lines = f.readlines()
        subject = lines[0]
        f.close()
        return subject

