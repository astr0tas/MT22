grammar MT22;

@lexer::header {
# StudentID: 2011672 - Dương Nguyễn Nguyên Nghĩa
from lexererr import *
}

options {
	language = Python3;
}

program: decls* EOF;

/*==================Parser==================*/
/*------------------Types-------------------*/
type_func:
	BOOLEAN
	| INTEGER
	| FLOAT
	| STRING
	| ARRAY LS (INTLIT COMMA)* INTLIT RS OF (
		INTEGER
		| FLOAT
		| BOOLEAN
		| STRING
	)
	| VOID
	| AUTO;
type_vardecl_noExpr:
	BOOLEAN
	| INTEGER
	| FLOAT
	| STRING
	| ARRAY LS ((INTLIT COMMA)* INTLIT)? RS OF (
		INTEGER
		| FLOAT
		| BOOLEAN
		| STRING
	)
	| AUTO;
type_vardecl_withExpr:
	BOOLEAN
	| INTEGER
	| FLOAT
	| STRING
	| AUTO;
/*----------------Declarations--------------*/
decls: vardecls | funcdecls;
idlist: (ID COMMA)* ID;
// Variable declarations
arraydeclWithExpr:
	ID COLON ARRAY LS ((INTLIT COMMA)* INTLIT)? RS OF (
		INTEGER
		| FLOAT
		| BOOLEAN
		| STRING
	) ASSIGN ARRAYLIT SEMI;
vardeclWithExpr: helpVardeclWithExpr SEMI;
helpVardeclWithExpr:
	ID COMMA helpVardeclWithExpr COMMA expression
	| ID COLON type_vardecl_withExpr ASSIGN expression;
vardeclNoExpr: idlist COLON type_vardecl_noExpr SEMI;
vardecls:
	vardeclWithExpr+
	| vardeclNoExpr+
	| arraydeclWithExpr+;
// Function declarations
paramdecl: INHERIT? OUT? ID COLON type_vardecl_noExpr;
funcdecl:
	(ID | MAIN) COLON FUNCTION type_func LP (
		(paramdecl COMMA)* paramdecl
	)? RP (INHERIT ID)? block_statement;
funcdecls: funcdecl+;
//--------------------------------------------
/*-----------------Expressions--------------*/
expression_list: (expression COMMA)* expression;
expression: string;
// String
string: relational STRING_CONCAT relational | relational;
// Relational
relational:
	logical1 (
		EQ
		| NOT_EQ
		| LESS
		| LESS_OR_EQ
		| GREATER
		| GREATER_OR_EQ
	) logical1
	| logical1;
// AND, OR
logical1: logical1 (AND | OR) arithmetic1 | arithmetic1;
// ADD, SUB
arithmetic1: arithmetic1 (ADD | SUB) arithmetic2 | arithmetic2;
// MUL,DIV,MOD
arithmetic2: arithmetic2 (MUL | DIV | MOD) logical2 | logical2;
// NOT
logical2: NOT logical2 | sign;
// Sign
sign: SUB sign | index;
// Index
index: index LS expression_list RS | term;
// Term
term:
	BOOLLIT
	| INTLIT
	| FLOATLIT
	| STRINGLIT
	| ID
	| special_function
	| function
	| LP expression RP;
// Function
function: ID LP (expression_list)? RP;
//--------------------------------------------
/*----------------Statements----------------*/
statement:
	assign
	| if_
	| for_
	| while_
	| do_while
	| break_
	| continue_
	| return_
	| call
	| block_statement
	| special_function SEMI;
// Assign
assign: (ID | index) ASSIGN expression SEMI;
// If
if_:
	IF LP expression RP (
		LC statement* RC
		| statement
		| SEMI
		| '{}'
	) (ELSE ( SEMI | LC statement* RC | statement | '{}'))?;
// For
for_:
	FOR LP ID ASSIGN expression COMMA expression COMMA expression RP (
		SEMI
		| LC statement* RC
		| '{}'
		| statement
	);
