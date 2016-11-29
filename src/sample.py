import MicroRegEx

regex = MicroRegEx.compile("(a|b)cd*e?")
result = regex.match("abcde")
