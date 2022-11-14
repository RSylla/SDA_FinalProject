from textblob import TextBlob, Word
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from .k_tickets import punctuation_removal

# 1.09 Add logic to remove extra space
def remove_extra(string):

    while '  ' in string:
        string = string.replace('  ', ' ')

    return string.strip()


# 1.10 Add logic to count characters
def count_characters(text):

    if text:
        with_spaces = len(text)
        without_spaces = len(text) - text.count(' ')
        spaces = text.count(' ')
        num_words = int(len(text.split()))

        char_count = f"All characters: {with_spaces};"
        char_wo_spaces = f"Only characters without spaces: {without_spaces};"
        space_count = f"Spaces: {spaces};"
        word_count = f" Words: {num_words};"

        return char_count, char_wo_spaces, space_count, word_count


#1.11 Add logic to check for text spellings
def spell_check(text):
    corrected = TextBlob(text)
    incorrect_words = []
    for word in text.split():
        wordy = Word(word).spellcheck()[0]
        if wordy[0] != word and wordy[1] >= 0.7:
            incorrect_words.append(word)

    corrected_text = corrected.correct()
    incorrect_words= f"Incorrect words: {', '.join(incorrect_words)}!"

    return corrected_text, incorrect_words


# 1.13 Add logic to remove stop words from text
def remove_stopwords(text):
    text = punctuation_removal(text)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:

            filtered_sentence.append(w)

    wo_stopwords = f"{', '.join(filtered_sentence)}"

    return wo_stopwords






