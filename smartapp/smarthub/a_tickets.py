from textblob import TextBlob   #for ticket 1.11

# 1.09 Add logic to remove extra space
def remove_extra(string):

    while '  ' in string:
        string = string.replace('  ', ' ')

    return string.strip()


# 1.10 Add logic to count characters
def count_characters(string):

    if string:
        with_spaces = len(string)
        without_spaces = len(string) - string.count(' ')
        spaces = string.count(' ')
        num_words = len(string.split())

    return (f"All characters: {with_spaces} \nOnly characters (without spaces): {without_spaces} \nSpaces: {spaces} \nWords: {num_words}")


# 1.11 Add logic to check for text spellings
# pip install textblob

from textblob import TextBlob, Word
from smartapp.smarthub.k_tickets import punctuation_removal


def spell_check(text):
    text = punctuation_removal(text)
    corrected = TextBlob(text)
    incorrect_words = []
    for word in text.split():
        wordy = Word(word).spellcheck()[0]
        if wordy[0] != word and wordy[1] >= 0.7:
            incorrect_words.append(word)
    print(incorrect_words)
    return (f"Corrected text: {corrected.correct()}, \nThese words were incorrect: {incorrect_words}")


# 1.13 Add logic to remove stop words from text

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

"""terminali:
python -m nltk.downloader stopwords
või 
nltk.download('stopwords') ...viimane ei tööta"""


text = """This IS a sample sentence, showing off the stop words filtration."""


def remove_stopwords(text):
    text = text
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:

            filtered_sentence.append(w)
    return (f"Original sentence: {text}, \nFiltered sentence: {filtered_sentence}")


print(remove_stopwords(text))


