import operator

def wordsCounterCharacters(words):
    #Contador de caracteres 
    counter = 0
    while words[counter:]:
        counter += 1
    print(counter, '\tcharacters')
    return counter

def wordsCounterWords(words):
    #Contador de palabras
    words = words.split()
    words_list = []

    for i in words:
        words_list.append(i)
    print(len(words_list), '\twords')


def wordsFrequencyDos(words):
    #Contador de la frecuencia de las palabras
    def count(elements):
        #Ignora el punto
        if elements[-1] == '.':
            elements = elements[0:len(elements) - 1]
        if elements[-1] == ',':
            elements = elements[0:len(elements) - 1]
        #Contador de elementos 
        if elements in dictionary:
            dictionary[elements] += 1

        else:
            dictionary.update({elements: 1})
    #Declara el diccionario 
    dictionary = {}
    #Divide las palabras entrantes del texto 
    lis = words.split()

    #Cuenta los elementos en el lis
    for elements in lis:
        count(elements)

    for allKeys in dictionary:
        
        sortedDict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    for result in sortedDict:
        print(result[0] + ":\t" + str(result[1]))

def run():
    #Ledctura del documento
    open_words = open('words.txt', 'r')
    words = open_words.read().lower()

    wordsCounterWords(words)
    wordsCounterCharacters(words)
    wordsFrequencyDos(words)

if __name__ == "__main__":
    run()

