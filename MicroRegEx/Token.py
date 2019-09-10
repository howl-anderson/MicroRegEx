class Token:
    def __init__(self, token, value=None):
        self.token = token
        self.value = value

    def __str__(self):
        return "{}: {}".format(self.token, self.value)

    def __repr__(self):
        return "{}({}, value={})".format(self.__class__.__name__, self.token, self.value)


CONCATENATE = "concatenate"
ASTERISK = "ASTERISK"
QUESTION = "QUESTION"
PLUS = "PLUS"
BAR = "BAR"
OPEN_PARENTHESIS = "OPEN_PARENTHESIS"
CLOSE_PARENTHESIS = "CLOSE_PARENTHESIS"
CHARACTER = "CHARACTER"
