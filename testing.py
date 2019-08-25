import MicroRegEx
import unittest


class TestRegEx(unittest.TestCase):
    def base(self, file):
        with open(file) as f:
            self.text = f.readlines()

        for line in self.text:
            if line.startswith("#"):
                #  comment line
                continue

            line_list = line.split()
            f_str = None
            pattern = None
            t_str = None
            if len(line_list) == 2:
                pattern, t_str = line_list
            elif len(line_list) == 3:
                pattern, t_str, f_str = line_list
            nfa = MicroRegEx.compile(pattern, use_dfa=True).simplify()
            self.assertEqual(nfa.match(t_str), True)

            if f_str:
                self.assertEqual(nfa.match(f_str), False)
            print(line, "pass")

    def test_basic(self):
        self.base("test_suite.dat")


if __name__ == "__main__":
    unittest.main()
