import unittest

from MicroRegEx.Automaton.SubsetConstruct.Online import Online
from MicroRegEx.Automaton.Minimal.Brzozowski import Brzozowski
from MicroRegEx.Lexer import Lexer
from MicroRegEx.Parser import Parser
from MicroRegEx.TokenToNFA import TokenToNFA
from MicroRegEx.PatternSyntaxError import PatternSyntaxError


class TestBrzozowski(unittest.TestCase):
    def test_simple_case(self):
        # construct nfa

        # "a(b|c)*" | "abc|bc|ad" | "r0|r1|r2|r3|r4|r5|r6|r7|r8|r9" | "(a|b)*abb"
        pattern = "a(b|c*)"
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

        # dfa.plot()

        simplified_dfa = dfa.simplify()

        simplified_dfa.plot("simplified_dfa")

        brzozowski = Brzozowski(simplified_dfa)

        reversed_nfa = brzozowski.reverse()
        # reversed_nfa.plot("reversed_nfa")

        postfix_minimal_dfa = brzozowski._construct_postfix_minimal_dfa()
        # postfix_minimal_dfa.plot("postfix_minimal_dfa")

        minimal_dfa = brzozowski.construct()

        minimal_dfa.simplify().plot("minimal_dfa")
