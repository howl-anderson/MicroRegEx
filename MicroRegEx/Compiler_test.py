import unittest

from MicroRegEx.Compiler import Compiler


class TestCompiler(unittest.TestCase):
    def test_simple(self):
        pattern = "abc"
        print("Pattern: {}".format(pattern))

        regex = Compiler().compile(pattern)

        result = regex.match("abc")
        self.assertEqual(result, True)

        result = regex.match("ac")
        self.assertEqual(result, False)

        result = regex.match("abcd")
        self.assertEqual(result, False)

    def test_middle_case(self):
        pattern = r"(ab|a)(bc|c)"
        print("Pattern: {}".format(pattern))

        regex = Compiler().compile(pattern)

        result = regex.match("abc")
        self.assertEqual(result, True)

        result = regex.match("acb")
        self.assertEqual(result, False)

    def test_complicate_case(self):
        pattern = r"((d|e)|(a+))+"
        print("Pattern: {}".format(pattern))

        regex = Compiler().compile(pattern)

        result = regex.match("d")
        self.assertEqual(result, True)

        result = regex.match("e")
        self.assertEqual(result, True)

        result = regex.match("aa")
        self.assertEqual(result, True)

        result = regex.match("ee")
        self.assertEqual(result, True)
