import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/////\\nasd','<EOF>', 101))

    def test2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/////\nhello', 'hello,<EOF>', 102))

    def test3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('(){ }[];', '(,),{,},[,],;,<EOF>', 103))
    
    def test4(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('"hello', 'Unclosed String: hello', 104))
    
    def test5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('int float array', 'int,float,array,<EOF>', 105))

    def test6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('var1,var2;var3', 'var1,,,var2,;,var3,<EOF>', 106))

    def test7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('writeFloat();', 'writeFloat,(,),;,<EOF>', 107))
    
    def test8(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('"hello\n"', 'Illegal Escape In String: hello\n', 108))
    
    def test9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('< > == != >= <=', '<,>,==,!=,>=,<=,<EOF>', 109))

    def test10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('+ - * / %', '+,-,*,/,%,<EOF>', 110))

    def test11(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('::', '::,<EOF>', 111))

    def test12(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(', . ; : =', ',,.,;,:,=,<EOF>', 112))

    def test13(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('\\ \\ "', '\\,\\,",<EOF>', 113))
    
    def test14(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('auto break boolean do else', 'auto,break,boolean,do,else,<EOF>', 114))
    
    def test15(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('false float for function if', 'false,float,for,function,if,<EOF>', 115))

    def test16(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('integer return string true while', 'integer,return,string,true,while,<EOF>', 116))

    def test17(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('void out continue of inherit', 'void,out,continue,of,inherit,<EOF>', 117))
    
    def test18(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('array main', 'array,main,<EOF>', 118))
    
    def test19(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('true false', 'true,false,<EOF>', 119))

    def test20(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('254821', '254821,<EOF>', 120))

    def test21(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('-45214', '-,45214,<EOF>', 121))

    def test22(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('32e-4', '32e-4,<EOF>', 122))

    def test23(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('15E-5', '15E-5,<EOF>', 123))
    
    def test24(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('154.0e-3', '154.0e-3,<EOF>', 124))
    
    def test25(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('-56.65E-5', '-,56.65E-5,<EOF>', 125))

    def test26(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('(){}[];', '(,),{},[,],;,<EOF>', 126))

    def test27(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('if(true);', 'if,(,true,),;,<EOF>', 127))
    
    def test28(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('for(i=0,i<10,i+1);', 'for,(,i,=,0,,,i,<,10,,,i,+,1,),;,<EOF>', 128))
    
    def test29(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('arr:array[] of integer;', 'arr,:,array,[,],of,integer,;,<EOF>', 129))

    def test30(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('arr:array[10] of integer;', 'arr,:,array,[,10,],of,integer,;,<EOF>', 130))

    def test31(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('str:string="abc";', 'str,:,string,=,abc,;,<EOF>', 131))

    def test32(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:integer=2;', 'a,:,integer,=,2,;,<EOF>', 132))

    def test33(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:float=2.3e-3;', 'a,:,float,=,2.3e-3,;,<EOF>', 133))
    
    def test34(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:boolean=true;', 'a,:,boolean,=,true,;,<EOF>', 134))
    
    def test35(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('arr[0]=3;', 'arr,[,0,],=,3,;,<EOF>', 135))

    def test36(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('printInteger(3);', 'printInteger,(,3,),;,<EOF>', 136))

    def test37(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('writeFloat(3.56);', 'writeFloat,(,3.56,),;,<EOF>', 137))
    
    def test38(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:integer=readInteger();', 'a,:,integer,=,readInteger,(,),;,<EOF>', 138))
    
    def test39(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:integer=5+11;', 'a,:,integer,=,5,+,11,;,<EOF>', 139))

    def test40(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:integer=5+11+(2-3);', 'a,:,integer,=,5,+,11,+,(,2,-,3,),;,<EOF>', 140))

    def test41(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:float=2.3e-3-3.4;', 'a,:,float,=,2.3e-3,-,3.4,;,<EOF>', 141))

    def test42(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('if(a>b) printString("a is larger than b!");', 'if,(,a,>,b,),printString,(,a is larger than b!,),;,<EOF>', 142))

    def test43(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('str:string="abc"::"xyz";', 'str,:,string,=,abc,::,xyz,;,<EOF>', 143))
    
    def test44(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('main: function void() {}', 'main,:,function,void,(,),{},<EOF>', 144))
    
    def test45(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('foo:function void(){return;}', 'foo,:,function,void,(,),{,return,;,},<EOF>', 145))

    def test46(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('while(true) printString("Looping!");', 'while,(,true,),printString,(,Looping!,),;,<EOF>', 146))

    def test47(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('do{}while()', 'do,{},while,(,),<EOF>', 147))
    
    def test48(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('inherit out', 'inherit,out,<EOF>', 148))
    
    def test49(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:float=2.3/5.0;', 'a,:,float,=,2.3,/,5.0,;,<EOF>', 149))

    def test50(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:integer=11%5;', 'a,:,integer,=,11,%,5,;,<EOF>', 150))

    def test51(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('foo:function integer(a:integer,b:integer){return a+b;}', 'foo,:,function,integer,(,a,:,integer,,,b,:,integer,),{,return,a,+,b,;,},<EOF>', 151))

    def test52(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('printString("!@#$%^&*()\\\\\\t\\b\\n");', 'printString,(,!@#$%^&*()\\\\\\t\\b\\n,),;,<EOF>', 152))

    def test53(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('foo1:function void(){} foo2:function void() inherit foo1', 'foo1,:,function,void,(,),{},foo2,:,function,void,(,),inherit,foo1,<EOF>', 153))
    
    def test54(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:integer=1; b:integer=a+2; c:integer=a+b; printInteger(c);', 'a,:,integer,=,1,;,b,:,integer,=,a,+,2,;,c,:,integer,=,a,+,b,;,printInteger,(,c,),;,<EOF>', 154))
    
    def test55(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('if(true){}else{}', 'if,(,true,),{},else,{},<EOF>', 155))

    def test56(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('return n*23795.00;', 'return,n,*,23795.00,;,<EOF>', 156))

    def test57(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Hello\\tworld!"', 'Hello\\tworld!,<EOF>', 157))
    
    def test58(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('get_power_of_m:function integer(n:integer,m:integer){}', 'get_power_of_m,:,function,integer,(,n,:,integer,,,m,:,integer,),{},<EOF>', 158))
    
    def test59(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('sum=sum+arr[i];', 'sum,=,sum,+,arr,[,i,],;,<EOF>', 159))

    def test60(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('{1,2,3,4,5,6,7,8,9,10}', '{,1,,,2,,,3,,,4,,,5,,,6,,,7,,,8,,,9,,,10,},<EOF>', 160))

    def test61(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"hello \\"Nghia\\""', 'hello \\"Nghia\\",<EOF>', 161))

    def test62(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('"What is \\"PPL\\"?"', 'What is \\"PPL\\"?,<EOF>', 162))

    def test63(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('printBoolean(!(true&&false));', 'printBoolean,(,!,(,true,&&,false,),),;,<EOF>', 163))
    
    def test64(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:integer=readInteger();', 'a,:,integer,=,readInteger,(,),;,<EOF>', 164))
    
    def test65(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('var123_456ABC', 'var123_456ABC,<EOF>', 165))

    def test66(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('int', 'int,<EOF>', 166))

    def test67(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('writeFloat();', 'writeFloat,(,),;,<EOF>', 167))
    
    def test68(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('readFloat();', 'readFloat,(,),;,<EOF>', 168))
    
    def test69(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:auto;', 'a,:,auto,;,<EOF>', 169))

    def test70(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:auto="abc";', 'a,:,auto,=,abc,;,<EOF>', 170))

    def test71(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('!', '!,<EOF>', 171))

    def test72(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('@', 'Error Token @', 172))

    def test73(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('#', 'Error Token #', 173))
    
    def test74(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('$', 'Error Token $', 174))
    
    def test75(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('^', 'Error Token ^', 175))

    def test76(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('&', 'Error Token &', 176))

    def test77(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('|', 'Error Token |', 177))
    
    def test78(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('35+6.5', '35,+,6.5,<EOF>', 178))
    
    def test79(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('name;', 'name,;,<EOF>', 179))

    def test80(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:auto=true||false;', 'a,:,auto,=,true,||,false,;,<EOF>', 180))

    def test81(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:void;', 'a,:,void,;,<EOF>', 181))

    def test82(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('a:auto=;', 'a,:,auto,=,;,<EOF>', 182))

    def test83(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('array[10]', 'array,[,10,],<EOF>', 183))
    
    def test84(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('i<=10', 'i,<=,10,<EOF>', 184))

    def test85(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('n%5==0', 'n,%,5,==,0,<EOF>', 185))

    def test86(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('n%10!=0', 'n,%,10,!=,0,<EOF>', 186))

    def test87(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('do;while();', 'do,;,while,(,),;,<EOF>', 187))
    
    def test88(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('3.e-4', '3.e-4,<EOF>', 188))
    
    def test89(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('foo(2,);', 'foo,(,2,,,),;,<EOF>', 189))

    def test90(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('.1e-3', '.1e-3,<EOF>', 190))

    def test91(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('4./', '4.,/,<EOF>', 191))

    def test92(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('{ {1,2},{3,4} }', '{,{,1,,,2,},,,{,3,,,4,},},<EOF>', 192))

    def test93(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('///////////////\rasd', 'asd,<EOF>', 193))
    
    def test94(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*******************\n********\t\b\r**********\n********/id:integer;', 'id,:,integer,;,<EOF>', 194))
    
    def test95(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('/*///////////////////////////////////////////*/', '<EOF>', 195))

    def test96(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('print();', 'print,(,),;,<EOF>', 196))

    def test97(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('printBoolean(a-b<10e-9);', 'printBoolean,(,a,-,b,<,10e-9,),;,<EOF>', 197))
    
    def test98(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('\'\'', '\',\',<EOF>', 198))
    
    def test99(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('"Hello\n', 'Illegal Escape In String: Hello\n', 199))

    def test100(self): #################### Error! ########################
        """test identifiers"""
        self.assertTrue(TestLexer.test('"This string is unclosed', 'Unclosed String: This string is unclosed', 200))
