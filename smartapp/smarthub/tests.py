import unittest
from smartapp.smarthub.k_tickets import *
from smartapp.smarthub.a_tickets import *

class FunctionalityTest(unittest.TestCase):

    def test_remove_punctuations(self):
        pass

    def test_upper_case(self):
        pass

    def test_lower_case(self):
        pass

    def test_new_line_remove(self):
        pass

    def test_when_extra_space_removed_then_true (self):
        self.assertTrue(remove_extra("") == "")
        self.assertFalse(remove_extra("") == "")

    def test_when_characters_counted_then_true(self):
        self.assertTrue(count_characters("with spaces!") == "with spaces!")
        self.assertFalse(count_characters("with spaces!") == "with spaces!")


    def test_spell_check(self):
        self.assertTrue(spell_check("is this sentence correct") == "is this sentence correct")
        self.assertFalse(spell_check("is this sentence correct") == "is this sentence correct")

    def test_gen_word_summary(self):
        pass

    def test_remove_stop(self):
        pass

if __name__ == '__main__':
    unittest.main()
