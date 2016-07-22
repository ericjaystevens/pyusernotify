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
testToAddress = "ericjaystevens@gmail.com"

class TestpyUserNotifynewmessage(unittest.TestCase):


    def setUp(self):
        file = open('.\messages.csv', 'w')
        file.close()
        #file.write("Name,fromAddress,templatePath")

    def test_pyUserNotify_newMessage(self):
        nm.pyusernotify_newMessage("test1", "me@you.com", '.\templateExample.md')
        msgs = pums.pyUserMessages()
        msgs.remove("test1")


    def test_newMessageObject(self):
        message = pum.pyUserMessage("test1", "me@you.com", '.\templateExample.md')
        msgs = pums.pyUserMessages()
        msgs.remove("test1")

    def test_pyUserMessages(self):
        messages = pums.pyUserMessages()
        
    def test_pyusernotifyGetMessage(self):
        self.message = pum.pyUserMessage("test1", "me@you.com", '.\templateExample.md')
        nm.pyusernotify_newMessage("test1", "me@you.com", '.\templateExample.md')
        msgs = pums.pyUserMessages()
        msgs.remove("test1")
        

    def test_removeMessageFromMessages(self):
        messages = pums.pyUserMessages()
        message = pum.pyUserMessage(testName,testEmail,testTemplate)
        messages.remove(message.name)
    
    def test_addToMessages(self):
        message = pum.pyUserMessage("test1", "me@you.com", '.\templateExample.md')
        msgs = pums.pyUserMessages()
        msgs.add(message)
        msgs.remove("test1")

    def test_pyUserMessagesAdd(self):
        messages = pums.pyUserMessages()
        message = pum.pyUserMessage("testaccountNotify",testEmail,testTemplate)
        messages.add(message)
        messages.remove(message.name)

    def test_pyUserNotify_newMessageFull(self):
        os.system("pyusernotify_newMessage.py --name accountNotify --fromAddress admin@acme.com --template .\mark.down")
        msgs = pums.pyUserMessages()
        msg = msgs.get("accountNotify")
        self.assertEqual(msg.name,"accountNotify")
        msgs.remove(msg.name)
    
    def test_pyUerMessage_send(self):
        msg = pum.pyUserMessage(testName,testEmail,testTemplate)
        msgs = pums.pyUserMessages()
        msgs.add(pum)
        msg.send(testToAddress)
        
    


if __name__ == '__main__':
    unittest.main()