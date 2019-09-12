[中文版本的 README](README.md)
------------------------------

## What's MicroRegEx
MicroRegEx is a micro regular expression engine.

## Operator
* `*` - zero or more repetitions
* `+` - one or more repetitions
* `?` - optional
* `a|b` - matches a or b
* `(expr)` - treat the `expr` as an atom
* `\` - escape character

## Usage
### Use like python built-in regex
```python
import MicroRegEx

regex = MicroRegEx.compile("(a|b)cd*e?")
result = regex.match("abcde")
print(result)

result = regex.match("acde")
print(result)
```

will output:
```text
False
True
```

### Plot NFA
```python
import MicroRegEx

regex = MicroRegEx.compile("(a|b)c?")
regex.plot()
```

will plot graph as fellow:
![NFA](img/nfa.png)

### Translate to DFA
#### NFA to DFA
##### Native DFA
```python
import MicroRegEx
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA

nfa = MicroRegEx.compile("(a|b)c?")

dfa = NFA2DFA(nfa).convert()
dfa.plot()
```

will plot graph as fellow:
![DFA_native](img/dfa_native.png)

##### Simplified DFA
```python
import MicroRegEx
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA

nfa = MicroRegEx.compile("(a|b)c?")

dfa = NFA2DFA(nfa).convert().simplify()
dfa.plot()
```

will plot graph as fellow:
![DFA_simplified](img/dfa_simplified.png)

#### DFA minimization
##### Brzozowski method
```python
import MicroRegEx
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA
from MicroRegEx.Automaton.Minimal.Brzozowski import Brzozowski

nfa = MicroRegEx.compile("(a|b)c?")

dfa = NFA2DFA(nfa).convert().simplify()
mini_dfa = Brzozowski(dfa).construct()
mini_dfa.plot()
```

will plot graph as fellow:
![DFA_mini](img/dfa_mini.png)

## Test
Test pass by a test data set which contains 64 examples. Please run `python ./testing.py` for a detailed test.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledge & Credits
1. Inspire by the [regex](https://github.com/xysun/regex) project of [xysun](https://github.com/xysun)
2. Some Documents from [regular\_expression\_engine](https://github.com/lihao98722/regular_expression_engine) project of [lihao98722](https://github.com/lihao98722/)
3. Test suite is based on [Glenn Fowler](http://www.research.att.com/~gsf/testregex/)'s regex test suites.
4. Test script is cloned from [regex](https://github.com/xysun/regex) project with some modification.

## Reference
* [Implementing Regular Expressions](https://swtch.com/~rsc/regexp/)
