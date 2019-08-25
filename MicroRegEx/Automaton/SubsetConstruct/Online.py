import collections

from MicroRegEx.Automaton.DFA import DFA
from MicroRegEx.Automaton.StatusSet import StatusSet


class Online:
    def __init__(self, nfa):
        self.nfa = nfa

    def construct(self):
        self.nfa.current_status = {self.nfa.start}
        self.nfa.epsilon()

        dfa_start_status = StatusSet(self.nfa.current_status)
        relation_set = []
        dfa_status_set = [dfa_start_status]
        work_list = [dfa_start_status]
        dfa = DFA(dfa_start_status)

        while len(work_list):
            status_set = work_list.pop()

            next_status_mapping = SetDict()
            for status in status_set:
                for k, v in status.translation.items():
                    self.nfa.current_status = set(v)
                    self.nfa.epsilon()
                    epsilon_status = self.nfa.current_status

                    next_status = {k: StatusSet(epsilon_status)}
                    next_status_mapping.extend(next_status)

            for k, v in next_status_mapping.items():
                v = StatusSet(v)
                relation_item = (status_set, k, v)
                if relation_item not in relation_set:
                    relation_set.append(relation_item)
                    dfa.translate(status_set, k, v)

                if v not in dfa_status_set:
                    dfa_status_set.append(v)
                    work_list.append(v)

        return dfa


class SetDict(dict):
    def __setitem__(self, key, value):
        if isinstance(value, collections.Sequence) or isinstance(value, set):
            super().__setitem__(key, set(value))
        else:
            msg = "Not support for %s: %s".format(repr(key), repr(value))
            raise ValueError(msg)

    def extend(self, other: dict):
        for k, v in other.items():
            if k in self:
                self[k].update(set(v))
            else:
                self[k] = set(v)
