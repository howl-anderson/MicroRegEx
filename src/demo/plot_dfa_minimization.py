import MicroRegEx
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA
from MicroRegEx.Automaton.Minimal.Brzozowski import Brzozowski

nfa = MicroRegEx.compile("(a|b)c?")

dfa = NFA2DFA(nfa).convert().simplify()
mini_dfa = Brzozowski(dfa).construct()
mini_dfa.plot()