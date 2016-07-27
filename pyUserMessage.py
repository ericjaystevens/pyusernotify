import smtplib
import configparser
import pyUserMessages as pums
from markdown2 import Markdown
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        msg = MIMEMultipart('alternative')
        msg['From'] = self.email
        sender = self.email
        msg['Subject'] = self.getSubject()
        html = self.getMessage
        part1 = MIMEText(html, 'html')
        msg.attach(part1)

        try:
            smtpObj = smtplib.SMTP(smtpServer)
            smtpObj.sendmail(sender, receivers, msg.as_string())         
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
        f.close()
        return message

    def getSubject(self):
        f = open(self.templatePath,"r")
        lines = f.readlines()
        subject = lines[0]
        f.close()

        return subject
