import AST
from tokens import TokenType, Token
from opcodes import Instruction, OpCode


class Emit:
    def __init__(self) -> None:
        self.variable_address: dict[str, int] = {}
        # We reserve address 0 to always store 0
        self.next_available_address = 1
        self.instructions: list[Instruction] = []
        self.constant_address: dict[int, int] = {0: 0}

    def get_or_declare(self, name: str):
        if name not in self.variable_address.keys():
            self.variable_address[name] = self.next_available_address
            self.next_available_address += 1
        return self.variable_address[name]

    def temporary_name(self):
        return str(self.next_available_address)

    def get_or_declare_constant(self, value: int):
        if value not in self.constant_address.keys():
            self.constant_address[value] = self.next_available_address
            self.next_available_address += 1
            self.instructions.append(Instruction(OpCode.StoreImmediate, value, 0, self.constant_address[value]))
        return self.constant_address[value]

    def emit_program(self, program: AST.Program):
        for statement in program.statements:
            match statement:
                case AST.AssignmentStatement():
                    self.emit_assignment(statement)
                case AST.InputStatement():
                    self.emit_input(statement)
                case AST.OutputStatement():
                    self.emit_output(statement)

    def emit_assignment(self, statement: AST.AssignmentStatement):
        self.instructions.append(
            Instruction(
                OpCode.Store,
                self.emit_expression(statement.expression),
                0,
                self.get_or_declare(statement.variable.content),
            )
        )

    def emit_input(self, statement: AST.InputStatement):
        self.instructions.append(
            Instruction(
                OpCode.Input,
                0,
                0,
                self.get_or_declare(statement.variable.content),
            )
        )

    def emit_output(self, statement: AST.InputStatement):
        self.instructions.append(
            Instruction(
                OpCode.Output,
                self.get_or_declare(statement.variable.content),
                0,
                0,
            )
        )

    def emit_expression(self, expression: AST.Expression):
        match expression:
            case AST.Integer(token):
                return self.get_or_declare_constant(int(token.content))
            case AST.Identifier(token):
                return self.get_or_declare(token.content)
            case AST.BinaryOperation(left, op, right):
                left_address = self.emit_expression(left)
                right_address = self.emit_expression(right)
                opcode = None
                match op:
                    case TokenType.Add:
                        opcode = OpCode.Add
                    case TokenType.Subtract:
                        opcode = OpCode.Subtract
                    case TokenType.Multiply:
                        opcode = OpCode.Multiply
                    case TokenType.Divide:
                        opcode = OpCode.Divide
                    case _:
                        raise Exception("Unknown binary operation")
                store = self.get_or_declare(self.temporary_name())
                self.instructions.append(
                    Instruction(opcode, left_address, right_address, store)
                )
                return store
