from graphviz import Digraph

from MicroRegEx.Automaton.Status import Status


class NFA:
    def __init__(self, start: Status, end: Status):
        self.start = start
        self.end = end
        self.current_status = set()
        self.epsilon_status = set()

    def reset(self):
        # reset status to very beginning
        self.current_status = set()
        self.epsilon_status = set()

    def match(self, string_):
        self.current_status = {self.start}
        self.epsilon()
        for char_ in string_:
            self.translate(char_)
            self.epsilon()

        for status in self.current_status:
            if status.accept:
                return True
        return False

    def is_accepted(self):
        for status in self.current_status:
            if status.accept:
                return True
        return False

    def match_step_by_step(self, string_):
        self.current_status = {self.start}
        self.epsilon()
        for char_ in string_:
            self.translate(char_)
            self.epsilon()

            yield None

        return self.is_accepted()

    def epsilon(self):
        self.epsilon_status = set()
        for status in self.current_status:
            self._epsilon(status.epsilon)
        self.current_status.update(self.epsilon_status)

    def _epsilon(self, status_list):
        for status in status_list:
            if status in self.current_status or status in self.epsilon_status:
                continue
            else:
                self.epsilon_status.add(status)
                epsilon_status_list = status.epsilon
                self._epsilon(epsilon_status_list)

    def translate(self, char_):
        new_status = set()
        for status in self.current_status:
            if char_ in status.translation:
                next_status = status.translation[char_]
                new_status.update(next_status)
        self.current_status = new_status

    def get_graph(self, current_status_list=None):
        def _shape(status_):
            return "doublecircle" if status_.accept else "circle"

        def _fillcolor(status_):
            return "red" if current_status_list and status_ in current_status_list else "black"

        graph = Digraph("finite_state_machine")
        graph.body.extend(["rankdir=LR", 'size="8,5"'])

        graph.node("", label="", shape="None", color="white")

        graph.node(self.start.name, shape=_shape(self.start))
        graph.edge("", self.start.name, label="")

        status_set = [self.start]
        plot_set = []
        work_list = [self.start]

        while len(work_list):
            current_status = work_list.pop()

            epsilon_status = [("ϵ", i) for i in current_status.epsilon]
            translation_status = []
            for k, v in current_status.translation.items():
                translation = zip([k] * len(v), v)
                translation_status.extend(translation)

            for symbol, status in epsilon_status + translation_status:
                if status not in status_set:
                    work_list.append(status)
                    status_set.append(status)

                plot_item = (current_status, status, symbol)
                if plot_item not in plot_set:
                    graph.node(status.name, shape=_shape(status), fontcolor=_fillcolor(status), color=_fillcolor(status))
                    graph.edge(current_status.name, status.name, label=symbol)

                    plot_set.append(plot_item)

        return graph

    def plot(self, file_name=None):
        def _shape(status_):
            return "doublecircle" if status_.accept else "circle"

        graph = Digraph("finite_state_machine", filename=file_name or "nfa")
        graph.body.extend(["rankdir=LR", 'size="8,5"'])

        graph.node("", label="", shape="None", color="white")

        graph.node(self.start.name, shape=_shape(self.start))
        graph.edge("", self.start.name, label="")

        status_set = [self.start]
        plot_set = []
        work_list = [self.start]

        while len(work_list):
            current_status = work_list.pop()

            epsilon_status = [("ϵ", i) for i in current_status.epsilon]
            translation_status = []
            for k, v in current_status.translation.items():
                translation = zip([k] * len(v), v)
                translation_status.extend(translation)

            for symbol, status in epsilon_status + translation_status:
                if status not in status_set:
                    work_list.append(status)
                    status_set.append(status)

                plot_item = (current_status, status, symbol)
                if plot_item not in plot_set:
                    graph.node(status.name, shape=_shape(status))
                    graph.edge(current_status.name, status.name, label=symbol)

                    plot_set.append(plot_item)

        graph.view()

        return graph
