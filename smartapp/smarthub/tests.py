<<<<<<< HEAD
<<<<<<< HEAD
import unittest
from .a_tickets import *

class FunctionalityTest(unittest.TestCase):

    def test_when_extra_space_removed_then_true (self):
        self.assertTrue(remove_extra("  This  is  with   spaces!  ") == "This is with spaces!")
        self.assertFalse(remove_extra("  This  is  with   spaces!  ") == "  This  is  with   spaces!  ")

    def test_when_characters_counted_then_true(self):
        self.assertTrue(count_characters("counting characters!") == ('All characters: 20;', 'Only characters without spaces: 19;', 'Spaces: 1;', ' Words: 2;'))
        self.assertFalse(count_characters("counting characters!") == ('All characters: 2;', 'Only characters without spaces: 1;', 'Spaces: 1;', ' Words: 2;'))
=======
=======
>>>>>>> Anneli
from unittest import TestCase
from .k_tickets import *
from .a_tickets import *

class FunctionalityTest(TestCase):

    def test_remove_punctuations(self):
        pass

    def test_upper_case(self):
        pass

    def test_lower_case(self):
        pass

    def test_new_line_remove(self):
        pass
<<<<<<< HEAD
>>>>>>> Anneli
=======
=======
import unittest
from .a_tickets import *

class FunctionalityTest(unittest.TestCase):

    def test_when_extra_space_removed_then_true (self):
        self.assertTrue(remove_extra("  This  is  with   spaces!  ") == "This is with spaces!")
        self.assertFalse(remove_extra("  This  is  with   spaces!  ") == "  This  is  with   spaces!  ")

    def test_when_characters_counted_then_true(self):
        self.assertTrue(count_characters("counting characters!") == ('All characters: 20;', 'Only characters without spaces: 19;', 'Spaces: 1;', ' Words: 2;'))
        self.assertFalse(count_characters("counting characters!") == ('All characters: 2;', 'Only characters without spaces: 1;', 'Spaces: 1;', ' Words: 2;'))
>>>>>>> 1e8946203ccb68e38738d3840b19f600bc11bcae
>>>>>>> Anneli

    def test_extra_space_remove(self):
        pass

<<<<<<< HEAD
<<<<<<< HEAD
=======
    def test_count_characters(self):
        pass
=======
>>>>>>> Anneli
    def test_when_spell_check_corrected_the_true(self):
        self.assertTrue(spell_check("It is verry loovely dday.")[0] == "It is very lovely day.")
        self.assertFalse(spell_check("It is verry loovely dday.") == "It is verry loovely dday.")
        self.assertTrue(spell_check("It is verry loovely dday.")[1] == "Incorrect words: verry, loovely!")
<<<<<<< HEAD
=======
    def test_count_characters(self):
        pass
>>>>>>> Anneli
=======
>>>>>>> 1e8946203ccb68e38738d3840b19f600bc11bcae
>>>>>>> Anneli

    def test_spell_check(self):
        pass

<<<<<<< HEAD
<<<<<<< HEAD
    def test_when_stop_words_removed_then_true(self):
        self.assertTrue(remove_stopwords("This is a random sentence") == "random, sentence")
        self.assertFalse(remove_stopwords("This is a random sentence") == "This is a random sentence")
=======
=======
>>>>>>> Anneli
    def test_gen_word_summary(self):
        pass

    def test_remove_stop(self):
        pass
<<<<<<< HEAD
>>>>>>> Anneli
=======
=======
    def test_when_stop_words_removed_then_true(self):
        self.assertTrue(remove_stopwords("This is a random sentence") == "random, sentence")
        self.assertFalse(remove_stopwords("This is a random sentence") == "This is a random sentence")
>>>>>>> 1e8946203ccb68e38738d3840b19f600bc11bcae
>>>>>>> Anneli

if __name__ == '__main__':
    unittest.main()
