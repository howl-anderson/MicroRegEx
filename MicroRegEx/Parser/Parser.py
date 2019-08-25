from MicroRegEx.PatternSyntaxError import PatternSyntaxError
from MicroRegEx.Token import Token
from MicroRegEx.Token import (
    CONCATENATE,
    ASTERISK,
    QUESTION,
    PLUS,
    BAR,
    OPEN_PARENTHESIS,
    CLOSE_PARENTHESIS,
    CHARACTER,
)


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = lexer.get_next_token()
        self.postfix = []

    def parse(self):
        self.expr()
        return self.postfix

    def expr(self):
        self.state()
        self.bar()

    def bar(self):
        if self.token is not None and self.token.token is BAR:
            self._match(BAR)
            self.state()
            self.postfix.append(Token(BAR))
            self.bar()
        else:
            pass  # epsilon

    def state(self):
        self.term()
        self.concatenate()

    def concatenate(self):
        if self.token is not None:
            if self.token.token in (CHARACTER, OPEN_PARENTHESIS):
                self.term()
                self.postfix.append(Token(CONCATENATE))
                self.concatenate()
            else:
                return  # epsilon
        else:
            return  # epsilon

    def term(self):
        self.item()
        self.rest()

    def item(self):
        if self.token.token == OPEN_PARENTHESIS:
            self._match(OPEN_PARENTHESIS)
            self.expr()
            self._match(CLOSE_PARENTHESIS)
        elif self.token.token == CHARACTER:
            self.element()
        else:
            pass  # epsilon

    def rest(self):
        if self.token is not None:
            if self.token.token in (PLUS, ASTERISK, QUESTION):
                old_token = self.token
                self._match(self.token.token)
                self.postfix.append(old_token)
            else:
                pass  # epsilon
        else:
            pass  # epsilon

    def element(self):
        old_token = self.token
        self._match(CHARACTER)
        self.postfix.append(old_token)

    def _match(self, lookahead):
        if lookahead != self.token.token:
            msg = "%s don't match %s" % (self.token.token, lookahead)
            raise PatternSyntaxError(msg)

        self.token = self.lexer.get_next_token()
