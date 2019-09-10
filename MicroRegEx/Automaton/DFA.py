from graphviz import Digraph

from MicroRegEx.Automaton.Status import Status
from MicroRegEx.Automaton.StatusSet import StatusSet


class DFA:
    def __init__(self, start_status=None):
        self.start = start_status
        self.table = {}

    def match(self, string_):
        current_status = self.start
        for symbol in string_:
            if current_status in self.table:
                if symbol in self.table[current_status]:
                    current_status = self.table[current_status][symbol]
                else:
                    return False
            else:
                # this status gos no where
                return False

        return current_status.accept

    def translate(self, status_from, input_char, status_to):
        status_translation = {input_char: status_to}
        if status_from not in self.table:
            self.table[status_from] = status_translation
        else:
            self.table[status_from].update(status_translation)

    def simplify(self):
        # reset status counter
        Status.count = 0

        new_start = Status()
        new_start.accept = self.start.accept

        simplified_dfa = DFA(new_start)

        status_mapping = {self.start: new_start}
        work_list = [self.start]

        while work_list:
            status = work_list.pop()
            new_status = status_mapping[status]

            if status not in self.table:
                # this status gos no where
                continue

            for k, v in self.table[status].items():
                if v not in status_mapping:
                    sub_status = Status()
                    sub_status.accept = v.accept

                    status_mapping.update({v: sub_status})
                    work_list.append(v)
                else:
                    sub_status = status_mapping[v]

                simplified_dfa.translate(new_status, k, sub_status)

        return simplified_dfa

    def get_graph(self):
        def _shape(status_):
            if isinstance(status_, StatusSet):
                accept = any([i.accept for i in status_])
            else:
                accept = status_.accept

            return "doublecircle" if accept else "circle"

        graph = Digraph("finite_state_machine")
        graph.body.extend(["rankdir=LR", 'size="8,5"'])

        graph.node("", label="", shape="None", color="white")

        graph.node(self.start.name, shape=_shape(self.start))
        graph.edge("", self.start.name, label="")

        relation_list = []
        status_list = [self.start]
        work_list = [self.start]

        while len(work_list):
            current_status = work_list.pop()
            if current_status not in self.table:
                # this status gos no where
                continue

            for symbol, status in self.table[current_status].items():
                if status not in status_list:
                    status_list.append(status)
                    work_list.append(status)

                relation_item = (current_status, status, symbol)
                if relation_item not in relation_list:
                    graph.node(status.name, shape=_shape(status))
                    graph.edge(current_status.name, status.name, label=symbol)
                    relation_list.append(relation_item)

        return graph

    def plot(self, file_name=None):
        def _shape(status_):
            if isinstance(status_, StatusSet):
                accept = any([i.accept for i in status_])
            else:
                accept = status_.accept

            return "doublecircle" if accept else "circle"

        graph = Digraph("finite_state_machine", filename=file_name or "dfa")
        graph.body.extend(["rankdir=LR", 'size="8,5"'])

        graph.node("", label="", shape="None", color="white")

        graph.node(self.start.name, shape=_shape(self.start))
        graph.edge("", self.start.name, label="")

        relation_list = []
        status_list = [self.start]
        work_list = [self.start]

        while len(work_list):
            current_status = work_list.pop()
            if current_status not in self.table:
                # this status gos no where
                continue

            for symbol, status in self.table[current_status].items():
                if status not in status_list:
                    status_list.append(status)
                    work_list.append(status)

                relation_item = (current_status, status, symbol)
                if relation_item not in relation_list:
                    graph.node(status.name, shape=_shape(status))
                    graph.edge(current_status.name, status.name, label=symbol)
                    relation_list.append(relation_item)

        graph.view()

        return graph
