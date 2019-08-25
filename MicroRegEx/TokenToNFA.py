from MicroRegEx.Automaton.NFA import NFA
from MicroRegEx.Automaton.Status import Status
from MicroRegEx.Token import CONCATENATE, ASTERISK, QUESTION, PLUS, BAR, CHARACTER


class TokenToNFA:
    def __init__(self, token):
        self.tokens = token
        self.nfa_stack = []

    def translate(self):
        for token in self.tokens:
            if token.token is CHARACTER:
                self.char_nfa(token)
            if token.token is ASTERISK:
                self.asterisk_nfa()
            if token.token is QUESTION:
                self.question_nfa()
            if token.token is PLUS:
                self.plus_nfa()
            if token.token is BAR:
                self.bar_nfa()
            if token.token is CONCATENATE:
                self.concatenate_nfa()
        return self.nfa_stack

    def char_nfa(self, token):
        start_status = Status()
        end_status = Status()
        start_status.translate(token.value, end_status)
        end_status.accept = True
        nfa = NFA(start_status, end_status)
        self.nfa_stack.append(nfa)

    def asterisk_nfa(self):
        start_status = Status()
        end_status = Status()
        nfa = self.nfa_stack.pop()
        start_status.epsilon.append(nfa.start)
        nfa.end.accept = False
        end_status.accept = True
        nfa.end.epsilon.append(nfa.start)
        nfa.end.epsilon.append(end_status)
        start_status.epsilon.append(end_status)
        self.nfa_stack.append(NFA(start_status, end_status))

    def question_nfa(self):
        nfa = self.nfa_stack.pop()
        nfa.start.epsilon.append(nfa.end)
        self.nfa_stack.append(nfa)

    def plus_nfa(self):
        start_status = Status()
        end_status = Status()
        end_status.accept = True
        nfa = self.nfa_stack.pop()
        nfa.end.accept = False
        nfa.end.epsilon.append(nfa.start)
        start_status.epsilon.append(nfa.start)
        nfa.end.epsilon.append(end_status)
        self.nfa_stack.append(NFA(start_status, end_status))

    def bar_nfa(self):
        nfa_last = self.nfa_stack.pop()
        nfa_first = self.nfa_stack.pop()
        start_status = Status()
        end_status = Status()
        end_status.accept = True
        start_status.epsilon.append(nfa_first.start)
        start_status.epsilon.append(nfa_last.start)
        nfa_first.end.epsilon.append(end_status)
        nfa_last.end.epsilon.append(end_status)
        nfa_first.end.accept = False
        nfa_last.end.accept = False
        nfa = NFA(start_status, end_status)
        self.nfa_stack.append(nfa)

    def concatenate_nfa(self):
        nfa_last = self.nfa_stack.pop()
        nfa_first = self.nfa_stack.pop()
        nfa_first.end.accept = False
        nfa_first.end.epsilon.append(nfa_last.start)
        nfa = NFA(nfa_first.start, nfa_last.end)
        self.nfa_stack.append(nfa)
