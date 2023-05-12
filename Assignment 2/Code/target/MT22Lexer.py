# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u025b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\7\3\u009d\n\3\f\3\16\3\u00a0\13\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\7\4\u00a8\n\4\f\4\16\4\u00ab\13")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5\u00b5\n\5\f\5\16")
        buf.write("\5\u00b8\13\5\3\5\3\5\6\5\u00bc\n\5\r\5\16\5\u00bd\7\5")
        buf.write("\u00c0\n\5\f\5\16\5\u00c3\13\5\3\5\5\5\u00c6\n\5\3\6\3")
        buf.write("\6\5\6\u00ca\n\6\3\6\7\6\u00cd\n\6\f\6\16\6\u00d0\13\6")
        buf.write("\3\6\3\6\5\6\u00d4\n\6\3\6\6\6\u00d7\n\6\r\6\16\6\u00d8")
        buf.write("\5\6\u00db\n\6\3\6\3\6\6\6\u00df\n\6\r\6\16\6\u00e0\3")
        buf.write("\6\3\6\5\6\u00e5\n\6\3\6\6\6\u00e8\n\6\r\6\16\6\u00e9")
        buf.write("\5\6\u00ec\n\6\5\6\u00ee\n\6\3\6\3\6\3\7\3\7\5\7\u00f4")
        buf.write("\n\7\3\b\3\b\3\b\3\b\7\b\u00fa\n\b\f\b\16\b\u00fd\13\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\39\39\3:\3:")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\7C\u0232\nC\fC\16C\u0235\13C\3D\3D\3E\3E\3F\3F\3G\6")
        buf.write("G\u023e\nG\rG\16G\u023f\3G\3G\3H\3H\3H\3H\7H\u0248\nH")
        buf.write("\fH\16H\u024b\13H\3H\3H\3I\3I\7I\u0251\nI\fI\16I\u0254")
        buf.write("\13I\3I\3I\3I\3J\3J\3J\3\u00a9\2K\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\3\2\f\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\2\u0272\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u0098\3\2\2")
        buf.write("\2\7\u00a3\3\2\2\2\t\u00c5\3\2\2\2\13\u00ed\3\2\2\2\r")
        buf.write("\u00f3\3\2\2\2\17\u00f5\3\2\2\2\21\u0101\3\2\2\2\23\u0106")
        buf.write("\3\2\2\2\25\u010c\3\2\2\2\27\u0114\3\2\2\2\31\u0117\3")
        buf.write("\2\2\2\33\u011c\3\2\2\2\35\u0122\3\2\2\2\37\u0128\3\2")
        buf.write("\2\2!\u012c\3\2\2\2#\u0135\3\2\2\2%\u0138\3\2\2\2\'\u0140")
        buf.write("\3\2\2\2)\u0147\3\2\2\2+\u014e\3\2\2\2-\u0153\3\2\2\2")
        buf.write("/\u0159\3\2\2\2\61\u015e\3\2\2\2\63\u0162\3\2\2\2\65\u016b")
        buf.write("\3\2\2\2\67\u016e\3\2\2\29\u0176\3\2\2\2;\u017c\3\2\2")
        buf.write("\2=\u0181\3\2\2\2?\u018d\3\2\2\2A\u019a\3\2\2\2C\u01a4")
        buf.write("\3\2\2\2E\u01af\3\2\2\2G\u01bb\3\2\2\2I\u01c8\3\2\2\2")
        buf.write("K\u01d3\3\2\2\2M\u01df\3\2\2\2O\u01e5\3\2\2\2Q\u01f4\3")
        buf.write("\2\2\2S\u01f6\3\2\2\2U\u01f8\3\2\2\2W\u01fa\3\2\2\2Y\u01fc")
        buf.write("\3\2\2\2[\u01fe\3\2\2\2]\u0200\3\2\2\2_\u0203\3\2\2\2")
        buf.write("a\u0206\3\2\2\2c\u0209\3\2\2\2e\u020c\3\2\2\2g\u020e\3")
        buf.write("\2\2\2i\u0211\3\2\2\2k\u0213\3\2\2\2m\u0216\3\2\2\2o\u0219")
        buf.write("\3\2\2\2q\u021b\3\2\2\2s\u021d\3\2\2\2u\u021f\3\2\2\2")
        buf.write("w\u0221\3\2\2\2y\u0223\3\2\2\2{\u0225\3\2\2\2}\u0227\3")
        buf.write("\2\2\2\177\u0229\3\2\2\2\u0081\u022b\3\2\2\2\u0083\u022d")
        buf.write("\3\2\2\2\u0085\u022f\3\2\2\2\u0087\u0236\3\2\2\2\u0089")
        buf.write("\u0238\3\2\2\2\u008b\u023a\3\2\2\2\u008d\u023d\3\2\2\2")
        buf.write("\u008f\u0243\3\2\2\2\u0091\u024e\3\2\2\2\u0093\u0258\3")
        buf.write("\2\2\2\u0095\u0096\7}\2\2\u0096\u0097\7\177\2\2\u0097")
        buf.write("\4\3\2\2\2\u0098\u0099\7\61\2\2\u0099\u009a\7\61\2\2\u009a")
        buf.write("\u009e\3\2\2\2\u009b\u009d\n\2\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3")
        buf.write("\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2")
        buf.write("\b\3\2\2\u00a2\6\3\2\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5")
        buf.write("\7,\2\2\u00a5\u00a9\3\2\2\2\u00a6\u00a8\13\2\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3")
        buf.write("\2\2\2\u00ac\u00ad\7,\2\2\u00ad\u00ae\7\61\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b0\b\4\2\2\u00b0\b\3\2\2\2\u00b1\u00c6")
        buf.write("\7\62\2\2\u00b2\u00b6\t\3\2\2\u00b3\u00b5\t\4\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00c1\3\2\2\2\u00b8\u00b6\3")
        buf.write("\2\2\2\u00b9\u00bb\7a\2\2\u00ba\u00bc\t\4\2\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00b9\3\2\2\2")
        buf.write("\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c6")
        buf.write("\b\5\3\2\u00c5\u00b1\3\2\2\2\u00c5\u00b2\3\2\2\2\u00c6")
        buf.write("\n\3\2\2\2\u00c7\u00c9\5\t\5\2\u00c8\u00ca\7\60\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00ce\3\2\2\2")
        buf.write("\u00cb\u00cd\t\4\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00d0\3")
        buf.write("\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00da")
        buf.write("\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d3\t\5\2\2\u00d2")
        buf.write("\u00d4\t\6\2\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\u00d6\3\2\2\2\u00d5\u00d7\t\4\2\2\u00d6\u00d5\3")
        buf.write("\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00d1\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00ee\3\2\2\2\u00dc\u00de\7\60\2")
        buf.write("\2\u00dd\u00df\t\4\2\2\u00de\u00dd\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write("\u00eb\3\2\2\2\u00e2\u00e4\t\5\2\2\u00e3\u00e5\t\6\2\2")
        buf.write("\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e7\3")
        buf.write("\2\2\2\u00e6\u00e8\t\4\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00ec\3\2\2\2\u00eb\u00e2\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00ee\3\2\2\2\u00ed\u00c7\3\2\2\2\u00ed\u00dc\3")
        buf.write("\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\b\6\4\2\u00f0\f")
        buf.write("\3\2\2\2\u00f1\u00f4\5+\26\2\u00f2\u00f4\5\33\16\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\16\3\2\2\2\u00f5")
        buf.write("\u00fb\5\u0089E\2\u00f6\u00fa\n\7\2\2\u00f7\u00f8\7^\2")
        buf.write("\2\u00f8\u00fa\t\b\2\2\u00f9\u00f6\3\2\2\2\u00f9\u00f7")
        buf.write("\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fe\u00ff\5\u0089E\2\u00ff\u0100\b\b\5\2\u0100\20\3")
        buf.write("\2\2\2\u0101\u0102\7c\2\2\u0102\u0103\7w\2\2\u0103\u0104")
        buf.write("\7v\2\2\u0104\u0105\7q\2\2\u0105\22\3\2\2\2\u0106\u0107")
        buf.write("\7d\2\2\u0107\u0108\7t\2\2\u0108\u0109\7g\2\2\u0109\u010a")
        buf.write("\7c\2\2\u010a\u010b\7m\2\2\u010b\24\3\2\2\2\u010c\u010d")
        buf.write("\7d\2\2\u010d\u010e\7q\2\2\u010e\u010f\7q\2\2\u010f\u0110")
        buf.write("\7n\2\2\u0110\u0111\7g\2\2\u0111\u0112\7c\2\2\u0112\u0113")
        buf.write("\7p\2\2\u0113\26\3\2\2\2\u0114\u0115\7f\2\2\u0115\u0116")
        buf.write("\7q\2\2\u0116\30\3\2\2\2\u0117\u0118\7g\2\2\u0118\u0119")
        buf.write("\7n\2\2\u0119\u011a\7u\2\2\u011a\u011b\7g\2\2\u011b\32")
        buf.write("\3\2\2\2\u011c\u011d\7h\2\2\u011d\u011e\7c\2\2\u011e\u011f")
        buf.write("\7n\2\2\u011f\u0120\7u\2\2\u0120\u0121\7g\2\2\u0121\34")
        buf.write("\3\2\2\2\u0122\u0123\7h\2\2\u0123\u0124\7n\2\2\u0124\u0125")
        buf.write("\7q\2\2\u0125\u0126\7c\2\2\u0126\u0127\7v\2\2\u0127\36")
        buf.write("\3\2\2\2\u0128\u0129\7h\2\2\u0129\u012a\7q\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b \3\2\2\2\u012c\u012d\7h\2\2\u012d\u012e")
        buf.write("\7w\2\2\u012e\u012f\7p\2\2\u012f\u0130\7e\2\2\u0130\u0131")
        buf.write("\7v\2\2\u0131\u0132\7k\2\2\u0132\u0133\7q\2\2\u0133\u0134")
        buf.write("\7p\2\2\u0134\"\3\2\2\2\u0135\u0136\7k\2\2\u0136\u0137")
        buf.write("\7h\2\2\u0137$\3\2\2\2\u0138\u0139\7k\2\2\u0139\u013a")
        buf.write("\7p\2\2\u013a\u013b\7v\2\2\u013b\u013c\7g\2\2\u013c\u013d")
        buf.write("\7i\2\2\u013d\u013e\7g\2\2\u013e\u013f\7t\2\2\u013f&\3")
        buf.write("\2\2\2\u0140\u0141\7t\2\2\u0141\u0142\7g\2\2\u0142\u0143")
        buf.write("\7v\2\2\u0143\u0144\7w\2\2\u0144\u0145\7t\2\2\u0145\u0146")
        buf.write("\7p\2\2\u0146(\3\2\2\2\u0147\u0148\7u\2\2\u0148\u0149")
        buf.write("\7v\2\2\u0149\u014a\7t\2\2\u014a\u014b\7k\2\2\u014b\u014c")
        buf.write("\7p\2\2\u014c\u014d\7i\2\2\u014d*\3\2\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014f\u0150\7t\2\2\u0150\u0151\7w\2\2\u0151\u0152")
        buf.write("\7g\2\2\u0152,\3\2\2\2\u0153\u0154\7y\2\2\u0154\u0155")
        buf.write("\7j\2\2\u0155\u0156\7k\2\2\u0156\u0157\7n\2\2\u0157\u0158")
        buf.write("\7g\2\2\u0158.\3\2\2\2\u0159\u015a\7x\2\2\u015a\u015b")
        buf.write("\7q\2\2\u015b\u015c\7k\2\2\u015c\u015d\7f\2\2\u015d\60")
        buf.write("\3\2\2\2\u015e\u015f\7q\2\2\u015f\u0160\7w\2\2\u0160\u0161")
        buf.write("\7v\2\2\u0161\62\3\2\2\2\u0162\u0163\7e\2\2\u0163\u0164")
        buf.write("\7q\2\2\u0164\u0165\7p\2\2\u0165\u0166\7v\2\2\u0166\u0167")
        buf.write("\7k\2\2\u0167\u0168\7p\2\2\u0168\u0169\7w\2\2\u0169\u016a")
        buf.write("\7g\2\2\u016a\64\3\2\2\2\u016b\u016c\7q\2\2\u016c\u016d")
        buf.write("\7h\2\2\u016d\66\3\2\2\2\u016e\u016f\7k\2\2\u016f\u0170")
        buf.write("\7p\2\2\u0170\u0171\7j\2\2\u0171\u0172\7g\2\2\u0172\u0173")
        buf.write("\7t\2\2\u0173\u0174\7k\2\2\u0174\u0175\7v\2\2\u01758\3")
        buf.write("\2\2\2\u0176\u0177\7c\2\2\u0177\u0178\7t\2\2\u0178\u0179")
        buf.write("\7t\2\2\u0179\u017a\7c\2\2\u017a\u017b\7{\2\2\u017b:\3")
        buf.write("\2\2\2\u017c\u017d\7o\2\2\u017d\u017e\7c\2\2\u017e\u017f")
        buf.write("\7k\2\2\u017f\u0180\7p\2\2\u0180<\3\2\2\2\u0181\u0182")
        buf.write("\7t\2\2\u0182\u0183\7g\2\2\u0183\u0184\7c\2\2\u0184\u0185")
        buf.write("\7f\2\2\u0185\u0186\7K\2\2\u0186\u0187\7p\2\2\u0187\u0188")
        buf.write("\7v\2\2\u0188\u0189\7g\2\2\u0189\u018a\7i\2\2\u018a\u018b")
        buf.write("\7g\2\2\u018b\u018c\7t\2\2\u018c>\3\2\2\2\u018d\u018e")
        buf.write("\7r\2\2\u018e\u018f\7t\2\2\u018f\u0190\7k\2\2\u0190\u0191")
        buf.write("\7p\2\2\u0191\u0192\7v\2\2\u0192\u0193\7K\2\2\u0193\u0194")
        buf.write("\7p\2\2\u0194\u0195\7v\2\2\u0195\u0196\7g\2\2\u0196\u0197")
        buf.write("\7i\2\2\u0197\u0198\7g\2\2\u0198\u0199\7t\2\2\u0199@\3")
        buf.write("\2\2\2\u019a\u019b\7t\2\2\u019b\u019c\7g\2\2\u019c\u019d")
        buf.write("\7c\2\2\u019d\u019e\7f\2\2\u019e\u019f\7H\2\2\u019f\u01a0")
        buf.write("\7n\2\2\u01a0\u01a1\7q\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3")
        buf.write("\7v\2\2\u01a3B\3\2\2\2\u01a4\u01a5\7y\2\2\u01a5\u01a6")
        buf.write("\7t\2\2\u01a6\u01a7\7k\2\2\u01a7\u01a8\7v\2\2\u01a8\u01a9")
        buf.write("\7g\2\2\u01a9\u01aa\7H\2\2\u01aa\u01ab\7n\2\2\u01ab\u01ac")
        buf.write("\7q\2\2\u01ac\u01ad\7c\2\2\u01ad\u01ae\7v\2\2\u01aeD\3")
        buf.write("\2\2\2\u01af\u01b0\7t\2\2\u01b0\u01b1\7g\2\2\u01b1\u01b2")
        buf.write("\7c\2\2\u01b2\u01b3\7f\2\2\u01b3\u01b4\7D\2\2\u01b4\u01b5")
        buf.write("\7q\2\2\u01b5\u01b6\7q\2\2\u01b6\u01b7\7n\2\2\u01b7\u01b8")
        buf.write("\7g\2\2\u01b8\u01b9\7c\2\2\u01b9\u01ba\7p\2\2\u01baF\3")
        buf.write("\2\2\2\u01bb\u01bc\7r\2\2\u01bc\u01bd\7t\2\2\u01bd\u01be")
        buf.write("\7k\2\2\u01be\u01bf\7p\2\2\u01bf\u01c0\7v\2\2\u01c0\u01c1")
        buf.write("\7D\2\2\u01c1\u01c2\7q\2\2\u01c2\u01c3\7q\2\2\u01c3\u01c4")
        buf.write("\7n\2\2\u01c4\u01c5\7g\2\2\u01c5\u01c6\7c\2\2\u01c6\u01c7")
        buf.write("\7p\2\2\u01c7H\3\2\2\2\u01c8\u01c9\7t\2\2\u01c9\u01ca")
        buf.write("\7g\2\2\u01ca\u01cb\7c\2\2\u01cb\u01cc\7f\2\2\u01cc\u01cd")
        buf.write("\7U\2\2\u01cd\u01ce\7v\2\2\u01ce\u01cf\7t\2\2\u01cf\u01d0")
        buf.write("\7k\2\2\u01d0\u01d1\7p\2\2\u01d1\u01d2\7i\2\2\u01d2J\3")
        buf.write("\2\2\2\u01d3\u01d4\7r\2\2\u01d4\u01d5\7t\2\2\u01d5\u01d6")
        buf.write("\7k\2\2\u01d6\u01d7\7p\2\2\u01d7\u01d8\7v\2\2\u01d8\u01d9")
        buf.write("\7U\2\2\u01d9\u01da\7v\2\2\u01da\u01db\7t\2\2\u01db\u01dc")
        buf.write("\7k\2\2\u01dc\u01dd\7p\2\2\u01dd\u01de\7i\2\2\u01deL\3")
        buf.write("\2\2\2\u01df\u01e0\7u\2\2\u01e0\u01e1\7w\2\2\u01e1\u01e2")
        buf.write("\7r\2\2\u01e2\u01e3\7g\2\2\u01e3\u01e4\7t\2\2\u01e4N\3")
        buf.write("\2\2\2\u01e5\u01e6\7r\2\2\u01e6\u01e7\7t\2\2\u01e7\u01e8")
        buf.write("\7g\2\2\u01e8\u01e9\7x\2\2\u01e9\u01ea\7g\2\2\u01ea\u01eb")
        buf.write("\7p\2\2\u01eb\u01ec\7v\2\2\u01ec\u01ed\7F\2\2\u01ed\u01ee")
        buf.write("\7g\2\2\u01ee\u01ef\7h\2\2\u01ef\u01f0\7c\2\2\u01f0\u01f1")
        buf.write("\7w\2\2\u01f1\u01f2\7n\2\2\u01f2\u01f3\7v\2\2\u01f3P\3")
        buf.write("\2\2\2\u01f4\u01f5\7-\2\2\u01f5R\3\2\2\2\u01f6\u01f7\7")
        buf.write("/\2\2\u01f7T\3\2\2\2\u01f8\u01f9\7,\2\2\u01f9V\3\2\2\2")
        buf.write("\u01fa\u01fb\7\61\2\2\u01fbX\3\2\2\2\u01fc\u01fd\7\'\2")
        buf.write("\2\u01fdZ\3\2\2\2\u01fe\u01ff\7#\2\2\u01ff\\\3\2\2\2\u0200")
        buf.write("\u0201\7(\2\2\u0201\u0202\7(\2\2\u0202^\3\2\2\2\u0203")
        buf.write("\u0204\7~\2\2\u0204\u0205\7~\2\2\u0205`\3\2\2\2\u0206")
        buf.write("\u0207\7?\2\2\u0207\u0208\7?\2\2\u0208b\3\2\2\2\u0209")
        buf.write("\u020a\7#\2\2\u020a\u020b\7?\2\2\u020bd\3\2\2\2\u020c")
        buf.write("\u020d\7>\2\2\u020df\3\2\2\2\u020e\u020f\7>\2\2\u020f")
        buf.write("\u0210\7?\2\2\u0210h\3\2\2\2\u0211\u0212\7@\2\2\u0212")
        buf.write("j\3\2\2\2\u0213\u0214\7@\2\2\u0214\u0215\7?\2\2\u0215")
        buf.write("l\3\2\2\2\u0216\u0217\7<\2\2\u0217\u0218\7<\2\2\u0218")
        buf.write("n\3\2\2\2\u0219\u021a\7*\2\2\u021ap\3\2\2\2\u021b\u021c")
        buf.write("\7+\2\2\u021cr\3\2\2\2\u021d\u021e\7]\2\2\u021et\3\2\2")
        buf.write("\2\u021f\u0220\7_\2\2\u0220v\3\2\2\2\u0221\u0222\7}\2")
        buf.write("\2\u0222x\3\2\2\2\u0223\u0224\7\177\2\2\u0224z\3\2\2\2")
        buf.write("\u0225\u0226\7.\2\2\u0226|\3\2\2\2\u0227\u0228\7\60\2")
        buf.write("\2\u0228~\3\2\2\2\u0229\u022a\7=\2\2\u022a\u0080\3\2\2")
        buf.write("\2\u022b\u022c\7<\2\2\u022c\u0082\3\2\2\2\u022d\u022e")
        buf.write("\7?\2\2\u022e\u0084\3\2\2\2\u022f\u0233\t\t\2\2\u0230")
        buf.write("\u0232\t\n\2\2\u0231\u0230\3\2\2\2\u0232\u0235\3\2\2\2")
        buf.write("\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0086\3")
        buf.write("\2\2\2\u0235\u0233\3\2\2\2\u0236\u0237\7^\2\2\u0237\u0088")
        buf.write("\3\2\2\2\u0238\u0239\7$\2\2\u0239\u008a\3\2\2\2\u023a")
        buf.write("\u023b\7)\2\2\u023b\u008c\3\2\2\2\u023c\u023e\t\13\2\2")
        buf.write("\u023d\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u023d\3")
        buf.write("\2\2\2\u023f\u0240\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0242")
        buf.write("\bG\2\2\u0242\u008e\3\2\2\2\u0243\u0249\5\u0089E\2\u0244")
        buf.write("\u0248\n\7\2\2\u0245\u0246\7^\2\2\u0246\u0248\t\b\2\2")
        buf.write("\u0247\u0244\3\2\2\2\u0247\u0245\3\2\2\2\u0248\u024b\3")
        buf.write("\2\2\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024c")
        buf.write("\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024d\bH\6\2\u024d")
        buf.write("\u0090\3\2\2\2\u024e\u0252\5\u0089E\2\u024f\u0251\n\7")
        buf.write("\2\2\u0250\u024f\3\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250")
        buf.write("\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0255\3\2\2\2\u0254")
        buf.write("\u0252\3\2\2\2\u0255\u0256\t\2\2\2\u0256\u0257\bI\7\2")
        buf.write("\u0257\u0092\3\2\2\2\u0258\u0259\13\2\2\2\u0259\u025a")
        buf.write("\bJ\b\2\u025a\u0094\3\2\2\2\33\2\u009e\u00a9\u00b6\u00bd")
        buf.write("\u00c1\u00c5\u00c9\u00ce\u00d3\u00d8\u00da\u00e0\u00e4")
        buf.write("\u00e9\u00eb\u00ed\u00f3\u00f9\u00fb\u0233\u023f\u0247")
        buf.write("\u0249\u0252\t\b\2\2\3\5\2\3\6\3\3\b\4\3H\5\3I\6\3J\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EMPTY_BODY = 1
    LINECMT = 2
    MULTLINECMT = 3
    INTLIT = 4
    FLOATLIT = 5
    BOOLLIT = 6
    STRINGLIT = 7
    AUTO = 8
    BREAK = 9
    BOOLEAN = 10
    DO = 11
    ELSE = 12
    FALSE = 13
    FLOAT = 14
    FOR = 15
    FUNCTION = 16
    IF = 17
    INTEGER = 18
    RETURN = 19
    STRING = 20
    TRUE = 21
    WHILE = 22
    VOID = 23
    OUT = 24
    CONTINUE = 25
    OF = 26
    INHERIT = 27
    ARRAY = 28
    MAIN = 29
    READINT = 30
    PRINTINT = 31
    READFLOAT = 32
    WRITEFLOAT = 33
    READBOOL = 34
    PRINTBOOL = 35
    READSTRING = 36
    PRINTSTRING = 37
    SUPER = 38
    PREVENTDEFAULT = 39
    ADD = 40
    SUB = 41
    MUL = 42
    DIV = 43
    MOD = 44
    NOT = 45
    AND = 46
    OR = 47
    EQ = 48
    NOT_EQ = 49
    LESS = 50
    LESS_OR_EQ = 51
    GREATER = 52
    GREATER_OR_EQ = 53
    STRING_CONCAT = 54
    LP = 55
    RP = 56
    LS = 57
    RS = 58
    LC = 59
    RC = 60
    COMMA = 61
    PERIOD = 62
    SEMI = 63
    COLON = 64
    ASSIGN = 65
    ID = 66
    BACKSLASH = 67
    DQUOTES = 68
    SQUOTE = 69
    WS = 70
    UNCLOSE_STRING = 71
    ILLEGAL_ESCAPE = 72
    ERROR_CHAR = 73

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{}'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
            "'false'", "'float'", "'for'", "'function'", "'if'", "'integer'", 
            "'return'", "'string'", "'true'", "'while'", "'void'", "'out'", 
            "'continue'", "'of'", "'inherit'", "'array'", "'main'", "'readInteger'", 
            "'printInteger'", "'readFloat'", "'writeFloat'", "'readBoolean'", 
            "'printBoolean'", "'readString'", "'printString'", "'super'", 
            "'preventDefault'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'.'", 
            "';'", "':'", "'='", "'\\'", "'\"'", "'''" ]

    symbolicNames = [ "<INVALID>",
            "EMPTY_BODY", "LINECMT", "MULTLINECMT", "INTLIT", "FLOATLIT", 
            "BOOLLIT", "STRINGLIT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
            "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
            "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", 
            "INHERIT", "ARRAY", "MAIN", "READINT", "PRINTINT", "READFLOAT", 
            "WRITEFLOAT", "READBOOL", "PRINTBOOL", "READSTRING", "PRINTSTRING", 
            "SUPER", "PREVENTDEFAULT", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "EQ", "NOT_EQ", "LESS", "LESS_OR_EQ", "GREATER", 
            "GREATER_OR_EQ", "STRING_CONCAT", "LP", "RP", "LS", "RS", "LC", 
            "RC", "COMMA", "PERIOD", "SEMI", "COLON", "ASSIGN", "ID", "BACKSLASH", 
            "DQUOTES", "SQUOTE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "EMPTY_BODY", "LINECMT", "MULTLINECMT", "INTLIT", "FLOATLIT", 
                  "BOOLLIT", "STRINGLIT", "AUTO", "BREAK", "BOOLEAN", "DO", 
                  "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "MAIN", "READINT", "PRINTINT", 
                  "READFLOAT", "WRITEFLOAT", "READBOOL", "PRINTBOOL", "READSTRING", 
                  "PRINTSTRING", "SUPER", "PREVENTDEFAULT", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", "NOT_EQ", 
                  "LESS", "LESS_OR_EQ", "GREATER", "GREATER_OR_EQ", "STRING_CONCAT", 
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
            actions[3] = self.INTLIT_action 
            actions[4] = self.FLOATLIT_action 
            actions[6] = self.STRINGLIT_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.ERROR_CHAR_action 
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
     


