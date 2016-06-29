#!/usr/bin/env python
import unittest
import pyusernotify_newMessage as nm
import pyusernotify as pun
import pyUserMessage as pum

class TestpyUserNotifynewmessage(unittest.TestCase):

    def setup(self):
        self.templateFile = file = open('.\templateExample.md', 'w+')
        self.templateFile.write("Name,fromAddress,templatePath")

    def test_pyUserNotify_newMessage(self):
        nm.pyusernotify_newMessage("test1", "me@you.com", '.\templateExample.md')

    def test_newMessageObject(self):
        self.message = pum.pyUserMessage("test1", "me@you.com", '.\templateExample.md')

    def test_pyusernotifyGetMessage(self):
        self.message = pum.pyUserMessage("test1", "me@you.com", '.\templateExample.md')
        nm.pyusernotify_newMessage("test1", "me@you.com", '.\templateExample.md')
        self.assertEqual(pun.getMessage("test1"),self.message)

if __name__ == '__main__':
    unittest.main()