from src.MicroRegEx.Status import Status


class NFA:
    def __init__(self, start: Status, end: Status):
        self.start = start
        self.end = end
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
                new_status.add(next_status)
        self.current_status = new_status