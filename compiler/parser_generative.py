"""
Version of Parser that uses Iterators instead of lists
Learn about 'yield' before looking at this
"""

from typing import Iterator
from lexer import Lexer
from tokens import Token, TokenType
import AST

class Parser:
    def __init__(self, tokens: Iterator[Token]) -> None:
        self.tokens = tokens
        self.peeked_token = None
        self.peeked = False
    def peek(self):
        if self.peeked:
            return self.peeked_token
        self.peeked_token = self.tokens.__next__()
        self.peeked = True
        return self.peeked_token
    def consume(self):
        consumed = self.peek()
        if consumed.token_type != TokenType.Eof:
            self.peeked = False
        return consumed
    def match(self, token_type: TokenType) -> Token:
        if self.peek().token_type != token_type:
            raise Exception(f"Unmatched token: {self.peek()}, expected {token_type}")
        return self.consume()
    def program(self):
        statements = []
        while True:
            peek_token = self.peek()
            match peek_token.token_type:
                case TokenType.Identifier:
                    statements.append(self.assignment_statement())
                case TokenType.Output:
                    statements.append(self.output_statement())
                case TokenType.Input:
                    statements.append(self.input_statement())
                case TokenType.Eof:
                    return AST.Program(statements)
    def assignment_statement(self):
        id = self.match(TokenType.Identifier)
        self.match(TokenType.Assign)
        expr = self.expression()
        return AST.AssignmentStatement(id, expr)
    def input_statement(self):
        self.match(TokenType.Input)
        id = self.match(TokenType.Identifier)
        return AST.InputStatement(id)
    def output_statement(self):
        self.match(TokenType.Output)
        id = self.match(TokenType.Identifier)
        return AST.OutputStatement(id)
    def expression(self):
        """
        expression: term (('+' | '-') term)*;
        """
        base = self.term()
        while True:
            peek = self.peek()
            match peek.token_type:
                case TokenType.Add | TokenType.Subtract:
                    self.consume()
                    right = self.term()
                    base = AST.BinaryOperation(base, peek.token_type, right)
                case _:
                    return base
        
    def term(self):
        """
        term: atom (('*' | '/') atom)*;
        """
        base = self.atom()
        while True:
            peek = self.peek()
            match peek.token_type:
                case TokenType.Multiply | TokenType.Divide:
                    self.consume()
                    right = self.atom()
                    base = AST.BinaryOperation(base, peek.token_type, right)
                case _:
                    return base
    def atom(self):
        """
        atom: ID | INTEGER | '(' expression ')';
        """
        peek = self.peek()
        base = None
        if peek.token_type == TokenType.OpenParenthesis:
            self.match(TokenType.OpenParenthesis)
            base = self.expression()
            self.match(TokenType.CloseParenthesis)
        elif peek.token_type == TokenType.Identifier:
            base = AST.Identifier(self.match(TokenType.Identifier))
        elif peek.token_type == TokenType.Integer:
            base = AST.Integer(self.match(TokenType.Integer))
        return base
    
if __name__ == "__main__":
    from dataclasses import asdict
    import json
    lexer = Lexer(""">a
>b
>c
d = 2 * a * (b + c * a)
<d
""")
    parser = Parser(lexer.tokens())
    ast = parser.program()
    print(ast)
    print(json.dumps(asdict(ast)))
    ast.flow()