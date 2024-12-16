import re

from lexer.tokens import TOKENS


class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        for name, pattern in TOKENS.items():
            for match in re.finditer(pattern, self.code):
                self.tokens.append((name, match.group(0)))
        return self.tokens
