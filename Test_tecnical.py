import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver 
from time import sleep 

#Lectura del documento .txt
open_words = open('words.txt', 'r')
words = open_words.read().lower()

class WordCounterTestSuite(unittest.TestCase):

    #Abertura del navegador y la página 
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)

        driver.get('https://wordcounter.net/')
        driver.maximize_window()
        text_field = driver.find_element_by_id('box')  
        text_field.clear()

        #Ingresa el texto del archivo .txt a la casilla de la página 
        text_field.send_keys(words)
        sleep(4) #Toca crear una espera 


    # Se establecen los casos de pruebas

    def testWordCounter(self):
        driver = self.driver
        #Encuentra el contador de palabras 
        count_words = driver.find_element_by_id('word_count')
        result_text_count_words = int(count_words.text)
        print(result_text_count_words, ' words')

        expected_value_words = 10

        self.assertEquals(expected_value_words, result_text_count_words, "The value does not match the number of words.")

    def testCharacterCounter(self):
        driver = self.driver
     #Encuentra el contador de caracteres 
        count_character = driver.find_element_by_id('character_count')
        result_text_count_character = int(count_character.text)
        print(result_text_count_character, ' character')

        expected_characters_value = 53

        self.assertEquals(expected_characters_value, result_text_count_character, "The value does not match the number of characters.")
       

    def testFirstFrecuencyCounter(self):
        driver = self.driver
       
        first_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[2]')
        frequency_first_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[1]/span[1]')
        print(first_word.text, '; ', frequency_first_word.text[0])

        self.assertEqual(int(frequency_first_word.text[0]), 2)

    def testSecondFrecuencyCounter(self):
        driver = self.driver

        second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[2]')
        frequency_second_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[2]/span[1]')
        print(second_word.text, '; ', frequency_second_word.text[0])

        self.assertEqual(int(frequency_second_word.text[0]), 1)

    def testThirdFrecuencyCounter(self):
        driver = self.driver
        
        third_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[2]')
        frequency_third_word = driver.find_element_by_xpath(f'/html/body/div[6]/div[1]/div[5]/div/div[2]/div[2]/div[1]/a[3]/span[1]')
        print(third_word.text, '; ', frequency_third_word.text[0])

        self.assertEqual(int(frequency_third_word.text[0]), 2)




    #Cierra automaticamente el navegador para no consumir memoría en la máquina 

    def tearDown(self):
        self.driver.quit()

    
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'word-counter-report'))
