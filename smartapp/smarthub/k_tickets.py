# 1.06 Add logic for removing punctuations

import wikipedia
import string


# 1.06 Add logic for removing punctuations

text = input("Enter your text: ")
def punctuation_removal(text):
    punctuation = ''''!()-[]{};:'"\,<>./?@#$%^&*_~¤'''

    for char in text:
        if char in punctuation:
            text = text.replace(char, "")
    return text




#1.07 Add logic to convert text to upper case and lower case

toggle_upper = True
toggle_lower = False

text = input("Enter your text: ")
def text_upper(text):
    return text.upper()

def text_lower(text):
    return text.lower()



# 1.08 Add logic to remove new line from text

text = "\nThis is a test case.\nType in your text."
def remove_new_line(text):
    return " ".join(text.split())





#1.12 Add logic to generate summary of word
example = "amazon"
def word_summary(example):
    summary = wikipedia.summary(example)
    return summary


print(word_summary(example))




