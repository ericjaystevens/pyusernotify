#!/usr/bin/env python
import unittest
import pyusernotify_newMessage as nm
import pyusernotify as pun
import pyUserMessage as pum
import pyUserMessages as pums
import os

testName = "test1"
testEmail = "me@you.com"
testTemplate = "templateExample.md"
testToAddress = "ejsteven@oakland.edu"

class TestpyUserNotifynewmessage(unittest.TestCase):


    def test_getFromEmail(self):
        message = pum.pyUserMessage("example")
        self.assertEqual(message.fromEmail,"admin@example.com") 

    def test_getSubject(self):
        message = pum.pyUserMessage("example")
        self.assertEqual(message.getSubject(),'Password Will Expire soon!')

    def test_getMessage(self):
        message = pum.pyUserMessage("example")
        message.getMessage()

    def test_sendMessage(self):
        message = pum.pyUserMessage("sendableExample")
        toAddress = testToAddress
        message.send(toAddress)

    


if __name__ == '__main__':
    unittest.main()