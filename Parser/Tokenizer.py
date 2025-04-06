class Tokenizer:
    def __init__(self):
        self.token_specification = [
            'N',
            'E',
            'S',
            'W',
            'U',
            'D',
            'GO',
            'LOOK',
            'TAKE',
            'DROP',
            'USE',
            'TALK',
            'GIVE',
            'WORD'
        ]
        
    def tokenize(self, input_string):
        tokens = []

        words = input_string.split()
        for word in words:
            word_upper = word.upper()
            if word_upper in self.token_specification:
                tokens.append((word_upper, word.lower()))
            else:
                tokens.append(('WORD', word.lower()))

        return tokens