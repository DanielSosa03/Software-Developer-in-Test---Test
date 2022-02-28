# Software-Developer-in-Test---Test
In this repository you will find the algorithm designed in python that will read a text .txt file to count the frequency of words in the text along with the number of words and characters. You will also find the Test Suite for the page https://wordcounter.net/ creating a set of tests that validate the # of words, the # of characters and the frequency of words in a text.

____________________________________________________________________________________________________

All the files are located in the MASTER branch, there you will find the tests and the text counter algorithm.
In the Word_Frequency_Counter folder there is a file Word_Frequency_Counter.py developed in Python that will read the text file words.txt and will be in charge of counting the number of words, the number of characters and the frequency with which each word is counted.
To execute this file it is necessary to have Python in your preferred version, once you have Python you can run the code from the terminal, you have to keep in mid the location of the repository where the file has been cloned, once in the terminal you are in the corresponding location, you can execute the command "python Word_Frequency_Counter.py" or " python3 Word_Frequency_Counter.py" or the command "py Word_Frequency_Counter.py" to execute.
Once the execution of the file is finished, it will give you the results in a histogram summarizing the number of words counted, the number of characters found and the frequency with which each word is repeated in descending order.
If you want to change the text, you can open the words.txt file and edit the preferred text you want to evaluate, SUCCESSES.

____________________________________________________________________________________________________

In the Word_Counter_Test_Suite folder you will find several files that will be in charge of carrying out the test tests to be executed on the https://wordcounter.net/ page and thus validate the different tests that are going to be carried out, such as the number of words, the number of characters and the 3 most repeated words with the number of repetitions.
To run the Test_tecnical.py file, it is necessary to have a version of python greater than 3.5 and less than 3.8 to avoid conflicts in the execution, it is also necessary to download the chromedriver.exe with the version required by your browser https:// chromedriver.chromium.org/downloads, and finally it is also necessary to download the Unittest, Selenium and Pyunitreport packages, the latter is the one that generates the reports in an html file.
Once you have configured all the requirements, now you can run the Test_tecnical.py file from the terminal with its corresponding location, using the commands "python Test_tecnica.py" or "python3 Test_tecnica.py" or the command "py Test_tecnica.py ", it will start opening Google Chrome pop-up windows performing all the tests to validate the operation of the page, it will take several minutes to generate the report that will be in the \reports\reports folder in an html file called word-counter-report .html, there you will find all the test cases that were executed, reporting the cases that passed, and those that failed.
The .txt files contain the texts, words, numbers and other entries that were taken into account for the designed scenarios.
