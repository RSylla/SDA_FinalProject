import unittest

from smartapp.smarthub.k_tickets import text_upper, text_lower, punctuation_removal, remove_new_line, word_summary


class TestTextMethods(unittest.TestCase):
    def test_remove_punctuation(self):
        self.assertTrue(punctuation_removal('Hi! How are you doing?!...¤') == 'Hi How are you doing')
        self.assertFalse(punctuation_removal('Hi! How are you doing?!...¤') == 'Hi! How are you doing?!...¤')

    def test_upper_case(self):
        self.assertTrue(text_upper('PYTHON') == 'PYTHON')
        self.assertFalse(text_upper('python') == 'python')

    def test_lower_case(self):
        self.assertTrue(text_lower('python') == 'python')
        self.assertFalse(text_lower('PYTHON') == 'PYTHON')

    def test_remove_new_line(self):
        self.assertFalse(remove_new_line('First,\n I wake up.') == 'I wake up.')
        self.assertTrue(remove_new_line('First, I wake up.') == 'First, I wake up.')

    def test_word_summary(self):
        self.assertFalse(word_summary('amazon') == 'It is an American multinational technology company.')
        self.assertTrue(bool(word_summary('amazon')))


    if __name__ == '__main__':
        unittest.main()
