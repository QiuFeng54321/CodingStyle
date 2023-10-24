# Code generation to CAIE Assembly

from opcodes import Instruction, OpCode

class CodeGenerator:
    def __init__(self, ir_instructions: list[Instruction]) -> None:
        self.ir_instructions = ir_instructions
        self.instructions = []
        self.current_instruction_address = 512
        self.constant_address = {0: 0}
        self.current_constant_address = 1
        
    def add_instruction(self, instruction: str) -> int:
        self.instructions.append(f"{self.current_instruction_address:03} {instruction}")
        self.current_instruction_address += 1
        return self.current_instruction_address - 1
    def add_constant(self, value: int) -> int:
        if value not in self.constant_address.keys():
            self.constant_address[value] = self.current_constant_address
            self.instructions.insert(0, f"{self.current_constant_address:03} {value}")
            self.current_constant_address += 1
        return self.constant_address[value]
    def generate_load(self, address: int):
        self.add_instruction(f"LDD {address}")
    def generate_store(self, address: int):
        self.add_instruction(f"STO {address}")

    def generate(self):
        for instruction in self.ir_instructions:
            match instruction.opcode:
                case OpCode.Store:
                    self.generate_load(instruction.operand1)
                    self.generate_store(instruction.store)
                case OpCode.StoreImmediate:
                    addr = self.add_constant(instruction.operand1)
                    self.generate_load(addr)
                    self.generate_store(instruction.store)
                case OpCode.Input:
                    self.add_instruction("IN")
                    self.generate_store(instruction.store)
                case OpCode.Output:
                    self.generate_load(instruction.operand1)
                    self.add_instruction("OUT")
                case OpCode.Add | OpCode.Subtract | OpCode.Multiply | OpCode.Divide:
                    self.generate_load(instruction.operand1)
                    self.add_instruction(f"{str(instruction.opcode.name)[:3].upper()} {instruction.operand2}")
                    self.generate_store(instruction.store)
        self.add_instruction("END")