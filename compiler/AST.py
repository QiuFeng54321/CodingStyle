from dataclasses import dataclass
from tokens import Token, TokenType

"""
Ignore anything with a 'flow' in it!
Those are supposed to help me build flowcharts, and has nothing to do with ASTs.
"""

current_flow_i = -1
def get_new_flow_name(annotate: str):
    global current_flow_i
    current_flow_i += 1
    return f"n{current_flow_i}[{annotate}]"
def get_new_identifier_flow_name(name: str):
    id_name = get_new_flow_name('identifier')
    print(f"{id_name} --> {get_new_flow_name(name)}")
    return id_name

@dataclass
class AST:
    pass


@dataclass
class Statement(AST):
    pass


@dataclass
class Expression(AST):
    pass


@dataclass
class Program(AST):
    statements: list[Statement]
    def flow(self):
        name = get_new_flow_name("program")
        for stmt in self.statements:
            print(f"{name} --> {stmt.flow()}")
        return name

@dataclass
class AssignmentStatement(Statement):
    variable: Token
    expression: Expression
    def flow(self):
        name = get_new_flow_name("assignment_statement")
        print(f"{name} --> {get_new_identifier_flow_name(self.variable.content)}")
        print(f"{name} --> {get_new_flow_name('=')}")
        print(f"{name} --> {self.expression.flow()}")
        return name


@dataclass
class InputStatement(Statement):
    variable: Token
    def flow(self):
        name = get_new_flow_name("input_statement")
        print(f"{name} --> {get_new_flow_name('>')}")
        print(f"{name} --> {get_new_identifier_flow_name(self.variable.content)}")
        return name


@dataclass
class OutputStatement(Statement):
    variable: Token
    def flow(self):
        name = get_new_flow_name("output_statement")
        print(f"{name} --> {get_new_flow_name('<')}")
        print(f"{name} --> {get_new_identifier_flow_name(self.variable.content)}")
        return name

@dataclass
class Atom(Expression):
    pass

@dataclass
class Integer(Atom):
    integer: Token
    def flow(self):
        name = get_new_flow_name('integer')
        print(f"{name} --> {get_new_flow_name(self.integer.content)}")
        return name

@dataclass
class Identifier(Atom):
    identifier: Token
    def flow(self):
        return get_new_identifier_flow_name(self.identifier.content)

@dataclass
class BinaryOperation(Expression):
    left: Expression
    operation: TokenType
    right: Expression
    def flow(self):
        name = get_new_flow_name("binary")
        print(f"{name} --> {self.left.flow()}")
        print(f"{name} --> {get_new_flow_name(self.operation.name)}")
        print(f"{name} --> {self.right.flow()}")
        return name
