import nltk
import pandas as pd
import re
import string

from num2words import num2words

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

from nltk.corpus import stopwords


def txt_preprocessing(sentence):

    """Tokenize text and convert text to lowercase
       Convert number to their textual representation
       Remove punctuation marks
       Remove stop words
       Eliminating Affixes 
       Return list of clean text words
    """

    tokens = re.split("\W+", sentence)

    # to lower case
    sentence = sentence.lower()

    # number to textual representation
    for i in range(0, len(sentence)):
        if sentence[i].isdigit():
            temp_digit = sentence[i]
            for j in range(i + 1, len(sentence)):
                if sentence[j].isdigit():
                    temp_digit = temp_digit + sentence[j]
                else:
                    break
            sentence = sentence.replace(temp_digit, num2words(temp_digit, lang='en'))

    # removing punctuation
    punc = string.punctuation
    sentence = [character for character in sentence if character not in punc]
    sentence = ''.join(sentence)

    # removing stop words
    stop_words = (stopwords.words('english'))
    sentence = sentence.split(' ')

    for i in sentence:
        for w in stop_words:
            if w == i:
                sentence.remove(i)

    # stemming
    porter = PorterStemmer()
    for i in range(0, len(sentence)):
        sentence[i] = porter.stem(sentence[i])

    return sentence
