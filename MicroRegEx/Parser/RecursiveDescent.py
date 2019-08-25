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


class RecursiveDescent:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token_index = 0
        self.token = lexer.get_tokens()
        self.token_postfix = []

    def parse(self):
        if self.expression():
            return self.token_postfix
        return False

    def term(self, token):
        if self.token_index >= len(self.token):
            return False

        current_token = self.token[self.token_index]
        if current_token.token == token:
            self.token_index += 1
            if current_token.token == CHARACTER:
                self.token_postfix.append(current_token)
            return True

        return False

    def expression(self):
        return self.pattern()

    def pattern(self):
        return self.subpattern() and self.postpattern()

    def subpattern(self):
        return self.element() and self.other()

    def element(self):
        return self.atom() and self.meta_character()

    def atom(self):
        save_point = self.token_index
        if self.atom_1():
            return True
        else:
            self.token_index = save_point
            return self.atom_2()

    def atom_1(self):
        return (
            self.term(OPEN_PARENTHESIS)
            and self.pattern()
            and self.term(CLOSE_PARENTHESIS)
        )

    def atom_2(self):
        return self.term(CHARACTER)

    def other(self):
        save_point = self.token_index
        if self.subpattern():
            self.token_postfix.append(Token(CONCATENATE))
            return True
        else:
            self.token_index = save_point
            # do nothing for epsilon expression
            return True

    def meta_character(self):
        save_point = self.token_index
        if self.term(QUESTION):
            self.token_postfix.append(Token(QUESTION))
            return True
        else:
            self.token_index = save_point
            if self.term(PLUS):
                self.token_postfix.append(Token(PLUS))
                return True
            else:
                self.token_index = save_point
                if self.term(ASTERISK):
                    self.token_postfix.append(Token(ASTERISK))
                    return True
                else:
                    self.token_index = save_point
                    # do nothing for epsilon expression
                    return True

    def postpattern(self):
        save_point = self.token_index
        if self.postpattern_1():
            return True
        else:
            self.token_index = save_point
            # do nothing for epsilon expression
            return True

    def postpattern_1(self):
        result = self.term(BAR) and self.subpattern() and self.postpattern()
        if result:
            self.token_postfix.append(Token(BAR))
            return True
        return False
