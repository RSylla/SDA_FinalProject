

# 1.09 Add logic to remove extra space

string = "       Täiesti    suvaline          proov!"


def remove_extra(string):

    while '  ' in string:
        string = string.replace('  ', ' ')

    return string.strip()


print(remove_extra(string))


# 1.10 Add logic to count characters

string = "How many characters are thereu on märke on lauses tühikutega ja ilma?"


def count_characters(string):

    if string:
        with_spaces = len(string)
        without_spaces = len(string) - string.count(' ')
        spaces = string.count(' ')
        num_words = len(string.split())

    return (f"Characters with spaces: {with_spaces} \nCharacters without spaces: {without_spaces} \nSpaces: {spaces} \nWords: {num_words}")


print(count_characters(string))


