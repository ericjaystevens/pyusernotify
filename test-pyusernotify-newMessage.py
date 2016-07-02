#!/usr/bin/env python
import unittest
import pyusernotify_newMessage as nm
import pyusernotify as pun
import pyUserMessage as pum
import pyUserMessages as pums
import os

testName = "test1"
testEmail = "me@you.com"
testTemplate = ".\templateExample.md"

class TestpyUserNotifynewmessage(unittest.TestCase):


    def setup(self):
        self.templateFile = file = open('.\templateExample.md', 'w+')
        self.templateFile.write("Name,fromAddress,templatePath")

    def test_pyUserNotify_newMessage(self):
        nm.pyusernotify_newMessage("test1", "me@you.com", '.\templateExample.md')

    def test_newMessageObject(self):
        self.message = pum.pyUserMessage("test1", "me@you.com", '.\templateExample.md')

    def test_pyUserMessages(self):
        messages = pums.pyUserMessages()
        
    def test_pyusernotifyGetMessage(self):
        self.message = pum.pyUserMessage("test1", "me@you.com", '.\templateExample.md')
        nm.pyusernotify_newMessage("test1", "me@you.com", '.\templateExample.md')
        messages = pums.pyUserMessages()

    def test_removeMessageFromMessages(self):
        messages = pums.pyUserMessages()
        message = pum.pyUserMessage(testName,testEmail,testTemplate)
        messages.remove(message.name)
    
    def test_addToMessages(self):
        message = pum.pyUserMessage("test1", "me@you.com", '.\templateExample.md')
        msgs = pums.pyUserMessages()
        msgs.add(message)

    def test_pyUserNotify_newMessageFull(self):
        os.system("pyusernotify_newMessage.py --name accountNotify --fromAddress admin@acme.com --tempalte .\message.mkd")
        msgs = pums.pyUserMessages()
        msg = msgs.get("accountNotify")
        self.assertEqual(msg.name,"accountNotify")

if __name__ == '__main__':
    unittest.main()