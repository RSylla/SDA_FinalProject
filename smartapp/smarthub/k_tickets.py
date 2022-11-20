import wikipedia
from string import punctuation


# 1.06 Add logic for removing punctuations
def punctuation_removal(text, punctuation):

    for char in text:
        if char in punctuation:
            text = text.replace(char, "")
    return text


#1.07 Add logic to convert text to upper case and lower case
def text_upper(text):
    return text.upper()


def text_lower(text):
    return text.lower()


# 1.08 Add logic to remove new line from text
def remove_new_line(text):
    return " ".join(text.split())


#1.12 Add logic to generate summary of word
def word_summary(example):
    try:
        search_suggestion = wikipedia.search(example, results=5)
        summary = wikipedia.summary(example)
        return f'{summary}\n\n You might want to consider these words also: {", ".join(search_suggestion)}.'
    except wikipedia.exceptions.DisambiguationError as e:
        return f"The word '{example}' may refer to: {e.options}"
    except wikipedia.exceptions.PageError:
        return f'Your text "{example}" does not match any pages to Generate Summary Of a Word. Try another text!'




