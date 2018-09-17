from actionBlock import performRamsLogin
import unittest


class runLogin(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
    
    def testDoLogin(self):
        run = performRamsLogin.performRamsLogin(self)
        run.login()
        run.curl()
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)