// While
while_:
	WHILE LP expression RP (
		SEMI
		| LC statement* RC
		| '{}'
		| statement
	);
// Do-while
do_while: DO block_statement WHILE LP expression RP SEMI;
// Break
break_: BREAK SEMI;
// Continue
continue_: CONTINUE SEMI;
// Return
return_: RETURN (expression)? SEMI;
// Call
call: function SEMI;
// Block
block_statement: (LC (statement | vardecls)* RC) | '{}';
//--------------------------------------------
/*---------------Special functions----------*/
special_function:
	read_int
	| read_bool
	| read_float
	| read_string
	| print_int
	| print_bool
	| print_string
	| write_float
	| super_
	| prevent_default;
read_int: 'readInteger' LP RP;
print_int: 'printInteger' LP expression RP;
read_float: 'readFloat' LP RP;
write_float: 'writeFloat' LP expression RP;
read_bool: 'readBooolean' LP RP;
print_bool: 'printBoolean' LP expression RP;
read_string: 'readString' LP RP;
print_string: 'printString' LP expression RP;
super_: 'super' LP expression_list RP;
prevent_default: 'preventDefault' LP RP;
//--------------------------------------------

/*
 * *******************************************
 */

/*===================Lexer==================*/
/*-------------------Comments---------------*/
LINECMT: '//' (~[\r\n])* -> skip;
MULTLINECMT: '/*' .*? '*/' -> skip;
//--------------------------------------------
/*-------------------Literals---------------*/
INTLIT:
	'0'
	| [1-9][0-9]* ('_' [0-9]+)* {self.text=self.text.replace("_","")};
FLOATLIT:
	(
		(INTLIT '.'? [0-9]* (('e' | 'E') ('-' | '+')? [0-9]+)?)
		| ('.' [0-9]+ (('e' | 'E') ('-' | '+')? [0-9]+)?)
	) {self.text=self.text.replace("_","")};
BOOLLIT: TRUE | FALSE;
STRINGLIT:
	DQUOTES (~["\\\r\n] | '\\' [btnfr"'\\])* DQUOTES {self.text = self.text[1:-1]};

ARRAYLIT: LC ((EXPRESSION COMMA)* EXPRESSION) RC;
fragment EXPRESSION:
	INTLIT
	| FLOATLIT
	| BOOLLIT
	| STRINGLIT
	| ARRAYLIT
	| ID;

//--------------------------------------------
/*-------------------Key words--------------*/
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';
MAIN: 'main';
//--------------------------------------------
/*--------------------Operators-------------*/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
NOT_EQ: '!=';
LESS: '<';
LESS_OR_EQ: '<=';
GREATER: '>';
GREATER_OR_EQ: '>=';
STRING_CONCAT: '::';
//--------------------------------------------
/*---------------------Separators-----------*/
LP: '(';
RP: ')';
LS: '[';
RS: ']';
LC: '{';
RC: '}';
COMMA: ',';
PERIOD: '.';
SEMI: ';';
COLON: ':';
ASSIGN: '=';
//--------------------------------------------
/*-----------------Identifiers--------------*/
ID: [a-zA-Z_][a-zA-Z_0-9]*;
//--------------------------------------------
/*----------------Characters set------------*/
BACKSLASH: '\\';
DQUOTES: '"';
SQUOTE: '\'';
WS: [ \t\r\n\f\b]+ -> skip;
//--------------------------------------------
/*-----------------Error Tokens-------------*/
UNCLOSE_STRING:
	DQUOTES (~["\\\r\n] | '\\' [btnfr"'\\])* {self.text = self.text[1:]; raise UncloseString(self.text)
		};
ILLEGAL_ESCAPE:
	DQUOTES (~["\\\r\n])* [\r\n] {self.text = self.text[1:]; raise IllegalEscape(self.text)};
ERROR_CHAR: . {raise ErrorToken(self.text)};