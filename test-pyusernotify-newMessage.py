#!/usr/bin/env python
import unittest
import pyusernotify_newMessage as nm

class TestpyUserNotifynewmessage(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(nm.pyusernotify_newmessage() , 'FOO')

if __name__ == '__main__':
    unittest.main()