import unittest

from MicroRegEx.Token import Token, CHARACTER
from MicroRegEx.TokenToNFA import TokenToNFA


class TestTokenToNFA(unittest.TestCase):
    def test_char_nfa(self):
        pass

    def test_asterisk_nfa(self):
        token_to_nfa = TokenToNFA([])
        token_to_nfa.char_nfa(Token(CHARACTER, "a"))
        token_to_nfa.asterisk_nfa()
        nfa = token_to_nfa.nfa_stack[0]

        # result = nfa.match("")
        # self.assertEqual(result, True)

        result = nfa.match("a")
        self.assertEqual(result, True)

        result = nfa.match("aa")
        self.assertEqual(result, True)

    def test_question_nfa(self):
        token_to_nfa = TokenToNFA([])
        token_to_nfa.char_nfa(Token(CHARACTER, "a"))
        token_to_nfa.question_nfa()
        nfa = token_to_nfa.nfa_stack[0]

        result = nfa.match("")
        self.assertEqual(result, True)

        result = nfa.match("a")
        self.assertEqual(result, True)

        result = nfa.match("aa")
        self.assertEqual(result, False)

    def test_plus_nfa(self):
        token_to_nfa = TokenToNFA([])
        token_to_nfa.char_nfa(Token(CHARACTER, "a"))
        token_to_nfa.plus_nfa()
        nfa = token_to_nfa.nfa_stack[0]

        result = nfa.match("")
        self.assertEqual(result, False)

        result = nfa.match("a")
        self.assertEqual(result, True)

        result = nfa.match("aa")
        self.assertEqual(result, True)

    def test_bar_nfa(self):
        token_to_nfa = TokenToNFA([])
        token_to_nfa.char_nfa(Token(CHARACTER, "a"))
        token_to_nfa.char_nfa(Token(CHARACTER, "b"))
        token_to_nfa.bar_nfa()
        nfa = token_to_nfa.nfa_stack[0]

        result = nfa.match("")
        self.assertEqual(result, False)

        result = nfa.match("a")
        self.assertEqual(result, True)

        result = nfa.match("b")
        self.assertEqual(result, True)

        result = nfa.match("c")
        self.assertEqual(result, False)

    def test_concatenate_nfa(self):
        token_to_nfa = TokenToNFA([])
        token_to_nfa.char_nfa(Token(CHARACTER, "a"))
        token_to_nfa.char_nfa(Token(CHARACTER, "b"))
        token_to_nfa.concatenate_nfa()
        nfa = token_to_nfa.nfa_stack[0]

        result = nfa.match("")
        self.assertEqual(result, False)

        result = nfa.match("a")
        self.assertEqual(result, False)

        result = nfa.match("b")
        self.assertEqual(result, False)

        result = nfa.match("ab")
        self.assertEqual(result, True)

        result = nfa.match("abc")
        self.assertEqual(result, False)
