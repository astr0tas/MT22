import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2(self):
        input = """x, y, z: integer;"""
        expect = """Program([\n\tVarDecl(x, IntegerType)\n\tVarDecl(y, IntegerType)\n\tVarDecl(z, IntegerType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3(self):
        input = """main: function void (a:integer) {}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = """main: function void (a:integer,b:float) {}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test5(self):
        input = """main: function void () {x:integer;}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6(self):
        input = """main: function void () {x,y,z:integer;}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test7(self):
        input = """main: function void () {prevent_default();}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(prevent_default, )]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test8(self):
        input = """main: function void () {printInteger(4);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test9(self):
        input = """main: function void () {a=1+2;}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(2)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test10(self):
        input = """main: function void () {a=1+2;
            a=2*3;}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(2))), AssignStmt(Id(a), BinExpr(*, IntegerLit(2), IntegerLit(3)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test11(self):
        input = """"""
        expect = """Program([\n\t\n])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12(self):
        input = """main: function void () {a:array[10] of integer;}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([IntegerLit(10)], IntegerType))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test13(self):
        input = """foo: function integer () {return 0;}"""
        expect = """Program([\n\tFuncDecl(foo, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test14(self):
        input = """main: function integer () {if(true) {} else {} return 0;}"""
        expect = """Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([]), BlockStmt([])), ReturnStmt(IntegerLit(0))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15(self):
        input = """main: function integer () {for(i=0,i<10,i+1){} return 0;}"""
        expect = """Program([\n\tFuncDecl(main, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([])), ReturnStmt(IntegerLit(0))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test16(self):
        input = """main: function void () {a:array[10] of integer={1,2,3};}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([IntegerLit(10)], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        input = """main: function void () {a:array[] of integer={1,2,3};}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test18(self):
        input = """main: function void () {a:array[5] of integer={};}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([IntegerLit(5)], IntegerType), ArrayLit([]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        input = """main: function void () {a:array[5,5] of integer={{},{},{},{},{}};}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([IntegerLit(5), IntegerLit(5)], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([])]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        input = """main: function void () {a:array[10,10] of integer={{1,2,3},1,2,3,4,5,{}};}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([IntegerLit(10), IntegerLit(10)], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), ArrayLit([])]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([\n\tVarDecl(x, IntegerType, IntegerLit(1))\n\tVarDecl(y, IntegerType, IntegerLit(2))\n\tVarDecl(z, IntegerType, IntegerLit(3))\n\tVarDecl(a, FloatType)\n\tVarDecl(b, FloatType)\n])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test22(self):
        input = """a,b,c:array[3] of integer={1,2,3},{4,5,6},{7,8,9};"""
        expect = """Program([\n\tVarDecl(a, ArrayType([IntegerLit(3)], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))\n\tVarDecl(b, ArrayType([IntegerLit(3)], IntegerType), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]))\n\tVarDecl(c, ArrayType([IntegerLit(3)], IntegerType), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test23(self):
        input = """a,b,c:array[3] of integer={},{},{};"""
        expect = """Program([\n\tVarDecl(a, ArrayType([IntegerLit(3)], IntegerType), ArrayLit([]))\n\tVarDecl(b, ArrayType([IntegerLit(3)], IntegerType), ArrayLit([]))\n\tVarDecl(c, ArrayType([IntegerLit(3)], IntegerType), ArrayLit([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test24(self):
        input = """a,b,c:array[] of integer={1,2,3},{4,5,6},{7,8,9};"""
        expect = """Program([\n\tVarDecl(a, ArrayType([], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))\n\tVarDecl(b, ArrayType([], IntegerType), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]))\n\tVarDecl(c, ArrayType([], IntegerType), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test25(self):
        input = """a,b,c:array[5,5] of integer={{},{},{},{},{}},{{},{},{},{},{}},{{},{},{},{},{}};"""
        expect = """Program([\n\tVarDecl(a, ArrayType([IntegerLit(5), IntegerLit(5)], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([])]))\n\tVarDecl(b, ArrayType([IntegerLit(5), IntegerLit(5)], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([])]))\n\tVarDecl(c, ArrayType([IntegerLit(5), IntegerLit(5)], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([]), ArrayLit([])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        input = """a,b,c:array[] of integer={{1},{2},{3},{4},{5}},{{6},{7},{8},{9},{10}},{{11},{12},{13}};"""
        expect = """Program([\n\tVarDecl(a, ArrayType([], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(4)]), ArrayLit([IntegerLit(5)])]))\n\tVarDecl(b, ArrayType([], IntegerType), ArrayLit([ArrayLit([IntegerLit(6)]), ArrayLit([IntegerLit(7)]), ArrayLit([IntegerLit(8)]), ArrayLit([IntegerLit(9)]), ArrayLit([IntegerLit(10)])]))\n\tVarDecl(c, ArrayType([], IntegerType), ArrayLit([ArrayLit([IntegerLit(11)]), ArrayLit([IntegerLit(12)]), ArrayLit([IntegerLit(13)])]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test27(self):
        input = """main: function void () {a:array[5] of integer={1+1,2*3,5-1,4/2,9%5};}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([IntegerLit(5)], IntegerType), ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(*, IntegerLit(2), IntegerLit(3)), BinExpr(-, IntegerLit(5), IntegerLit(1)), BinExpr(/, IntegerLit(4), IntegerLit(2)), BinExpr(%, IntegerLit(9), IntegerLit(5))]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test28(self):
        input = """main: function void () {while(true);}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), None)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test29(self):
        input = """main: function void () {while(true){}}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test30(self):
        input = """main: function void () {for(i=0,true,i+1) break;}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BooleanLit(True), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test31(self):
        input = """main: function void () {x, y, z: integer; b,c:integer;}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType)]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test32(self):
        input = """main: function void () {x,y,z:integer=1,2,3;}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(y, IntegerType, IntegerLit(2)), VarDecl(z, IntegerType, IntegerLit(3))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        input = """main: function void () {a:integer=5+6-(123*10+(24-30));}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(5), IntegerLit(6)), BinExpr(+, BinExpr(*, IntegerLit(123), IntegerLit(10)), BinExpr(-, IntegerLit(24), IntegerLit(30)))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test34(self):
        input = """calculate_C: function float () {r:float=readFloat(); pi:float=3.14; C:float=2*r*pi; return C;}"""
        expect = """Program([\n\tFuncDecl(calculate_C, FloatType, [], None, BlockStmt([VarDecl(r, FloatType, FuncCall(readFloat, [])), VarDecl(pi, FloatType, FloatLit(3.14)), VarDecl(C, FloatType, BinExpr(*, BinExpr(*, IntegerLit(2), Id(r)), Id(pi))), ReturnStmt(Id(C))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test35(self):
        input = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a*b);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(readInteger, [])), VarDecl(b, IntegerType, FuncCall(readInteger, [])), CallStmt(printInteger, BinExpr(*, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test36(self):
        input = """main: function void () {printBoolean(1+1==2);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(1)), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test37(self):
        input = """main: function void () {printBoolean(!!false);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, UnExpr(!, UnExpr(!, BooleanLit(False))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test38(self):
        input = """uselessFunc:function string(){return "Zero";}"""
        expect = """Program([\n\tFuncDecl(uselessFunc, StringType, [], None, BlockStmt([ReturnStmt(StringLit(Zero))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test39(self):
        input = """main: function void () {writeFloat(-2.65e-3);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(writeFloat, UnExpr(-, FloatLit(0.00265)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test40(self):
        input = """main: function void () {writeFloat(2.e-7+3e-1);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(writeFloat, BinExpr(+, FloatLit(2e-07), FloatLit(0.3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test41(self):
        input = """main: function void () {n:float=readFloat(); writeFloat(n);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, FloatType, FuncCall(readFloat, [])), CallStmt(writeFloat, Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test42(self):
        input = """print: function void(str:string) {printString(str);}"""
        expect = """Program([
	FuncDecl(print, VoidType, [Param(str, StringType)], None, BlockStmt([CallStmt(printString, Id(str))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        input = """concatString: function string(str1:string,str2:string) {return str1::str2;}"""
        expect = """Program([\n\tFuncDecl(concatString, StringType, [Param(str1, StringType), Param(str2, StringType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(str1), Id(str2)))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test44(self):
        input = """main: function void() {str:string="abc"::("def"::("ghi"::"jkl"));}"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(str, StringType, BinExpr(::, StringLit(abc), BinExpr(::, StringLit(def), BinExpr(::, StringLit(ghi), StringLit(jkl)))))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test45(self):
        input = """fibonacci:function integer(n:integer){if(n==0) return 0; if(n==1) return 1; return fibonacci(n-1)+fibonacci(n-2);} main: function void() {n:integer=readInteger(); printInteger(fibonacci(n));}"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(0))), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1))), ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(2))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), CallStmt(printInteger, FuncCall(fibonacci, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test46(self):
        input = """foo:function void(inherit a:auto){}"""
        expect = """Program([\n\tFuncDecl(foo, VoidType, [InheritParam(a, AutoType)], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test47(self):
        input = """foo:function void(inherit out a:auto){}"""
        expect = """Program([\n\tFuncDecl(foo, VoidType, [InheritOutParam(a, AutoType)], None, BlockStmt([]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test48(self):
        input = """main: function void() {arr:array[10] of integer={1,2,3,4,5,6,7,8,9,10};
        for(i=0,i<10,i+1)
            printInteger(arr[i]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([IntegerLit(10)], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, ArrayCell(Id(arr), [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
    
    def test49(self):
        input = """main: function void(){
        arr:array[10] of integer={1,2,3,4,5,6,7,8,9,10};
        sum:integer=0;
        for(i=0,i<10,i+1){
            sum=sum+arr[i];
        }
        printInteger(sum);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([IntegerLit(10)], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(Id(arr), [Id(i)])))])), CallStmt(printInteger, Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test50(self):
        input = """main: function void() {n:integer=readInteger(); if((n%5==0) && (n%10!=0)) printString("n is only divisible by 5!");}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), IfStmt(BinExpr(&&, BinExpr(==, BinExpr(%, Id(n), IntegerLit(5)), IntegerLit(0)), BinExpr(!=, BinExpr(%, Id(n), IntegerLit(10)), IntegerLit(0))), CallStmt(printString, StringLit(n is only divisible by 5!)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test51(self):
        input = """main: function void() {n:auto="test auto variable";}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, AutoType, StringLit(test auto variable))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test52(self):
        input = """main: function void() {a:auto=true||false;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        input = """get_power_of_2:function integer(n:integer){return n*n;}"""
        expect = """Program([
	FuncDecl(get_power_of_2, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(n), Id(n)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test54(self):
        input = """main: function void() {do{}while(true);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test55(self):
        input = """convert_USD_to_VND: function float (n:float) {return n*23795.00;}"""
        expect = """Program([
	FuncDecl(convert_USD_to_VND, FloatType, [Param(n, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(n), FloatLit(23795.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test56(self):
        input = """main: function void() {a:integer=1; b:integer=a+2; c:integer=a+b; printInteger(c);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, BinExpr(+, Id(a), IntegerLit(2))), VarDecl(c, IntegerType, BinExpr(+, Id(a), Id(b))), CallStmt(printInteger, Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test57(self):
        input = """foo1:function void(){} foo2:function void() inherit foo1{}"""
        expect = """Program([
	FuncDecl(foo1, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo2, VoidType, [], foo1, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test58(self):
        input = """main: function void () {printString(\"!@#$%^&*()\\\\\\t\\b\\n\");}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(!@#$%^&*()\\\\\\t\\b\\n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test59(self):
        input = """foo:function boolean(a:float,b:float){return a-b<10e-9;} main: function void() {printBoolean(foo(1.3,1.30000001));}"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(<, BinExpr(-, Id(a), Id(b)), FloatLit(1e-08)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, FuncCall(foo, [FloatLit(1.3), FloatLit(1.30000001)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test60(self):
        input = """main: function void() {n:integer=readInteger(); arr:array[100] of integer; for(i=0,i<n,i+1) arr[i]=readInteger(); sum:integer=0; for(i=0,i<n,i+1) sum=sum+arr[i]; printInteger(sum);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(arr, ArrayType([IntegerLit(100)], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(Id(arr), [Id(i)]), FuncCall(readInteger, []))), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(Id(arr), [Id(i)])))), CallStmt(printInteger, Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test61(self):
        input = """get_power_of_m:function integer(n:integer,m:integer){
            result:integer=1;
            for(i=0,i<m,i+1)
                result=result*n;
            return result;
        }"""
        expect = """Program([
	FuncDecl(get_power_of_m, IntegerType, [Param(n, IntegerType), Param(m, IntegerType)], None, BlockStmt([VarDecl(result, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(m)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(result), BinExpr(*, Id(result), Id(n)))), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test62(self):
        input = """main: function void() {arr:array[10,10] of integer; arr[5][2]=1;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([IntegerLit(10), IntegerLit(10)], IntegerType)), AssignStmt(ArrayCell(ArrayCell(Id(arr), [IntegerLit(5)]), [IntegerLit(2)]), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        input = """main: function void () {do{printString("I'm in a loop!");}while(true);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([CallStmt(printString, StringLit(I'm in a loop!))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test64(self):
        input = """main: function void() {arr:array[10] of float={.1e-2,2e-3,3e-1};}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([IntegerLit(10)], FloatType), ArrayLit([FloatLit(0.001), FloatLit(0.002), FloatLit(0.3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = """abs:function integer(n:integer){if(n<0) return -n; return n;} main: function void () {n:integer=readInteger(); printInteger(abs(n));}"""
        expect = """Program([
	FuncDecl(abs, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(0)), ReturnStmt(UnExpr(-, Id(n)))), ReturnStmt(Id(n))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), CallStmt(printInteger, FuncCall(abs, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test66(self):
        input = """main: function void () {a:boolean=!false&&true;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BinExpr(&&, UnExpr(!, BooleanLit(False)), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test67(self):
        input = """foo:function integer(a:integer,b:integer){return -a+b;}"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, UnExpr(-, Id(a)), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test68(self):
        input = """main: function void () {{a:integer;}}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test69(self):
        input = """main: function void() {n:integer=readInteger(); arr:array[100] of integer; for(i=0,i<n,i+1) arr[i]=readInteger(); for(i=0,i<n,i+1){printInteger(arr[i]); printSring(" ");}}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(arr, ArrayType([IntegerLit(100)], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(Id(arr), [Id(i)]), FuncCall(readInteger, []))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(Id(arr), [Id(i)])), CallStmt(printSring, StringLit( ))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = """main: function void() {arr:array[5] of integer={1,2,3,4,5}; a:integer=arr[1];}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([IntegerLit(5)], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), VarDecl(a, IntegerType, ArrayCell(Id(arr), [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test71(self):
        input = """foo:function void(){return;} main: function void(){foo();}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ReturnStmt()]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test72(self):
        input = """get_power_of_3:function integer(n:integer){
            return n*n*n;
        } 
        main: function void() {
        n:integer=readInteger(); 
        arr:array[100] of integer; 
        for(i=0,i<n,i+1) 
            arr[i]=readInteger();
        for(i=0,i<n,i+1)
            arr[i]=get_power_of_3(arr[i]);
        }"""
        expect = """Program([
	FuncDecl(get_power_of_3, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, BinExpr(*, Id(n), Id(n)), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(arr, ArrayType([IntegerLit(100)], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(Id(arr), [Id(i)]), FuncCall(readInteger, []))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(Id(arr), [Id(i)]), FuncCall(get_power_of_3, [ArrayCell(Id(arr), [Id(i)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = """get_power_of_2:function integer(n:integer){
            return n*n;
        } 
        main: function void() {
        n:integer=readInteger(); 
        arr:array[100] of integer; 
        for(i=0,i<n,i+1) 
            arr[i]=readInteger();
        for(i=0,i<n,i+1)
            arr[i]=get_power_of_2(arr[i]);
        }"""
        expect = """Program([
	FuncDecl(get_power_of_2, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(n), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(arr, ArrayType([IntegerLit(100)], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(Id(arr), [Id(i)]), FuncCall(readInteger, []))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(Id(arr), [Id(i)]), FuncCall(get_power_of_2, [ArrayCell(Id(arr), [Id(i)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test74(self):
        input = """main: function void() {
        n:integer=readInteger(); 
        arr:array[100] of integer; 
        for(i=0,i<n,i+1) 
            arr[i]=readInteger();
        printInteger(arr[0]+arr[n-1]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(arr, ArrayType([IntegerLit(100)], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(Id(arr), [Id(i)]), FuncCall(readInteger, []))), CallStmt(printInteger, BinExpr(+, ArrayCell(Id(arr), [IntegerLit(0)]), ArrayCell(Id(arr), [BinExpr(-, Id(n), IntegerLit(1))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = """foo:function float(a:integer,b:float){return a+b;} main: function void () {foo(2,.31e2);}"""
        expect = """Program([
	FuncDecl(foo, FloatType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(2), FloatLit(31.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test76(self):
        input = """main: function integer()
        {n:integer=readInteger(); 
        arr:array[100] of integer;
        for(i=0,i<n,i+1)
        {
            arr[i]=readInteger();
        }
        for(i=0,i<n,i+1)
        {
            if(n%5==0) continue;
            else
            {
                printInteger(arr[i]);
            }
        }
        return 0;
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(arr, ArrayType([IntegerLit(100)], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(i)]), FuncCall(readInteger, []))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), IntegerLit(5)), IntegerLit(0)), ContinueStmt(), BlockStmt([CallStmt(printInteger, ArrayCell(Id(arr), [Id(i)]))]))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = """main: function integer()
        {n:integer=readInteger(); 
        arr:array[100] of integer;
        for(i=0,i<n,i+1)
        {
            arr[i]=readInteger();
        }
        for(i=0,i<n/2,i+1)
        {
            temp:integer=arr[i];
            arr[i]=arr[n-1-i];
            arr[n-1-i]=temp;
        }
        return 0;
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(arr, ArrayType([IntegerLit(100)], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(i)]), FuncCall(readInteger, []))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(temp, IntegerType, ArrayCell(Id(arr), [Id(i)])), AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [BinExpr(-, BinExpr(-, Id(n), IntegerLit(1)), Id(i))])), AssignStmt(ArrayCell(Id(arr), [BinExpr(-, BinExpr(-, Id(n), IntegerLit(1)), Id(i))]), Id(temp))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = """main: function integer () {str:string="Hello world!"; printString(str); return 0;}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(str, StringType, StringLit(Hello world!)), CallStmt(printString, Id(str)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = """main: function void () {for(i=0,true,i+1) break; return 0;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BooleanLit(True), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = """main: function void () {writeFloat(2.3/3.4);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(writeFloat, BinExpr(/, FloatLit(2.3), FloatLit(3.4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test81(self):
        input = """main: function void () {printBoolean(!(1!=2));}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, UnExpr(!, BinExpr(!=, IntegerLit(1), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test82(self):
        input = """main: function void () {frh,cel:float; frh=readFloat(); cel = ((frh * 5.0)-(5.0 * 32))/9; writeFloat(cel);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(frh, FloatType), VarDecl(cel, FloatType), AssignStmt(Id(frh), FuncCall(readFloat, [])), AssignStmt(Id(cel), BinExpr(/, BinExpr(-, BinExpr(*, Id(frh), FloatLit(5.0)), BinExpr(*, FloatLit(5.0), IntegerLit(32))), IntegerLit(9))), CallStmt(writeFloat, Id(cel))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        input = """main: function void () {fahren,celsius:float; celsius=readFloat(); fahren =(9.0/5.0) * celsius + 32; writeFloat(fahren);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(fahren, FloatType), VarDecl(celsius, FloatType), AssignStmt(Id(celsius), FuncCall(readFloat, [])), AssignStmt(Id(fahren), BinExpr(+, BinExpr(*, BinExpr(/, FloatLit(9.0), FloatLit(5.0)), Id(celsius)), IntegerLit(32))), CallStmt(writeFloat, Id(fahren))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test84(self):
        input = """main: function void () {celsius:float=readFloat(); writeFloat(celsius+273.15);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(celsius, FloatType, FuncCall(readFloat, [])), CallStmt(writeFloat, BinExpr(+, Id(celsius), FloatLit(273.15)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test85(self):
        input = """main: function void () {kelvin:float=readFloat(); writeFloat(kelvin-273.15);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(kelvin, FloatType, FuncCall(readFloat, [])), CallStmt(writeFloat, BinExpr(-, Id(kelvin), FloatLit(273.15)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test86(self):
        input = """main: function void () {printBoolean(!(1>=2) || !0 && (2==2));}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, BinExpr(&&, BinExpr(||, UnExpr(!, BinExpr(>=, IntegerLit(1), IntegerLit(2))), UnExpr(!, IntegerLit(0))), BinExpr(==, IntegerLit(2), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test87(self):
        input = """main: function void () {printInteger(-(-203-33+2));}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, UnExpr(-, BinExpr(+, BinExpr(-, UnExpr(-, IntegerLit(203)), IntegerLit(33)), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test88(self):
        input = """main: function void () {input:string=readString(); printBoolean(input=="");}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(input, StringType, FuncCall(readString, [])), CallStmt(printBoolean, BinExpr(==, Id(input), StringLit()))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test89(self):
        input = """main: function void () {input:string=readString(); while((input=="y") || (input=="Y")){input=readString();}}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(input, StringType, FuncCall(readString, [])), WhileStmt(BinExpr(||, BinExpr(==, Id(input), StringLit(y)), BinExpr(==, Id(input), StringLit(Y))), BlockStmt([AssignStmt(Id(input), FuncCall(readString, []))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = """main: function void () {exp:boolean=!(true && false || false);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(exp, BooleanType, UnExpr(!, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), BooleanLit(False))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = """main: function void () {str:string=readString(); printString(str::"EOF");}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(str, StringType, FuncCall(readString, [])), CallStmt(printString, BinExpr(::, Id(str), StringLit(EOF)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = """main: function void () {printInteger(!(----3));}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, UnExpr(!, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(3)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = """main: function void () {printBoolean("Zero");}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, StringLit(Zero))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = """main: function void () {for(i=1,i<=9,i+1) printInteger(5*i);}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(9)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, BinExpr(*, IntegerLit(5), Id(i))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = """main: function void () {str1,str2:string;
        str1=readString();
        str2=readString();
        printString((str1::str2)::"EOF");}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(str1, StringType), VarDecl(str2, StringType), AssignStmt(Id(str1), FuncCall(readString, [])), AssignStmt(Id(str2), FuncCall(readString, [])), CallStmt(printString, BinExpr(::, BinExpr(::, Id(str1), Id(str2)), StringLit(EOF)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test96(self):
        input = """main: function void () {a:array[] of integer={{1,2,3},{4},{5,6}};}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4)]), ArrayLit([IntegerLit(5), IntegerLit(6)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = """isEven: function boolean(a:integer){if(a%2==0) return true; else return false;}"""
        expect = """Program([
	FuncDecl(isEven, BooleanType, [Param(a, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = """compare:function boolean(a:integer,b:integer){return !(a>=b);}"""
        expect = """Program([
	FuncDecl(compare, BooleanType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(UnExpr(!, BinExpr(>=, Id(a), Id(b))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test99(self):
        input = """goo:function void() {} foo:function void(inherit a:auto) inherit goo{}"""
        expect = """Program([
	FuncDecl(goo, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo, VoidType, [InheritParam(a, AutoType)], goo, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test100(self):
        input = """main: function void () {arr1,arr2:array[10] of integer; for(i=0,i<10,i+1) arr1[i]=readInteger(); for(i=0,i<10,i+1) arr2[i]=arr1[9-i]; for(i=0,i<10,i+1){printInteger(arr1[i]);} for(i=0,i<10,i+1){printInteger(arr2[i]);}}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr1, ArrayType([IntegerLit(10)], IntegerType)), VarDecl(arr2, ArrayType([IntegerLit(10)], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(Id(arr1), [Id(i)]), FuncCall(readInteger, []))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(Id(arr2), [Id(i)]), ArrayCell(Id(arr1), [BinExpr(-, IntegerLit(9), Id(i))]))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(Id(arr1), [Id(i)]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(Id(arr2), [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))