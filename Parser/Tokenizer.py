from Parser.TokenType import TokenType

class Tokenizer:
    def __init__(self):
        pass
    def tokenize(self, input_string):
        tokens = []

        words = input_string.split()
        for word in words:
            word_lower = word.lower()
            word_upper = word.upper()
            # Check if the word matches any value in the TokenType enum
            matching_token = next((token for token in TokenType if token.value == word_upper), None)
            if matching_token:
                tokens.append((matching_token, word_lower))
            else:
                tokens.append((TokenType.WORD, word_lower))

        return tokens