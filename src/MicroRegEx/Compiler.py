from src.MicroRegEx.Lexer import Lexer
from src.MicroRegEx.Parser import Parser
from src.MicroRegEx.PatternSyntaxError import PatternSyntaxError
from src.MicroRegEx.TokenToNFA import TokenToNFA


class Compiler:
    def __init__(self):
        self.lexeme_begin = 0

    def compile(self, pattern):
        lexer = Lexer(pattern)
        lexer.analyse()

        parser = Parser(lexer)
        postfix_expr = parser.parse()

        nfa_stack = TokenToNFA(postfix_expr).translate()
        if len(nfa_stack) != 1:
            raise PatternSyntaxError
        else:
            return nfa_stack[0]