import unittest

from MicroRegEx.Lexer import Lexer
from MicroRegEx.Parser import Parser


class TestParser(unittest.TestCase):
    def test_simple(self):
        pattern = "abc"
        print("Pattern: {}".format(pattern))

        lexer = Lexer(pattern)
        lexer.analyse()
        parser = Parser(lexer)
        postfix_expr = parser.parse()

        for i in postfix_expr:
            print(i)

        self.assertEqual(1, 2)

    def test_middle_case(self):
        pattern = r"(ab|a)(bc|c)"
        print("Pattern: {}".format(pattern))

        lexer = Lexer(pattern)
        lexer.analyse()
        parser = Parser(lexer)
        postfix_expr = parser.parse()

        for i in postfix_expr:
            print(i)

        self.assertEqual(1, 2)

    def test_complicate_case(self):
        pattern = r"(((d|e)?)|(a+))+"
        print("Pattern: {}".format(pattern))

        lexer = Lexer(pattern)
        lexer.analyse()
        parser = Parser(lexer)
        postfix_expr = parser.parse()

        for i in postfix_expr:
            print(i)

        self.assertEqual(1, 2)
