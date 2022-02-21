import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver 
from time import sleep 

class TestStringMethods(unittest.TestCase):
    
	def test_positive(self):
		testValue = False 

		if 4 == 4:
			testValue = True

		message = "Test value is not true."
        
		self.assertTrue( testValue, message)
 
if __name__ == '__main__':
    unittest.main()