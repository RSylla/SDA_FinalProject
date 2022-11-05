# 1.06 Add logic for removing punctuations

import string

text = input("Enter your text: ")
def punctuation_removal(text):
    punctuation = ''''!()-[]{};:'"\,<>./?@#$%^&*_~¤'''

    for char in text:
        if char in punctuation:
            text = text.replace(char, "")
    return text


#print(punctuation_removal(text))

#1.07 Add logic to convert text to upper case and lower case

toggle_upper = True
toggle_lower = False

text = input("Enter your text: ")
def text_upper(text):
    return text.upper()

def text_lower(text):
    return text.lower()

# print(text_upper(text))
# print(text_lower(text))




# 1.08 Add logic to remove new line from text

text = "\nThis is a test case.\nType in your text."
# def remove_new_line(text):
#     text = text.split("\n")
#     text = " ".join(text)
#     return text

def remove_new_line(text):
    return " ".join(text.split())

print(remove_new_line(text))




#1.12 Add logic to generate summary of word


