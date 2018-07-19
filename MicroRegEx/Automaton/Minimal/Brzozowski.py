from MicroRegEx.Automaton.NFA import NFA
from MicroRegEx.Automaton.DFA import DFA
from MicroRegEx.Automaton.NFA2DFA import NFA2DFA
from MicroRegEx.Automaton.Status import Status


class Brzozowski:
    def __init__(self, dfa: DFA):
        self.dfa = dfa

    def construct(self):
        dfa = self._construct_postfix_minimal_dfa()
        return self._construct_prefix_minimal_dfa(dfa)

    def _construct_prefix_minimal_dfa(self, postfix_minimal_dfa):
        self.dfa = postfix_minimal_dfa.simplify()
        reversed_nfa = self.reverse()

        nfa2dfa = NFA2DFA(reversed_nfa)
        minimal_dfa = nfa2dfa.convert()

        return minimal_dfa

    def _construct_postfix_minimal_dfa(self):
        reversed_nfa = self.reverse()
        nfa2dfa = NFA2DFA(reversed_nfa)
        postfix_minimal_dfa = nfa2dfa.convert()

        return postfix_minimal_dfa

    def reverse(self):
        # reset Status count
        Status.count = 0

        end_status = Status()
        end_status.accept = True

        accept_status_list = []
        status_list = {self.dfa.start: end_status}
        work_list = [self.dfa.start]

        while work_list:
            status = work_list.pop()
            new_status = status_list[status]

            if status not in self.dfa.table:
                # this status gos no where
                continue

            for k, v in self.dfa.table[status].items():
                sub_status = None

                if v not in status_list:
                    sub_status = Status()
                    if v.accept:
                        accept_status_list.append(sub_status)

                    status_list.update({v: sub_status})
                    work_list.append(v)
                else:
                    sub_status = status_list[v]

                sub_status.translate(k, new_status)

        start_status = Status()
        start_status.epsilon = accept_status_list

        return NFA(start_status, end_status)
