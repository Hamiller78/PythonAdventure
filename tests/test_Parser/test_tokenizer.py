import unittest

from Parser.Tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_tokenize_with_valid_commands(self):
        input_string = "n take key"
        expected_tokens = [
            ('N', 'n'),
            ('TAKE', 'take'),
            ('WORD', 'key')
        ]
        self.assertEqual(self.tokenizer.tokenize(input_string), expected_tokens)

    def test_tokenize_with_mixed_case_commands(self):
        input_string = "N tAkE Key"
        expected_tokens = [
            ('N', 'n'),
            ('TAKE', 'take'),
            ('WORD', 'key')
        ]
        self.assertEqual(self.tokenizer.tokenize(input_string), expected_tokens)

    def test_tokenize_with_unknown_words(self):
        input_string = "jump climb run"
        expected_tokens = [
            ('WORD', 'jump'),
            ('WORD', 'climb'),
            ('WORD', 'run')
        ]
        self.assertEqual(self.tokenizer.tokenize(input_string), expected_tokens)

    def test_tokenize_with_empty_string(self):
        input_string = ""
        expected_tokens = []
        self.assertEqual(self.tokenizer.tokenize(input_string), expected_tokens)

    def test_tokenize_with_mixed_valid_and_unknown_words(self):
        input_string = "n jump take climb"
        expected_tokens = [
            ('N', 'n'),
            ('WORD', 'jump'),
            ('TAKE', 'take'),
            ('WORD', 'climb')
        ]
        self.assertEqual(self.tokenizer.tokenize(input_string), expected_tokens)

if __name__ == "__main__":
    unittest.main()