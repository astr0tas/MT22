import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test1(self):
        """Simple program: int main() {} """
        input = """main:function void(){writeFloat(-2.65e-3);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test2(self):
        """Simple program: int main() {} """
        input = """isEven: function boolean(a:integer){if(a%2==0) return true; else return false;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test3(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    
    def test4(self):
        """Simple program: int main() {} """
        input = """main: function void () {n:float=readFloat(); writeFloat(n);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test5(self):
        """Simple program: int main() {} """
        input = """main: function void () {writeFloat(2.e-7+3e-1);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test6(self):
        """Simple program: int main() {} """
        input = """main: function void () {preventDefault();}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test7(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:integer=5+6-(123*10+(24-30));}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test8(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[] of string={"string1","string2","string3"};}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test9(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[] of float={};}"""
        expect = "Error on line 1 col 44: {}"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test10(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[5,5] of integer={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    def test11(self):
        """Simple program: int main() {} """
        input = """calculate_C: function float () {r:float=readFloat(); pi:float=3.14; C:float=2*r*pi; return C;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test12(self):
        """Simple program: int main() {} """
        input = """main: function void () {do{printString("I'm in a loop!");}while(true);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test13(self):
        """Simple program: int main() {} """
        input = """main: function void() {var:flaot;}"""
        expect = "Error on line 1 col 27: flaot"
        self.assertTrue(TestParser.test(input, expect, 213))
    
    def test14(self):
        """Simple program: int main() {} """
        input = """compare:function boolean(a:integer,b:integer){return a>=b;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        """Simple program: int main() {} """
        input = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a+b);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test16(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:integer=readInteger(); b:integer=readInteger(); printInteger(a*b);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test17(self):
        """Simple program: int main() {} """
        input = """main: function void () {while(true);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        """Simple program: int main() {} """
        input = """main: function void () {while();}"""
        expect = "Error on line 1 col 30: )"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test19(self):
        """Simple program: int main() {} """
        input = """main: function void () {foo(4/);}"""
        expect = "Error on line 1 col 30: )"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[2] of boolean={true,false};}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test21(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[3,3] of integer={{},{},{}};}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test22(self):
        """Simple program: int main() {} """
        input = """main: function void () {printBoolean(1+1==2);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test23(self):
        """Simple program: int main() {} """
        input = """main: function void () {for(i=0,true,i+1) break;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    
    def test24(self):
        """Simple program: int main() {} """
        input = """main: function void () {if(true);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test25(self):
        """Simple program: int main() {} """
        input = """main: function void () {if(true){}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test26(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[] of float={1.3,5.6,4.2};}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test27(self):
        """Simple program: int main() {} """
        input = """main: function void () {printInteger();}"""
        expect = "Error on line 1 col 37: )"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test28(self):
        """Simple program: int main() {} """
        input = """main: function void () {printBoolean(!!false);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test29(self):
        """Simple program: int main() {} """
        input = """main: function void () {printInteger(---3);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test30(self):
        """Simple program: int main() {} """
        input = """uselessFunc:function integer(){return 0;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
    
    def test31(self):
        """Simple program: int main() {} """
        input = """uselessFunc:function string(){return "Zero";}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test32(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:int;}"""
        expect = "Error on line 1 col 25: int"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test33(self):
        """Simple program: int main() {} """
        input = """main: function void() {b:bool;}"""
        expect = "Error on line 1 col 25: bool"
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def test34(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:integer=;}"""
        expect = "Error on line 1 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test35(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[ of integer;}"""
        expect = "Error on line 1 col 34: of"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test36(self):
        """Simple program: int main() {} """
        input = """main: function void() {str:string="abc"::"def";}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test37(self):
        """Simple program: int main() {} """
        input = """main: function void() {str:string="abc"::"def"::("ghi"::"jkl");}"""
        expect = "Error on line 1 col 46: ::"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test38(self):
        """Simple program: int main() {} """
        input = """main: function void() {exp:boolean=!(true && false || false);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[10] of integer; arr[0]=1;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test40(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[10,10] of integer; arr[5][2]=1;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test41(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[10] of float={.1e-2,2e-3,3e-1};}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test42(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[10] of float; writeFloat(arr[2]);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test43(self):
        """Simple program: int main() {} """
        input = """print: function void(str:string) {printString(str);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    
    def test44(self):
        """Simple program: int main() {} """
        input = """concatString: function string(str1:string,str2:string) {return str1::str2;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test45(self):
        """Simple program: int main() {} """
        input = """main: function void() {a,b,c:integer=1,2,3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test46(self):
        """Simple program: int main() {} """
        input = """main: function void() {a,b,c:integer=1,2,3,4;}"""
        expect = "Error on line 1 col 42: ,"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test47(self):
        """Simple program: int main() {} """
        input = """main: function void() {a,b,c:integer=1,2;}"""
        expect = "Error on line 1 col 40: ;"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        """Simple program: int main() {} """
        input = """main: function void() {str:string="abc"::("def"::("ghi"::"jkl"));}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test49(self):
        """Simple program: int main() {} """
        input = """abs:function integer(n:integer){if(n<0) return -n; return n;} main: function void () {n:integer=readInteger(); printInteger(abs(n));}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test50(self):
        """Simple program: int main() {} """
        input = """fibonacci:function integer(n:integer){if(n==0) return 0; if(n==1) return 1; return fibonacci(n-1)+fibonacci(n-2);} main: function void() {n:integer=readInteger(); printInteger(fibonacci(n));}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test51(self):
        """Simple program: int main() {} """
        input = """main: function void() {str:string="abc":"xyz";}"""
        expect = "Error on line 1 col 39: :"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test52(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:auto;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test53(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:auto=true||false;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    
    def test54(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:auto=2.3e+3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test55(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:auto="hello!";}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test56(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:void;}"""
        expect = "Error on line 1 col 25: void"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test57(self):
        """Simple program: int main() {} """
        input = """foo:function void(a:void){}"""
        expect = "Error on line 1 col 20: void"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test58(self):
        """Simple program: int main() {} """
        input = """foo:function void(inherit a:auto){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test59(self):
        """Simple program: int main() {} """
        input = """foo:function void(out a:auto){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test60(self):
        """Simple program: int main() {} """
        input = """foo:function void(inherit out a:auto){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test61(self):
        """Simple program: int main() {} """
        input = """foo:function void(out inherit a:auto){}"""
        expect = "Error on line 1 col 22: inherit"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test62(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:atuo;}"""
        expect = "Error on line 1 col 25: atuo"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test63(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:auto=;}"""
        expect = "Error on line 1 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 263))
    
    def test64(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[10] of integer={1,2,3,4,5,6,7,8,9,10};
        for(i=0,i<10,i+1)
            printInteger(arr[i]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test65(self):
        """Simple program: int main() {} """
        input = """main: function void(){
        arr:array[10] of integer={1,2,3,4,5,6,7,8,9,10};
        sum:integer=0;
        for(i=0,i<10,i+1){
            sum=sum+arr[i];
        }
        printInteger(sum);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test66(self):
        """Simple program: int main() {} """
        input = """main: function void(){
        arr:array[10] of integer={1,2,3,4,5,6,7,8,9,10};
        sum:integer=0;
        for(i=0,i<10,i+1){
            if(arr[i]%2==0)
                sum=sum+arr[i];
        }
        printInteger(sum);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test67(self):
        """Simple program: int main() {} """
        input = """main: function void(){
        arr:array[10] of integer={1,2,3,4,5,6,7,8,9,10};
        sum:integer=0;
        for(i=0,i<10,i+1){
            if(arr[i]%2!=0)
                sum=sum+arr[i];
        }
        printInteger(sum);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test68(self):
        """Simple program: int main() {} """
        input = """main: function void() {n:integer=readInteger(); if((n%5==0) && (n%10!=0)) printString("Is only divisible by 5!");}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test69(self):
        """Simple program: int main() {} """
        input = """get_power_of_2:function integer(n:integer){return n*n;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test70(self):
        """Simple program: int main() {} """
        input = """get_power_of_3:function integer(n:integer){return n*n*n;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test71(self):
        """Simple program: int main() {} """
        input = """get_power_of_m:function integer(n:integer,m:integer){
            result:integer=1;
            for(i=0,i<m,i+1)
                result=result*n;
            return result;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test72(self):
        """Simple program: int main() {} """
        input = """main: function void() {for(int i=0,i<10,i+1);}"""
        expect = "Error on line 1 col 31: i"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test73(self):
        """Simple program: int main() {} """
        input = """main: function void() {for(i=0,i<10,i++);}"""
        expect = "Error on line 1 col 38: +"
        self.assertTrue(TestParser.test(input, expect, 273))
    
    def test74(self):
        """Simple program: int main() {} """
        input = """main: function void() {for(i=0;i<10;i+1);}"""
        expect = "Error on line 1 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test75(self):
        """Simple program: int main() {} """
        input = """main: function void() {do{}while(true)}"""
        expect = "Error on line 1 col 38: }"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test76(self):
        """Simple program: int main() {} """
        input = """main: function void() {do{}while();}"""
        expect = "Error on line 1 col 33: )"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test77(self):
        """Simple program: int main() {} """
        input = """convert_USD_to_VND: function float (n:float) {return n*23795.00;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test78(self):
        """Simple program: int main() {} """
        input = """convert_VND_to_USD: function float (n:float) {return n/23795.00;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test79(self):
        """Simple program: int main() {} """
        input = """main: function void() {if(true){}else{}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test80(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr:array[5] of integer={1,2,3,4,5}; a:integer=arr[];}"""
        expect = "Error on line 1 col 74: ]"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test81(self):
        """Simple program: int main() {} """
        input = """main: function void() {a:integer=1; b:integer=a+2; c:integer=a+b; printInteger(c);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test82(self):
        """Simple program: int main() {} """
        input = """foo1:function void(){} foo2:function void() inherit foo1{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test83(self):
        """Simple program: int main() {} """
        input = """foo1:function void(){} foo2:function void() inherit foo1(){}"""
        expect = "Error on line 1 col 56: ("
        self.assertTrue(TestParser.test(input, expect, 283))
    
    def test84(self):
        """Simple program: int main() {} """
        input = """foo1:function void(){} foo2:function void() inherit {}"""
        expect = "Error on line 1 col 52: {}"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test85(self):
        """Simple program: int main() {} """
        input = """foo1:function void(){} foo2:function void() inherit foo1"""
        expect = "Error on line 1 col 56: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test86(self):
        """Simple program: int main() {} """
        input = """foo:function integer(a:integer,b:integer){return a+b;} main: function void () {foo(2,);}"""
        expect = "Error on line 1 col 85: )"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test87(self):
        """Simple program: int main() {} """
        input = """main: function void () {printString("!@#$%^&*()\\\\\\t\\b\\n");}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test88(self):
        """Simple program: int main() {} """
        input = """main: function void() {if();}"""
        expect = "Error on line 1 col 26: )"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test89(self):
        """Simple program: int main() {} """
        input = """main: function void() {else{}}"""
        expect = "Error on line 1 col 23: else"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test90(self):
        """Simple program: int main() {} """
        input = """main: function void() {do{}}"""
        expect = "Error on line 1 col 27: }"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test91(self):
        """Simple program: int main() {} """
        input = """foo:function void(){return;} main: function void(){foo();}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test92(self):
        """Simple program: int main() {} """
        input = """foo:function boolean(a:float,b:float){return a-b<10e-9;} main: function void() {printBoolean(foo(1.3,1.30000001));}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test93(self):
        """Simple program: int main() {} """
        input = """main: function void() {arr1:array[10] of integer={1,2,3,4,5,6,7,8,9,10}; arr2:array[5] of integer; for(i=0,i<5,i+1) arr2[i]=arr1[i];}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    
    def test94(self):
        """Simple program: int main() {} """
        input = """main: function void() {str:string=readString(); printString(str);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test95(self):
        """Simple program: int main() {} """
        input = """main: function void() {n:integer=readInteger(); arr:array[100] of integer; for(i=0,i<n,i+1) arr[i]=readInteger(); for(i=0,i<n,i+1){printInteger(arr[i]); printSring(" ");}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test96(self):
        """Simple program: int main() {} """
        input = """main: function void() {n:integer=readInteger(); arr:array[100] of integer; for(i=0,i<n,i+1) arr[i]=readInteger(); sum:integer=0; for(i=0,i<n,i+1) sum=sum+arr[i]; printInteger(sum);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test97(self):
        """Simple program: int main() {} """
        input = """main: function void() {
        n:integer=readInteger(); 
        arr1:array[100] of integer; 
        for(i=0,i<n,i+1) 
            arr1[i]=readInteger();
        arr2:array[100] of integer;
        for(i=n-1,i>=0,i-1)
            arr2[n-1-i]=arr1[i];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test98(self):
        """Simple program: int main() {} """
        input = """main: function void() {
        n:integer=readInteger(); 
        arr:array[100] of integer; 
        for(i=0,i<n,i+1) 
            arr[i]=readInteger();
        printInteger(arr[0]+arr[n-1]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test99(self):
        """Simple program: int main() {} """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test100(self):
        """Simple program: int main() {} """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
