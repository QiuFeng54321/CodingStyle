grammar ExprParser;
program: statement+;
statement:
	assignment_statement
	| input_statement
	| output_statement;
assignment_statement: ID '=' expression;
input_statement: '>' ID;
output_statement: '<' ID;

expression: expression ('+' | '-') term | term;
term: term ('*' | '/') atom | atom;
atom: ID | INTEGER | '(' expression ')';
ID: [a-z]+;
INTEGER: [0-9]+;
WS: [ \t\n]+ -> skip;