
from dataclasses import dataclass
from enum import IntEnum, IntFlag


class OpCode(IntEnum):
    Input = 0
    Output = 1
    Add = 2
    Subtract = 3
    Multiply = 4
    Divide = 5
    Store = 6
    StoreImmediate = 7

@dataclass
class Instruction:
    opcode: OpCode
    operand1: int
    operand2: int
    store: int
    def __repr__(self) -> str:
        return f"{self.opcode.name:<8} {self.operand1:<2} {self.operand2:<2} {self.store:<2}"