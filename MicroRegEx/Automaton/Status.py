class Status:
    count = 0

    def __init__(self, name=None):
        if name is None:
            name = str(self.count)
            self.__class__.count += 1

        self.name = name
        self.translation = {}
        self.epsilon = []
        self.accept = False
        super().__init__()

    def translate(self, symbol, status):
        if symbol in self.translation:
            self.translation[symbol].append(status)
        else:
            self.translation[symbol] = [status]

    def __str__(self):
        format_str = "<{} translation={} epsilon={} accept={}>"
        return format_str.format(
            str(self.name),
            repr(self.translation),
            repr(self.epsilon),
            repr(self.accept),
        )
