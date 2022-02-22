import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

testNumbersWord = open('testNumbersWord.txt', 'r')
test_Number_sWord = testNumbersWord.read().lower()

class WordCounterTestSuite(unittest.TestCase):

    #Abertura del navegador y la página 
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(5)

        driver.get('https://wordcounter.net/')
        driver.maximize_window()


    def testNumbersOneFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Number_sWord)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 3, 'The frequency expected does not match the word.')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'word-counter-report'))
