class Backtrack:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token_list = []
        self.token_list.append(lexer.get_next_token())

    def parse(self):
        pass

    def match(self, token):
        pass

    def expression(self):
        pass

    def pattern(self):
        pass
