import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

open_words = open('text_words.txt', 'r')
text_words = open_words.read().lower()

class WordCounterTestSuite(unittest.TestCase):

    #Abertura del navegador y la página 
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(5)

        driver.get('https://wordcounter.net/')
        driver.maximize_window()

#______________________________________________________________________________________________
    def testOneLetterWordCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('a')
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))


        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 1

        self.assertEquals(expected_value_words, result_text_count_words, "The value expected does not match the number of words.")

    def testOneLetterCharacterCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('a')
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 1

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testFirstOneLetterFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('a')

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 1, 'The density frequency expected does not match the word.')

#______________________________________________________________________________________________
    def testOneWordWordCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('hello')
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))


        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 1

        self.assertEquals(expected_value_words, result_text_count_words, "The value expected does not match the number of words.")

    def testOneWordCharacterCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('hello')
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 5

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testFirstOneWordFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('hello')

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 1, 'The density frequency expected does not match the word.')

#______________________________________________________________________________________________
    def testNamesWordWordCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('Daniel Edward Santiago Pedro Edward Daniel Erika Alexander Oscar Daniel Pedro Pedro Pedro Erika')
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))


        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 14

        self.assertEquals(expected_value_words, result_text_count_words, "The value expected does not match the number of words.")

    def testNamesWordCharacterCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('Daniel Edward Santiago Pedro Edward Daniel Erika Alexander Oscar Daniel Pedro Pedro Pedro Erika')
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 95

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testNamesOneWordFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('Daniel Edward Santiago Pedro Edward Daniel Erika Alexander Oscar Daniel Pedro Pedro Pedro Erika')

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 4, 'The density frequency expected does not match the word.')

    def testNamesSecondFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('Daniel Edward Santiago Pedro Edward Daniel Erika Alexander Oscar Daniel Pedro Pedro Pedro Erika')

        second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
        frequency_second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
        print(second_word.text, '; ', frequency_second_word.text[0])

        self.assertEqual(int(frequency_second_word.text[0]), 3, 'The density frequency expected does not match the word.')

    def testNamesThirdFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys('Daniel Edward Santiago Pedro Edward Daniel Erika Alexander Oscar Daniel Pedro Pedro Pedro Erika')

        third_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
        frequency_third_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
        print(third_word.text, '; ', frequency_third_word.text[0])

        self.assertEqual(int(frequency_third_word.text[0]), 2, 'The density frequency expected does not match the word.')

#______________________________________________________________________________________________
    def testTextWordWordCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(text_words)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))


        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 152

        self.assertEquals(expected_value_words, result_text_count_words, "The value expected does not match the number of words.")

    def testTextWordCharacterCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(text_words)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 912

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testTextOneWordFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(text_words)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 6, 'The density frequency expected does not match the word.')

    def testTextSecondFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(text_words)

        second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
        frequency_second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
        print(second_word.text, '; ', frequency_second_word.text[0])

        self.assertEqual(int(frequency_second_word.text[0]), 3, 'The density frequency expected does not match the word.')

    def testTextThirdFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(text_words)

        third_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
        frequency_third_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
        print(third_word.text, '; ', frequency_third_word.text[0])

        self.assertEqual(int(frequency_third_word.text[0]), 3, 'The density frequency expected does not match the word.')

#______________________________________________________________________________________________

    # def testWordCounter(self):
    #     driver = self.driver
    #     #Encuentra el contador de palabras 
    #     count_words = driver.find_element_by_id('word_count')
    #     result_text_count_words = int(count_words.text)
    #     print(result_text_count_words, ' words')

    #     expected_value_words = 10

    #     self.assertEquals(expected_value_words, result_text_count_words, "The value does not match the number of words.")

    # def testCharacterCounter(self):
    #     driver = self.driver
    #  #Encuentra el contador de caracteres 
    #     count_character = driver.find_element_by_id('character_count')
    #     result_text_count_character = int(count_character.text)
    #     print(result_text_count_character, ' character')

    #     expected_characters_value = 53

    #     self.assertEquals(expected_characters_value, result_text_count_character, "The value does not match the number of characters.")
       

    # def testFirstFrecuencyCounter(self):
    #     driver = self.driver
       
    #     first_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
    #     frequency_first_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
    #     print(first_word.text, '; ', frequency_first_word.text[0])

    #     self.assertEqual(int(frequency_first_word.text[0]), 2)

    # def testSecondFrecuencyCounter(self):
    #     driver = self.driver

    #     second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
    #     frequency_second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
    #     print(second_word.text, '; ', frequency_second_word.text[0])

    #     self.assertEqual(int(frequency_second_word.text[0]), 1)

    # def testThirdFrecuencyCounter(self):
    #     driver = self.driver
        
    #     third_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
    #     frequency_third_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
    #     print(third_word.text, '; ', frequency_third_word.text[0])

    #     self.assertEqual(int(frequency_third_word.text[0]), 2)




    #Cierra automaticamente el navegador para no consumir memoría en la máquina 

    def tearDown(self):
        self.driver.quit()

    
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'word-counter-report'))
