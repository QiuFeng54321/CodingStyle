from tokens import Token, TokenType


class Lexer:
    def __init__(self, content: str) -> None:
        self.content = content
        self.current_peek_index = 0 # The index to the peeking character

    def peek(self) -> str:
        """Peeking returns the character ahead, but does not consume

        :return: the character ahead
        :rtype: str
        """
        if self.current_peek_index >= len(self.content):
            return None
        return self.content[self.current_peek_index]

    def consume(self) -> str:
        consumed_char = self.peek()
        self.current_peek_index += 1
        return consumed_char

    def tokens(self):
        result = []
        while True:
            peek_char = self.peek()
            if peek_char == None:
                result.append(Token(TokenType.Eof, "$"))
                break
            if "0" <= peek_char <= "9":
                content = self.consume()
                while self.peek() != None and "0" <= self.peek() <= "9":
                    content += self.consume()
                result.append(Token(TokenType.Integer, content))
            elif peek_char.isalpha():
                content = self.consume()
                while self.peek() != None and self.peek().isalnum():
                    content += self.consume()
                result.append(Token(TokenType.Identifier, content))
            elif peek_char == "+":
                result.append(Token(TokenType.Add, self.consume()))
            elif peek_char == "-":
                result.append(Token(TokenType.Subtract, self.consume()))
            elif peek_char == "*":
                result.append(Token(TokenType.Multiply, self.consume()))
            elif peek_char == "/":
                result.append(Token(TokenType.Divide, self.consume()))
            elif peek_char == "(":
                result.append(Token(TokenType.OpenParenthesis, self.consume()))
            elif peek_char == ")":
                result.append(Token(TokenType.CloseParenthesis, self.consume()))
            elif peek_char == "=":
                result.append(Token(TokenType.Assign, self.consume()))
            elif peek_char == "<":
                result.append(Token(TokenType.Output, self.consume()))
            elif peek_char == ">":
                result.append(Token(TokenType.Input, self.consume()))
            elif peek_char.isspace():
                self.consume() # Ignore space
                continue
            else:
                result.append(Token(TokenType.Unknown, self.consume()))
        return result


if __name__ == "__main__":
    for token in Lexer(">in\nout = (2 + in) * 30\n<out").tokens():
        print(token)
