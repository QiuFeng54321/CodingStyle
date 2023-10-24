from opcodes import Instruction, OpCode


class VM:
    def __init__(self) -> None:
        self.memory = [0] * 1024
    
    def execute_program(self, instructions: list[Instruction]):
        for instruction in instructions:
            self.execute(instruction)

    def execute(self, instruction: Instruction):
        match instruction.opcode:
            case OpCode.Input:
                self.memory[instruction.store] = int(input())
            case OpCode.Output:
                print(self.memory[instruction.operand1])
            case OpCode.Store:
                self.memory[instruction.store] = self.memory[instruction.operand1]
            case OpCode.StoreImmediate:
                self.memory[instruction.store] = instruction.operand1
            case OpCode.Add:
                self.memory[instruction.store] = (
                    self.memory[instruction.operand1]
                    + self.memory[instruction.operand2]
                )
            case OpCode.Subtract:
                self.memory[instruction.store] = (
                    self.memory[instruction.operand1]
                    - self.memory[instruction.operand2]
                )
            case OpCode.Multiply:
                self.memory[instruction.store] = (
                    self.memory[instruction.operand1]
                    * self.memory[instruction.operand2]
                )
            case OpCode.Divide:
                self.memory[instruction.store] = (
                    self.memory[instruction.operand1]
                    / self.memory[instruction.operand2]
                )
