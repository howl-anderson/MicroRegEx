from MicroRegEx.PatternSyntaxError import PatternSyntaxError
from MicroRegEx.Token import Token
from MicroRegEx.Token import (
    ASTERISK,
    QUESTION,
    PLUS,
    BAR,
    OPEN_PARENTHESIS,
    CLOSE_PARENTHESIS,
    CHARACTER,
)


class Lexer(object):
    def __init__(self, pattern):
        self.pattern = pattern
        self.tokens = []
        self.token_index = -1

    def analyse(self):
        index = 0
        while index < len(self.pattern):
            char_ = self.pattern[index]

            if char_ == "*":
                self.tokens.append(Token(ASTERISK))
            elif char_ == "?":
                self.tokens.append(Token(QUESTION))
            elif char_ == "+":
                self.tokens.append(Token(PLUS))
            elif char_ == "|":
                self.tokens.append(Token(BAR))
            elif char_ == "(":
                self.tokens.append(Token(OPEN_PARENTHESIS))
            elif char_ == ")":
                self.tokens.append(Token(CLOSE_PARENTHESIS))
            elif char_ == "\\":
                index += 1
                char_ = self.pattern[index]
                if char_ == "*":
                    self.tokens.append(Token(CHARACTER, "*"))
                elif char_ == "?":
                    self.tokens.append(Token(CHARACTER, "?"))
                elif char_ == "+":
                    self.tokens.append(Token(CHARACTER, "+"))
                elif char_ == "|":
                    self.tokens.append(Token(CHARACTER, "|"))
                elif char_ == "(":
                    self.tokens.append(Token(CHARACTER, "("))
                elif char_ == ")":
                    self.tokens.append(Token(CHARACTER, ")"))
                elif char_ == "\\":
                    self.tokens.append(Token(CHARACTER, "\\"))
                else:
                    raise PatternSyntaxError("\\" + char_ + " is not unrecognizable.")
            else:
                self.tokens.append(Token(CHARACTER, char_))
            index += 1

    def get_next_token(self):
        if self.token_index == len(self.tokens) - 1:
            return None
        else:
            self.token_index += 1
            return self.tokens[self.token_index]

    def get_tokens(self):
        return self.tokens
