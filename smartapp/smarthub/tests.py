from django.test import TestCase

# Create your tests here.

toggle_upper = True
toggle_lower = False

text = "Suvaline text, mida on vaja muuta."

def text_upper(text):
    return text.upper()

def text_lower(text):
    return text.lower()




text = "\n Suvaline text, mis on vaja muuta!\n Ma ei tea kas see on norm."
def rem_new_line(text):
    text = text.split()
    text = " ".join(text)
    return text

def remove_new_line(text):
    return " ".join(text.split())

print(rem_new_line(text))
print(remove_new_line(text))
