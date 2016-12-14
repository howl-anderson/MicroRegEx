from MicroRegEx.Automaton.SubsetConstruct.Online import Online
from MicroRegEx.Automaton.SubsetConstruct.Offline import Offline


class NFA2DFA:
    def __init__(self, nfa, offline_converter=False):
        self.nfa = nfa

        if offline_converter:
            self.converter = Offline
        else:
            self.converter = Online

    def convert(self):
        online_convert = self.converter(self.nfa)
        dfa = online_convert.construct()
        return dfa
