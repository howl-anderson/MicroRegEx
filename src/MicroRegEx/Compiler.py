from MicroRegEx.Lexer import Lexer
from MicroRegEx.Parser import Parser
from MicroRegEx.PatternSyntaxError import PatternSyntaxError
from MicroRegEx.TokenToNFA import TokenToNFA
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA


class Compiler:
    def __init__(self):
        self.lexeme_begin = 0

    def compile(self, pattern, use_dfa=False):
        lexer = Lexer(pattern)
        lexer.analyse()

        parser = Parser(lexer)
        postfix_expr = parser.parse()

        nfa_stack = TokenToNFA(postfix_expr).translate()
        if len(nfa_stack) != 1:
            raise PatternSyntaxError

        automaton = nfa_stack[0]

        if use_dfa:
            nfa2dfa = NFA2DFA(automaton)
            automaton = nfa2dfa.convert()

        return automaton
