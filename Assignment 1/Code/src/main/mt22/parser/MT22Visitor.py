# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_func.
    def visitType_func(self, ctx:MT22Parser.Type_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_vardecl_noExpr.
    def visitType_vardecl_noExpr(self, ctx:MT22Parser.Type_vardecl_noExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_vardecl_withExpr.
    def visitType_vardecl_withExpr(self, ctx:MT22Parser.Type_vardecl_withExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraydeclWithExpr.
    def visitArraydeclWithExpr(self, ctx:MT22Parser.ArraydeclWithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclWithExpr.
    def visitVardeclWithExpr(self, ctx:MT22Parser.VardeclWithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#helpVardeclWithExpr.
    def visitHelpVardeclWithExpr(self, ctx:MT22Parser.HelpVardeclWithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclNoExpr.
    def visitVardeclNoExpr(self, ctx:MT22Parser.VardeclNoExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecls.
    def visitVardecls(self, ctx:MT22Parser.VardeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramdecl.
    def visitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecls.
    def visitFuncdecls(self, ctx:MT22Parser.FuncdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string.
    def visitString(self, ctx:MT22Parser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational.
    def visitRelational(self, ctx:MT22Parser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical1.
    def visitLogical1(self, ctx:MT22Parser.Logical1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arithmetic1.
    def visitArithmetic1(self, ctx:MT22Parser.Arithmetic1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arithmetic2.
    def visitArithmetic2(self, ctx:MT22Parser.Arithmetic2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical2.
    def visitLogical2(self, ctx:MT22Parser.Logical2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign.
    def visitSign(self, ctx:MT22Parser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index.
    def visitIndex(self, ctx:MT22Parser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#term.
    def visitTerm(self, ctx:MT22Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function.
    def visitFunction(self, ctx:MT22Parser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign.
    def visitAssign(self, ctx:MT22Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_.
    def visitIf_(self, ctx:MT22Parser.If_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_.
    def visitFor_(self, ctx:MT22Parser.For_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_.
    def visitWhile_(self, ctx:MT22Parser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while.
    def visitDo_while(self, ctx:MT22Parser.Do_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_.
    def visitBreak_(self, ctx:MT22Parser.Break_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_.
    def visitContinue_(self, ctx:MT22Parser.Continue_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_.
    def visitReturn_(self, ctx:MT22Parser.Return_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call.
    def visitCall(self, ctx:MT22Parser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_statement.
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_function.
    def visitSpecial_function(self, ctx:MT22Parser.Special_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_int.
    def visitRead_int(self, ctx:MT22Parser.Read_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_int.
    def visitPrint_int(self, ctx:MT22Parser.Print_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_float.
    def visitRead_float(self, ctx:MT22Parser.Read_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#write_float.
    def visitWrite_float(self, ctx:MT22Parser.Write_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_bool.
    def visitRead_bool(self, ctx:MT22Parser.Read_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_bool.
    def visitPrint_bool(self, ctx:MT22Parser.Print_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_string.
    def visitRead_string(self, ctx:MT22Parser.Read_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_string.
    def visitPrint_string(self, ctx:MT22Parser.Print_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#super_.
    def visitSuper_(self, ctx:MT22Parser.Super_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prevent_default.
    def visitPrevent_default(self, ctx:MT22Parser.Prevent_defaultContext):
        return self.visitChildren(ctx)



del MT22Parser