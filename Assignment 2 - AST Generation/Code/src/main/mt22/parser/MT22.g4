grammar MT22;

@lexer::header {
# StudentID: 2011672 - Dương Nguyễn Nguyên Nghĩa
from lexererr import *
}

options {
	language = Python3;
}

program: (decls |) EOF;

/*==================Parser==================*/
/*------------------Types-------------------*/
int_list: INTLIT COMMA int_list | INTLIT;
type_func: BOOLEAN | INTEGER | FLOAT | STRING | VOID | AUTO;
type_vardecl_no_expr:
	BOOLEAN
	| INTEGER
	| FLOAT
	| STRING
	| ARRAY LS int_list RS OF (
		INTEGER
		| FLOAT
		| BOOLEAN
		| STRING
	)
	| AUTO;
type_vardecl_with_expr:
	BOOLEAN
	| INTEGER
	| FLOAT
	| STRING
	| AUTO;
/*----------------Declarations--------------*/
decls: vardecl decls | funcdecl decls | vardecl | funcdecl;
idlist: ID COMMA idlist | ID;
// Variable declarations
array_expression_list1:
	LC array_expression1 RC COMMA array_expression_list1
	| LC array_expression1 RC;
array_expression1:
	array_expression1 COMMA array_expression1
	| LC array_expression1 RC
	| expression_list;
array_expression_list2:
	LC array_expression2 RC COMMA array_expression_list2
	| EMPTY_BODY COMMA array_expression_list2
	| LC array_expression2 RC
	| EMPTY_BODY;
array_expression2:
	array_expression2 COMMA array_expression2
	| LC array_expression2 RC
	| EMPTY_BODY
	| LC RC
	| expression_list;
arraydecl_with_expr:
	idlist COLON ARRAY LS (int_list |) RS OF (
		INTEGER
		| FLOAT
		| BOOLEAN
		| STRING
	) ASSIGN array_expression_list1 SEMI;
arraydecl_no_expr:
	idlist COLON ARRAY LS (int_list) RS OF (
		INTEGER
		| FLOAT
		| BOOLEAN
		| STRING
	) ASSIGN array_expression_list2 SEMI;
vardecl_with_expr:
	idlist COLON type_vardecl_with_expr ASSIGN expression_list SEMI; //help_vardecl_with_expr SEMI;
// help_vardecl_with_expr: ID COMMA help_vardecl_with_expr COMMA expression | ID COLON type_vardecl_with_expr ASSIGN expression;
vardecl_no_expr: idlist COLON type_vardecl_no_expr SEMI;
vardecl:
	vardecl_with_expr
	| vardecl_no_expr
	| arraydecl_with_expr
	| arraydecl_no_expr;
// Function declarations
param_list: paramdecl COMMA param_list | paramdecl;
paramdecl: (INHERIT |) (OUT |) ID COLON type_vardecl_no_expr;
inherit: INHERIT ID;
funcdecl:
	(ID | MAIN) COLON FUNCTION type_func LP (param_list |) RP (
		inherit
		|
	) block_statement;
//--------------------------------------------
/*-----------------Expressions--------------*/
expression_list: expression COMMA expression_list | expression;
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
index: index LS expression RS | term;
// Term
term:
	BOOLLIT
	| INTLIT
	| FLOATLIT
	| STRINGLIT
	| ID
	| function
	| LP expression RP;
// Function
function: (ID LP (expression_list |) RP)|special_function;
//--------------------------------------------
/*----------------Statements----------------*/
statements: statement statements | statement;
statement:
	assign SEMI
	| if_
	| for_
	| while_
	| do_while
	| break_
	| continue_
	| return_
	| block_statement
	| call;

// Assign
assign: (ID | index) ASSIGN expression;
// If
if_:
	IF LP expression RP (statement | SEMI) (
		(ELSE (statement | SEMI))
		|
	);
// For
for_:
	FOR LP assign COMMA expression COMMA expression RP (
		statement
		| SEMI
	);
// While
while_: WHILE LP expression RP (statement | SEMI);
// Do-while
do_while: DO block_statement WHILE LP expression RP SEMI;
// Break
break_: BREAK SEMI;
// Continue
continue_: CONTINUE SEMI;
// Return
return_: RETURN (expression |) SEMI;
// Call
call: ((ID LP (expression_list |) RP) | special_function) SEMI;
// Block
mixed: statement mixed | vardecl mixed | statement | vardecl;
block_statement: EMPTY_BODY | (LC (mixed |) RC);
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
read_int: READINT LP RP;
print_int: PRINTINT LP expression RP;
read_float: READFLOAT LP RP;
write_float: WRITEFLOAT LP expression RP;
read_bool: READBOOL LP RP;
print_bool: PRINTBOOL LP expression RP;
read_string: READSTRING LP RP;
print_string: PRINTSTRING LP expression RP;
super_: SUPER LP expression_list RP;
prevent_default: PREVENTDEFAULT LP RP;
//--------------------------------------------

/*
 * ******************************************* *******************************************
 * ******************************************* *******************************************
 * ******************************************* *******************************************
 * ******************************************* *******************************************
 * ******************************************* *******************************************
 */

/*===================Lexer==================*/
EMPTY_BODY: '{}';
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
		(INTLIT '.'? [0-9]* ( ('e' | 'E') ('-' | '+')? [0-9]+)?)
		| ('.' [0-9]+ (('e' | 'E') ('-' | '+')? [0-9]+)?)
	) {self.text=self.text.replace("_","")};
BOOLLIT: TRUE | FALSE;
STRINGLIT:
	DQUOTES (~["\\\r\n] | '\\' [btnfr"'\\])* DQUOTES {self.text = self.text[1:-1]};

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
READINT: 'readInteger';
PRINTINT: 'printInteger';
READFLOAT: 'readFloat';
WRITEFLOAT: 'writeFloat';
READBOOL: 'readBoolean';
PRINTBOOL: 'printBoolean';
READSTRING: 'readString';
PRINTSTRING: 'printString';
SUPER: 'super';
PREVENTDEFAULT: 'preventDefault';
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