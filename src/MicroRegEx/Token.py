class Token:
    def __init__(self, token, value=None):
        self.token = token
        self.value = value

    def __str__(self):
        return "{}: {}".format(self.token, self.value)
