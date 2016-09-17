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
    def __init__(self, name):
        self.name = name
        config = configparser.ConfigParser()
        config.read(configFile)
        self.templatePath = config['Default']['templateDir'] + name + '.pun'
        self.fromEmail = self.getFromEmail()

    def send(self,toAddress):
        config = configparser.ConfigParser()
        config.read(configFile)
        smtpServer = config['Default']['SmtpServer']

        receivers = toAddress
        msg = Message(From=self.fromEmail,To=toAddress)
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

        firstLineOfMessage = 0
        

        for line in lines:
            firstLineOfMessage = firstLineOfMessage + 1
            if line == '\n':
                break
   
        for i in range(firstLineOfMessage,len(lines)):
            msgAsMarkdown = msgAsMarkdown + lines[i]
        
        markdowner = Markdown()
        message = markdowner.convert(msgAsMarkdown)
        f.close()
        return message

    def getSubject(self):
        f = open(self.templatePath,"r")
        lines = f.readlines()
        subjectLine = lines[1]
        subject = subjectLine.split(":")[1].strip()
        f.close()
        return subject

    def getFromEmail(self):
        f = open(self.templatePath,"r")
        lines = f.readlines()
        emailLine = lines[0]
        email = emailLine.split(":")[1].strip()
        f.close()
        return email

