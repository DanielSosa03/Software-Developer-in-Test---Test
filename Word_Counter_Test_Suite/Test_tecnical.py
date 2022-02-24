import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

testOneLetter = open('testOneLetter.txt', 'r')
test_One_Letter = testOneLetter.read().lower()

testOneWord = open('testOneWord.txt', 'r')
test_One_Word = testOneWord.read().lower()

testMoreWord = open('testMoreWord.txt', 'r')
test_More_Word = testMoreWord.read().lower()

testNamesWord = open('testNamesWord.txt', 'r')
test_Names_Word = testNamesWord.read().lower()

testTextWord = open('testTextWord.txt', 'r')
test_Text_Word = testTextWord.read().lower()

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

#______________________________________________________________________________________________
    def testOneLetterWordCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_One_Letter)
        
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
        text_field.send_keys(test_One_Letter)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 1

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testFirstOneLetterDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_One_Letter)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'a', 'The density expected does not match the word.')

    def testFirstOneLetterFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_One_Letter)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 1, 'The frequency expected does not match the word.')

#______________________________________________________________________________________________
    def testOneWordWordCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_One_Word)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))


        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 2

        self.assertEquals(expected_value_words, result_text_count_words, "The value expected does not match the number of words.")

    def testOneCharacterCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_One_Word)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 11

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testFirstOneDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_One_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'hello', 'The density expected does not match the word.')

    def testFirstOneFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_One_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 2, 'The frequency expected does not match the word.')

#______________________________________________________________________________________________
    def testMoreWordWordCounter(self):

        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_More_Word)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))


        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 6

        self.assertEquals(expected_value_words, result_text_count_words, "The value expected does not match the number of words.")

    def testMoreCharacterCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_More_Word)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 26

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testMoreOneDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_More_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'dog', 'The density expected does not match the word.')

    def testMoreOneFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_More_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 3, 'The frequency expected does not match the word.')

    def testMoreSecondDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_More_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'cat', 'The density expected does not match the word.')

    def testMoresSecondFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_More_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
  
        second_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
        frequency_second_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
        print(second_word.text, '; ', frequency_second_word.text[0])

        self.assertEqual(int(frequency_second_word.text[0]), 2, 'The frequency expected does not match the word.')

    def testMoreThirdDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_More_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'gerbil', 'The density expected does not match the word.')

    def testMoresThirdFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_More_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
  
        second_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
        frequency_second_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
        print(second_word.text, '; ', frequency_second_word.text[0])

        self.assertEqual(int(frequency_second_word.text[0]), 1, 'The frequency expected does not match the word.')

#______________________________________________________________________________________________
    def testNamesWordWordCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Names_Word)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))


        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 14

        self.assertEquals(expected_value_words, result_text_count_words, "The value expected does not match the number of words.")

    def testNamesCharacterCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Names_Word)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 95

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testNamesOneDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Names_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'pedro', 'The density expected does not match the word.')

    def testNamesOneFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Names_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 4, 'The frequency expected does not match the word.')

    def testNamesSecondDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Names_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'daniel', 'The density expected does not match the word.')

    def testNamesSecondFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Names_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

        second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
        frequency_second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
        print(second_word.text, '; ', frequency_second_word.text[0])

        self.assertEqual(int(frequency_second_word.text[0]), 3, 'The frequency expected does not match the word.')

    def testNamesThirdDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Names_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'edward', 'The density expected does not match the word.')

    def testNamesThirdFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Names_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
  
        third_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
        frequency_third_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
        print(third_word.text, '; ', frequency_third_word.text[0])

        self.assertEqual(int(frequency_third_word.text[0]), 2, 'The frequency expected does not match the word.')

#______________________________________________________________________________________________
    def testTextWordWordCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Text_Word)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))


        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 152

        self.assertEquals(expected_value_words, result_text_count_words, "The value expected does not match the number of words.")

    def testTextCharacterCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Text_Word)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 912

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testTextOneDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Text_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'black', 'The density expected does not match the word.')

    def testTextOneFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Text_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 6, 'The frequency expected does not match the word.')

    def testTextSecondDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Text_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'hole', 'The density expected does not match the word.')

    def testTextSecondFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Text_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

        second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
        frequency_second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
        print(second_word.text, '; ', frequency_second_word.text[0])

        self.assertEqual(int(frequency_second_word.text[0]), 3, 'The frequency expected does not match the word.')

    def testTextThirdDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Text_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, 'spacetime', 'The density expected does not match the word.')

    def testTextThirdFrecuencyCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Text_Word)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

        third_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
        frequency_third_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
        print(third_word.text, '; ', frequency_third_word.text[0])

        self.assertEqual(int(frequency_third_word.text[0]), 3, 'The frequency expected does not match the word.')

#______________________________________________________________________________________________
    def testNumbersWordCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Number_sWord)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))


        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 9

        self.assertEquals(expected_value_words, result_text_count_words, "The value expected does not match the number of words.")

    def testNumbersCharacterCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Number_sWord)
        
        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))

     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 33

        self.assertEquals(expected_characters_value, result_text_count_character, "The value expected does not match the number of characters.")

    def testNumbersOneDensityCounter(self):
        driver = self.driver

        text_field = driver.find_element_by_id('box')
        text_field.send_keys(test_Number_sWord)

        #Espera implicita
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[3]/button')))
       
        first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(first_word.text, '49', 'The density expected does not match the word.')

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

#______________________________________________________________________________________________
    #Cierra automaticamente el navegador para no consumir memoría en la máquina 
    def tearDown(self):
        self.driver.quit()

    
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'word-counter-report'))
