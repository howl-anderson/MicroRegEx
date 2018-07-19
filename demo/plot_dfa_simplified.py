import MicroRegEx
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA

nfa = MicroRegEx.compile("(a|b)c?")

dfa = NFA2DFA(nfa).convert().simplify()
dfa.plot()