import MicroRegEx

regex = MicroRegEx.compile("(a|b)cd*e?")
result = regex.match("abcde")
print(result)

result = regex.match("acde")
print(result)
