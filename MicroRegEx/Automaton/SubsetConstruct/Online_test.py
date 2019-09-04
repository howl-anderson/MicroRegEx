import unittest

from .Online import Online
from MicroRegEx.Lexer import Lexer
from MicroRegEx.Parser import Parser
from MicroRegEx.TokenToNFA import TokenToNFA
from MicroRegEx.PatternSyntaxError import PatternSyntaxError


class TestOnline(unittest.TestCase):
    def test_simple_case(self):
        # construct nfa
        pattern = "abc|bc|ad"  # "a(b|c)*" | ""
        lexer = Lexer(pattern)
        lexer.analyse()

        parser = Parser(lexer)
        postfix_expr = parser.parse()

        nfa_stack = TokenToNFA(postfix_expr).translate()
        if len(nfa_stack) != 1:
            raise PatternSyntaxError
        nfa = nfa_stack[0]

        # nfa.plot()

        online = Online(nfa)
        dfa = online.construct()

        dfa.plot()

        simplified_dfa = dfa.simplify()

        simplified_dfa.plot("simplified_dfa")
