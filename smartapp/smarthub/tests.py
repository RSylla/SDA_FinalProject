import unittest
from .a_tickets import *

class FunctionalityTest(unittest.TestCase):

    def test_when_extra_space_removed_then_true (self):
        self.assertTrue(remove_extra("  This  is  with   spaces!  ") == "This is with spaces!")
        self.assertFalse(remove_extra("  This  is  with   spaces!  ") == "  This  is  with   spaces!  ")

    def test_when_characters_counted_then_true(self):
        self.assertTrue(count_characters("counting characters!") == ('All characters: 20;', 'Only characters without spaces: 19;', 'Spaces: 1;', ' Words: 2;'))
        self.assertFalse(count_characters("counting characters!") == ('All characters: 2;', 'Only characters without spaces: 1;', 'Spaces: 1;', ' Words: 2;'))


    def test_when_spell_check_corrected_the_true(self):
        self.assertTrue(spell_check("It is verry loovely dday.")[0] == "It is very lovely day.")
        self.assertFalse(spell_check("It is verry loovely dday.") == "It is verry loovely dday.")
        self.assertTrue(spell_check("It is verry loovely dday.")[1] == "Incorrect words: verry, loovely!")


    def test_when_stop_words_removed_then_true(self):
        self.assertTrue(remove_stopwords("This is a random sentence") == "random, sentence")
        self.assertFalse(remove_stopwords("This is a random sentence") == "This is a random sentence")

if __name__ == '__main__':
    unittest.main()
