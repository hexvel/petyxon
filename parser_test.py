from lexer.lexer import Lexer

code = """
объявить x = 10
если x > 5:
    вывести "x больше 5"
"""

lexer = Lexer(code)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
