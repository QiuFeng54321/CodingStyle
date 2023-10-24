from lexer import Lexer
from parser import Parser
from emit import Emit
from vm import VM
from codegen import CodeGenerator
import sys

program_source = ""
if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        program_source = f.read()
else:
    program_source = input("Program: ")
lexer = Lexer(program_source)
parser = Parser(lexer.tokens())
ast = parser.program()
print(ast)
emit = Emit()
emit.emit_program(ast)
print("\n\nIR Representation:")
print("\n".join(map(str, emit.instructions)))

print("\n\nAssembly:")
codegen = CodeGenerator(emit.instructions)
codegen.generate()
print("\n".join(codegen.instructions))
print("Starting execution")
vm = VM()
vm.execute_program(emit.instructions)
