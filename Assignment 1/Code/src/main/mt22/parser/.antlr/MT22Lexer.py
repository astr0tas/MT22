# Generated from e:\Semesters\Semester 222\Principles of Programming Languages\Assignments\Assignment 1\Code\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# StudentID: 2011672 - Dương Nguyễn Nguyên Nghĩa
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2L")
        buf.write("\u0275\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\7\r\u0115\n\r\f\r\16\r\u0118\13\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\7\16\u0120\n\16\f\16\16\16\u0123")
        buf.write("\13\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\7\17\u012d")
        buf.write("\n\17\f\17\16\17\u0130\13\17\3\17\3\17\6\17\u0134\n\17")
        buf.write("\r\17\16\17\u0135\7\17\u0138\n\17\f\17\16\17\u013b\13")
        buf.write("\17\3\17\5\17\u013e\n\17\3\20\3\20\5\20\u0142\n\20\3\20")
        buf.write("\7\20\u0145\n\20\f\20\16\20\u0148\13\20\3\20\3\20\5\20")
        buf.write("\u014c\n\20\3\20\6\20\u014f\n\20\r\20\16\20\u0150\5\20")
        buf.write("\u0153\n\20\3\20\3\20\6\20\u0157\n\20\r\20\16\20\u0158")
        buf.write("\3\20\3\20\5\20\u015d\n\20\3\20\6\20\u0160\n\20\r\20\16")
        buf.write("\20\u0161\5\20\u0164\n\20\5\20\u0166\n\20\3\20\3\20\3")
        buf.write("\21\3\21\5\21\u016c\n\21\3\22\3\22\3\22\3\22\7\22\u0172")
        buf.write("\n\22\f\22\16\22\u0175\13\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\7\23\u017e\n\23\f\23\16\23\u0181\13\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u018d")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>")
        buf.write("\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\7E\u024c\n")
        buf.write("E\fE\16E\u024f\13E\3F\3F\3G\3G\3H\3H\3I\6I\u0258\nI\r")
        buf.write("I\16I\u0259\3I\3I\3J\3J\3J\3J\7J\u0262\nJ\fJ\16J\u0265")
        buf.write("\13J\3J\3J\3K\3K\7K\u026b\nK\fK\16K\u026e\13K\3K\3K\3")
        buf.write("K\3L\3L\3L\3\u0121\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\2)\25+\26-\27/\30\61\31\63\32\65\33\67\349\35;\36=")
        buf.write("\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60a\61c\62e\63")
        buf.write("g\64i\65k\66m\67o8q9s:u;w<y={>}?\177@\u0081A\u0083B\u0085")
        buf.write("C\u0087D\u0089E\u008bF\u008dG\u008fH\u0091I\u0093J\u0095")
        buf.write("K\u0097L\3\2\f\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\2\u0291\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2")
        buf.write("\2\5\u009c\3\2\2\2\7\u00a8\3\2\2\2\t\u00b5\3\2\2\2\13")
        buf.write("\u00bf\3\2\2\2\r\u00ca\3\2\2\2\17\u00d7\3\2\2\2\21\u00e4")
        buf.write("\3\2\2\2\23\u00ef\3\2\2\2\25\u00fb\3\2\2\2\27\u0101\3")
        buf.write("\2\2\2\31\u0110\3\2\2\2\33\u011b\3\2\2\2\35\u013d\3\2")
        buf.write("\2\2\37\u0165\3\2\2\2!\u016b\3\2\2\2#\u016d\3\2\2\2%\u0179")
        buf.write("\3\2\2\2\'\u018c\3\2\2\2)\u018e\3\2\2\2+\u0193\3\2\2\2")
        buf.write("-\u0199\3\2\2\2/\u01a1\3\2\2\2\61\u01a4\3\2\2\2\63\u01a9")
        buf.write("\3\2\2\2\65\u01af\3\2\2\2\67\u01b5\3\2\2\29\u01b9\3\2")
        buf.write("\2\2;\u01c2\3\2\2\2=\u01c5\3\2\2\2?\u01cd\3\2\2\2A\u01d4")
        buf.write("\3\2\2\2C\u01db\3\2\2\2E\u01e0\3\2\2\2G\u01e6\3\2\2\2")
        buf.write("I\u01eb\3\2\2\2K\u01ef\3\2\2\2M\u01f8\3\2\2\2O\u01fb\3")
        buf.write("\2\2\2Q\u0203\3\2\2\2S\u0209\3\2\2\2U\u020e\3\2\2\2W\u0210")
        buf.write("\3\2\2\2Y\u0212\3\2\2\2[\u0214\3\2\2\2]\u0216\3\2\2\2")
        buf.write("_\u0218\3\2\2\2a\u021a\3\2\2\2c\u021d\3\2\2\2e\u0220\3")
        buf.write("\2\2\2g\u0223\3\2\2\2i\u0226\3\2\2\2k\u0228\3\2\2\2m\u022b")
        buf.write("\3\2\2\2o\u022d\3\2\2\2q\u0230\3\2\2\2s\u0233\3\2\2\2")
        buf.write("u\u0235\3\2\2\2w\u0237\3\2\2\2y\u0239\3\2\2\2{\u023b\3")
        buf.write("\2\2\2}\u023d\3\2\2\2\177\u023f\3\2\2\2\u0081\u0241\3")
        buf.write("\2\2\2\u0083\u0243\3\2\2\2\u0085\u0245\3\2\2\2\u0087\u0247")
        buf.write("\3\2\2\2\u0089\u0249\3\2\2\2\u008b\u0250\3\2\2\2\u008d")
        buf.write("\u0252\3\2\2\2\u008f\u0254\3\2\2\2\u0091\u0257\3\2\2\2")
        buf.write("\u0093\u025d\3\2\2\2\u0095\u0268\3\2\2\2\u0097\u0272\3")
        buf.write("\2\2\2\u0099\u009a\7}\2\2\u009a\u009b\7\177\2\2\u009b")
        buf.write("\4\3\2\2\2\u009c\u009d\7t\2\2\u009d\u009e\7g\2\2\u009e")
        buf.write("\u009f\7c\2\2\u009f\u00a0\7f\2\2\u00a0\u00a1\7K\2\2\u00a1")
        buf.write("\u00a2\7p\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4\7g\2\2\u00a4")
        buf.write("\u00a5\7i\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7t\2\2\u00a7")
        buf.write("\6\3\2\2\2\u00a8\u00a9\7r\2\2\u00a9\u00aa\7t\2\2\u00aa")
        buf.write("\u00ab\7k\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7v\2\2\u00ad")
        buf.write("\u00ae\7K\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7v\2\2\u00b0")
        buf.write("\u00b1\7g\2\2\u00b1\u00b2\7i\2\2\u00b2\u00b3\7g\2\2\u00b3")
        buf.write("\u00b4\7t\2\2\u00b4\b\3\2\2\2\u00b5\u00b6\7t\2\2\u00b6")
        buf.write("\u00b7\7g\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9\7f\2\2\u00b9")
        buf.write("\u00ba\7H\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7q\2\2\u00bc")
        buf.write("\u00bd\7c\2\2\u00bd\u00be\7v\2\2\u00be\n\3\2\2\2\u00bf")
        buf.write("\u00c0\7y\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7k\2\2\u00c2")
        buf.write("\u00c3\7v\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7H\2\2\u00c5")
        buf.write("\u00c6\7n\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7c\2\2\u00c8")
        buf.write("\u00c9\7v\2\2\u00c9\f\3\2\2\2\u00ca\u00cb\7t\2\2\u00cb")
        buf.write("\u00cc\7g\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7f\2\2\u00ce")
        buf.write("\u00cf\7D\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7q\2\2\u00d1")
        buf.write("\u00d2\7q\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7g\2\2\u00d4")
        buf.write("\u00d5\7c\2\2\u00d5\u00d6\7p\2\2\u00d6\16\3\2\2\2\u00d7")
        buf.write("\u00d8\7r\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7k\2\2\u00da")
        buf.write("\u00db\7p\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7D\2\2\u00dd")
        buf.write("\u00de\7q\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7n\2\2\u00e0")
        buf.write("\u00e1\7g\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\20\3\2\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7g\2\2\u00e6")
        buf.write("\u00e7\7c\2\2\u00e7\u00e8\7f\2\2\u00e8\u00e9\7U\2\2\u00e9")
        buf.write("\u00ea\7v\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7k\2\2\u00ec")
        buf.write("\u00ed\7p\2\2\u00ed\u00ee\7i\2\2\u00ee\22\3\2\2\2\u00ef")
        buf.write("\u00f0\7r\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7k\2\2\u00f2")
        buf.write("\u00f3\7p\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5\7U\2\2\u00f5")
        buf.write("\u00f6\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7k\2\2\u00f8")
        buf.write("\u00f9\7p\2\2\u00f9\u00fa\7i\2\2\u00fa\24\3\2\2\2\u00fb")
        buf.write("\u00fc\7u\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7r\2\2\u00fe")
        buf.write("\u00ff\7g\2\2\u00ff\u0100\7t\2\2\u0100\26\3\2\2\2\u0101")
        buf.write("\u0102\7r\2\2\u0102\u0103\7t\2\2\u0103\u0104\7g\2\2\u0104")
        buf.write("\u0105\7x\2\2\u0105\u0106\7g\2\2\u0106\u0107\7p\2\2\u0107")
        buf.write("\u0108\7v\2\2\u0108\u0109\7F\2\2\u0109\u010a\7g\2\2\u010a")
        buf.write("\u010b\7h\2\2\u010b\u010c\7c\2\2\u010c\u010d\7w\2\2\u010d")
        buf.write("\u010e\7n\2\2\u010e\u010f\7v\2\2\u010f\30\3\2\2\2\u0110")
        buf.write("\u0111\7\61\2\2\u0111\u0112\7\61\2\2\u0112\u0116\3\2\2")
        buf.write("\2\u0113\u0115\n\2\2\2\u0114\u0113\3\2\2\2\u0115\u0118")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u0119\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\b\r\2\2")
        buf.write("\u011a\32\3\2\2\2\u011b\u011c\7\61\2\2\u011c\u011d\7,")
        buf.write("\2\2\u011d\u0121\3\2\2\2\u011e\u0120\13\2\2\2\u011f\u011e")
        buf.write("\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u0122\3\2\2\2\u0121")
        buf.write("\u011f\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0121\3\2\2\2")
        buf.write("\u0124\u0125\7,\2\2\u0125\u0126\7\61\2\2\u0126\u0127\3")
        buf.write("\2\2\2\u0127\u0128\b\16\2\2\u0128\34\3\2\2\2\u0129\u013e")
        buf.write("\7\62\2\2\u012a\u012e\t\3\2\2\u012b\u012d\t\4\2\2\u012c")
        buf.write("\u012b\3\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2")
        buf.write("\u012e\u012f\3\2\2\2\u012f\u0139\3\2\2\2\u0130\u012e\3")
        buf.write("\2\2\2\u0131\u0133\7a\2\2\u0132\u0134\t\4\2\2\u0133\u0132")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0133\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0131\3\2\2\2")
        buf.write("\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3")
        buf.write("\2\2\2\u013a\u013c\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013e")
        buf.write("\b\17\3\2\u013d\u0129\3\2\2\2\u013d\u012a\3\2\2\2\u013e")
        buf.write("\36\3\2\2\2\u013f\u0141\5\35\17\2\u0140\u0142\7\60\2\2")
        buf.write("\u0141\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0146\3")
        buf.write("\2\2\2\u0143\u0145\t\4\2\2\u0144\u0143\3\2\2\2\u0145\u0148")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u0152\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014b\t\5\2\2")
        buf.write("\u014a\u014c\t\6\2\2\u014b\u014a\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014c\u014e\3\2\2\2\u014d\u014f\t\4\2\2\u014e\u014d")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u014e\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0149\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153\u0166\3\2\2\2\u0154\u0156\7")
        buf.write("\60\2\2\u0155\u0157\t\4\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u0163\3\2\2\2\u015a\u015c\t\5\2\2\u015b\u015d\t")
        buf.write("\6\2\2\u015c\u015b\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f")
        buf.write("\3\2\2\2\u015e\u0160\t\4\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0162\u0164\3\2\2\2\u0163\u015a\3\2\2\2\u0163\u0164\3")
        buf.write("\2\2\2\u0164\u0166\3\2\2\2\u0165\u013f\3\2\2\2\u0165\u0154")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\b\20\4\2\u0168")
        buf.write(" \3\2\2\2\u0169\u016c\5C\"\2\u016a\u016c\5\63\32\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016c\"\3\2\2\2\u016d")
        buf.write("\u0173\5\u008dG\2\u016e\u0172\n\7\2\2\u016f\u0170\7^\2")
        buf.write("\2\u0170\u0172\t\b\2\2\u0171\u016e\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0176\u0177\5\u008dG\2\u0177\u0178\b\22\5\2\u0178$\3")
        buf.write("\2\2\2\u0179\u017f\5{>\2\u017a\u017b\5\'\24\2\u017b\u017c")
        buf.write("\5\177@\2\u017c\u017e\3\2\2\2\u017d\u017a\3\2\2\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183\5")
        buf.write("\'\24\2\u0183\u0184\3\2\2\2\u0184\u0185\5}?\2\u0185&\3")
        buf.write("\2\2\2\u0186\u018d\5\35\17\2\u0187\u018d\5\37\20\2\u0188")
        buf.write("\u018d\5!\21\2\u0189\u018d\5#\22\2\u018a\u018d\5%\23\2")
        buf.write("\u018b\u018d\5\u0089E\2\u018c\u0186\3\2\2\2\u018c\u0187")
        buf.write("\3\2\2\2\u018c\u0188\3\2\2\2\u018c\u0189\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018b\3\2\2\2\u018d(\3\2\2\2\u018e")
        buf.write("\u018f\7c\2\2\u018f\u0190\7w\2\2\u0190\u0191\7v\2\2\u0191")
        buf.write("\u0192\7q\2\2\u0192*\3\2\2\2\u0193\u0194\7d\2\2\u0194")
        buf.write("\u0195\7t\2\2\u0195\u0196\7g\2\2\u0196\u0197\7c\2\2\u0197")
        buf.write("\u0198\7m\2\2\u0198,\3\2\2\2\u0199\u019a\7d\2\2\u019a")
        buf.write("\u019b\7q\2\2\u019b\u019c\7q\2\2\u019c\u019d\7n\2\2\u019d")
        buf.write("\u019e\7g\2\2\u019e\u019f\7c\2\2\u019f\u01a0\7p\2\2\u01a0")
        buf.write(".\3\2\2\2\u01a1\u01a2\7f\2\2\u01a2\u01a3\7q\2\2\u01a3")
        buf.write("\60\3\2\2\2\u01a4\u01a5\7g\2\2\u01a5\u01a6\7n\2\2\u01a6")
        buf.write("\u01a7\7u\2\2\u01a7\u01a8\7g\2\2\u01a8\62\3\2\2\2\u01a9")
        buf.write("\u01aa\7h\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac\7n\2\2\u01ac")
        buf.write("\u01ad\7u\2\2\u01ad\u01ae\7g\2\2\u01ae\64\3\2\2\2\u01af")
        buf.write("\u01b0\7h\2\2\u01b0\u01b1\7n\2\2\u01b1\u01b2\7q\2\2\u01b2")
        buf.write("\u01b3\7c\2\2\u01b3\u01b4\7v\2\2\u01b4\66\3\2\2\2\u01b5")
        buf.write("\u01b6\7h\2\2\u01b6\u01b7\7q\2\2\u01b7\u01b8\7t\2\2\u01b8")
        buf.write("8\3\2\2\2\u01b9\u01ba\7h\2\2\u01ba\u01bb\7w\2\2\u01bb")
        buf.write("\u01bc\7p\2\2\u01bc\u01bd\7e\2\2\u01bd\u01be\7v\2\2\u01be")
        buf.write("\u01bf\7k\2\2\u01bf\u01c0\7q\2\2\u01c0\u01c1\7p\2\2\u01c1")
        buf.write(":\3\2\2\2\u01c2\u01c3\7k\2\2\u01c3\u01c4\7h\2\2\u01c4")
        buf.write("<\3\2\2\2\u01c5\u01c6\7k\2\2\u01c6\u01c7\7p\2\2\u01c7")
        buf.write("\u01c8\7v\2\2\u01c8\u01c9\7g\2\2\u01c9\u01ca\7i\2\2\u01ca")
        buf.write("\u01cb\7g\2\2\u01cb\u01cc\7t\2\2\u01cc>\3\2\2\2\u01cd")
        buf.write("\u01ce\7t\2\2\u01ce\u01cf\7g\2\2\u01cf\u01d0\7v\2\2\u01d0")
        buf.write("\u01d1\7w\2\2\u01d1\u01d2\7t\2\2\u01d2\u01d3\7p\2\2\u01d3")
        buf.write("@\3\2\2\2\u01d4\u01d5\7u\2\2\u01d5\u01d6\7v\2\2\u01d6")
        buf.write("\u01d7\7t\2\2\u01d7\u01d8\7k\2\2\u01d8\u01d9\7p\2\2\u01d9")
        buf.write("\u01da\7i\2\2\u01daB\3\2\2\2\u01db\u01dc\7v\2\2\u01dc")
        buf.write("\u01dd\7t\2\2\u01dd\u01de\7w\2\2\u01de\u01df\7g\2\2\u01df")
        buf.write("D\3\2\2\2\u01e0\u01e1\7y\2\2\u01e1\u01e2\7j\2\2\u01e2")
        buf.write("\u01e3\7k\2\2\u01e3\u01e4\7n\2\2\u01e4\u01e5\7g\2\2\u01e5")
        buf.write("F\3\2\2\2\u01e6\u01e7\7x\2\2\u01e7\u01e8\7q\2\2\u01e8")
        buf.write("\u01e9\7k\2\2\u01e9\u01ea\7f\2\2\u01eaH\3\2\2\2\u01eb")
        buf.write("\u01ec\7q\2\2\u01ec\u01ed\7w\2\2\u01ed\u01ee\7v\2\2\u01ee")
        buf.write("J\3\2\2\2\u01ef\u01f0\7e\2\2\u01f0\u01f1\7q\2\2\u01f1")
        buf.write("\u01f2\7p\2\2\u01f2\u01f3\7v\2\2\u01f3\u01f4\7k\2\2\u01f4")
        buf.write("\u01f5\7p\2\2\u01f5\u01f6\7w\2\2\u01f6\u01f7\7g\2\2\u01f7")
        buf.write("L\3\2\2\2\u01f8\u01f9\7q\2\2\u01f9\u01fa\7h\2\2\u01fa")
        buf.write("N\3\2\2\2\u01fb\u01fc\7k\2\2\u01fc\u01fd\7p\2\2\u01fd")
        buf.write("\u01fe\7j\2\2\u01fe\u01ff\7g\2\2\u01ff\u0200\7t\2\2\u0200")
        buf.write("\u0201\7k\2\2\u0201\u0202\7v\2\2\u0202P\3\2\2\2\u0203")
        buf.write("\u0204\7c\2\2\u0204\u0205\7t\2\2\u0205\u0206\7t\2\2\u0206")
        buf.write("\u0207\7c\2\2\u0207\u0208\7{\2\2\u0208R\3\2\2\2\u0209")
        buf.write("\u020a\7o\2\2\u020a\u020b\7c\2\2\u020b\u020c\7k\2\2\u020c")
        buf.write("\u020d\7p\2\2\u020dT\3\2\2\2\u020e\u020f\7-\2\2\u020f")
        buf.write("V\3\2\2\2\u0210\u0211\7/\2\2\u0211X\3\2\2\2\u0212\u0213")
        buf.write("\7,\2\2\u0213Z\3\2\2\2\u0214\u0215\7\61\2\2\u0215\\\3")
        buf.write("\2\2\2\u0216\u0217\7\'\2\2\u0217^\3\2\2\2\u0218\u0219")
        buf.write("\7#\2\2\u0219`\3\2\2\2\u021a\u021b\7(\2\2\u021b\u021c")
        buf.write("\7(\2\2\u021cb\3\2\2\2\u021d\u021e\7~\2\2\u021e\u021f")
        buf.write("\7~\2\2\u021fd\3\2\2\2\u0220\u0221\7?\2\2\u0221\u0222")
        buf.write("\7?\2\2\u0222f\3\2\2\2\u0223\u0224\7#\2\2\u0224\u0225")
        buf.write("\7?\2\2\u0225h\3\2\2\2\u0226\u0227\7>\2\2\u0227j\3\2\2")
        buf.write("\2\u0228\u0229\7>\2\2\u0229\u022a\7?\2\2\u022al\3\2\2")
        buf.write("\2\u022b\u022c\7@\2\2\u022cn\3\2\2\2\u022d\u022e\7@\2")
        buf.write("\2\u022e\u022f\7?\2\2\u022fp\3\2\2\2\u0230\u0231\7<\2")
        buf.write("\2\u0231\u0232\7<\2\2\u0232r\3\2\2\2\u0233\u0234\7*\2")
        buf.write("\2\u0234t\3\2\2\2\u0235\u0236\7+\2\2\u0236v\3\2\2\2\u0237")
        buf.write("\u0238\7]\2\2\u0238x\3\2\2\2\u0239\u023a\7_\2\2\u023a")
        buf.write("z\3\2\2\2\u023b\u023c\7}\2\2\u023c|\3\2\2\2\u023d\u023e")
        buf.write("\7\177\2\2\u023e~\3\2\2\2\u023f\u0240\7.\2\2\u0240\u0080")
        buf.write("\3\2\2\2\u0241\u0242\7\60\2\2\u0242\u0082\3\2\2\2\u0243")
        buf.write("\u0244\7=\2\2\u0244\u0084\3\2\2\2\u0245\u0246\7<\2\2\u0246")
        buf.write("\u0086\3\2\2\2\u0247\u0248\7?\2\2\u0248\u0088\3\2\2\2")
        buf.write("\u0249\u024d\t\t\2\2\u024a\u024c\t\n\2\2\u024b\u024a\3")
        buf.write("\2\2\2\u024c\u024f\3\2\2\2\u024d\u024b\3\2\2\2\u024d\u024e")
        buf.write("\3\2\2\2\u024e\u008a\3\2\2\2\u024f\u024d\3\2\2\2\u0250")
        buf.write("\u0251\7^\2\2\u0251\u008c\3\2\2\2\u0252\u0253\7$\2\2\u0253")
        buf.write("\u008e\3\2\2\2\u0254\u0255\7)\2\2\u0255\u0090\3\2\2\2")
        buf.write("\u0256\u0258\t\13\2\2\u0257\u0256\3\2\2\2\u0258\u0259")
        buf.write("\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025b\u025c\bI\2\2\u025c\u0092\3\2\2\2")
        buf.write("\u025d\u0263\5\u008dG\2\u025e\u0262\n\7\2\2\u025f\u0260")
        buf.write("\7^\2\2\u0260\u0262\t\b\2\2\u0261\u025e\3\2\2\2\u0261")
        buf.write("\u025f\3\2\2\2\u0262\u0265\3\2\2\2\u0263\u0261\3\2\2\2")
        buf.write("\u0263\u0264\3\2\2\2\u0264\u0266\3\2\2\2\u0265\u0263\3")
        buf.write("\2\2\2\u0266\u0267\bJ\6\2\u0267\u0094\3\2\2\2\u0268\u026c")
        buf.write("\5\u008dG\2\u0269\u026b\n\7\2\2\u026a\u0269\3\2\2\2\u026b")
        buf.write("\u026e\3\2\2\2\u026c\u026a\3\2\2\2\u026c\u026d\3\2\2\2")
        buf.write("\u026d\u026f\3\2\2\2\u026e\u026c\3\2\2\2\u026f\u0270\t")
        buf.write("\2\2\2\u0270\u0271\bK\7\2\u0271\u0096\3\2\2\2\u0272\u0273")
        buf.write("\13\2\2\2\u0273\u0274\bL\b\2\u0274\u0098\3\2\2\2\35\2")
        buf.write("\u0116\u0121\u012e\u0135\u0139\u013d\u0141\u0146\u014b")
        buf.write("\u0150\u0152\u0158\u015c\u0161\u0163\u0165\u016b\u0171")
        buf.write("\u0173\u017f\u018c\u024d\u0259\u0261\u0263\u026c\t\b\2")
        buf.write("\2\3\17\2\3\20\3\3\22\4\3J\5\3K\6\3L\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    LINECMT = 12
    MULTLINECMT = 13
    INTLIT = 14
    FLOATLIT = 15
    BOOLLIT = 16
    STRINGLIT = 17
    ARRAYLIT = 18
    AUTO = 19
    BREAK = 20
    BOOLEAN = 21
    DO = 22
    ELSE = 23
    FALSE = 24
    FLOAT = 25
    FOR = 26
    FUNCTION = 27
    IF = 28
    INTEGER = 29
    RETURN = 30
    STRING = 31
    TRUE = 32
    WHILE = 33
    VOID = 34
    OUT = 35
    CONTINUE = 36
    OF = 37
    INHERIT = 38
    ARRAY = 39
    MAIN = 40
    ADD = 41
    SUB = 42
    MUL = 43
    DIV = 44
    MOD = 45
    NOT = 46
    AND = 47
    OR = 48
    EQ = 49
    NOT_EQ = 50
    LESS = 51
    LESS_OR_EQ = 52
    GREATER = 53
    GREATER_OR_EQ = 54
    STRING_CONCAT = 55
    LP = 56
    RP = 57
    LS = 58
    RS = 59
    LC = 60
    RC = 61
    COMMA = 62
    PERIOD = 63
    SEMI = 64
    COLON = 65
    ASSIGN = 66
    ID = 67
    BACKSLASH = 68
    DQUOTES = 69
    SQUOTE = 70
    WS = 71
    UNCLOSE_STRING = 72
    ILLEGAL_ESCAPE = 73
    ERROR_CHAR = 74

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{}'", "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBooolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'auto'", "'break'", "'boolean'", 
            "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
            "'if'", "'integer'", "'return'", "'string'", "'true'", "'while'", 
            "'void'", "'out'", "'continue'", "'of'", "'inherit'", "'array'", 
            "'main'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'.'", "';'", 
            "':'", "'='", "'\\'", "'\"'", "'''" ]

    symbolicNames = [ "<INVALID>",
            "LINECMT", "MULTLINECMT", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
            "ARRAYLIT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", 
            "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
            "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "MAIN", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
            "OR", "EQ", "NOT_EQ", "LESS", "LESS_OR_EQ", "GREATER", "GREATER_OR_EQ", 
            "STRING_CONCAT", "LP", "RP", "LS", "RS", "LC", "RC", "COMMA", 
            "PERIOD", "SEMI", "COLON", "ASSIGN", "ID", "BACKSLASH", "DQUOTES", 
            "SQUOTE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "LINECMT", "MULTLINECMT", 
                  "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ARRAYLIT", 
                  "EXPRESSION", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "MAIN", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQ", "NOT_EQ", "LESS", 
                  "LESS_OR_EQ", "GREATER", "GREATER_OR_EQ", "STRING_CONCAT", 
                  "LP", "RP", "LS", "RS", "LC", "RC", "COMMA", "PERIOD", 
                  "SEMI", "COLON", "ASSIGN", "ID", "BACKSLASH", "DQUOTES", 
                  "SQUOTE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[13] = self.INTLIT_action 
            actions[14] = self.FLOATLIT_action 
            actions[16] = self.STRINGLIT_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text=self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:]; raise UncloseString(self.text)
            		
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


