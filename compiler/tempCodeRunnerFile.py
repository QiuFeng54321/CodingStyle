ser(lexer.tokens())
ast = parser.program()
print(ast)
emit = Emit()