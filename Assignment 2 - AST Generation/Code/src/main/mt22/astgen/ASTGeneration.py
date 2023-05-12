from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    ######################### Program #########################
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()) if ctx.decls() else [])
    ######################### Program #########################

    ######################### Declarations #########################
    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        if (ctx.decls()):
            if ctx.vardecl():
                return self.visit(ctx.vardecl())+self.visit(ctx.decls())
            else:
                return [self.visit(ctx.funcdecl())]+self.visit(ctx.decls())
        else:
            if ctx.vardecl():
                return self.visit(ctx.vardecl())
            else:
                return [self.visit(ctx.funcdecl())]
    ######################### Declarations #########################

    ######################### IDlist #########################
    def visitInt_list(self, ctx: MT22Parser.Int_listContext):
        return [IntegerLit(int(ctx.INTLIT().getText()))] + ([] if ctx.getChildCount() == 1 else self.visit(ctx.int_list()))

    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        return [ctx.ID().getText()] + ([] if ctx.getChildCount() == 1 else self.visit(ctx.idlist()))
    ######################### IDlist #########################

    ######################### Types #########################
    def visitType_vardecl_no_expr(self, ctx: MT22Parser.Type_vardecl_no_exprContext):
        if ctx.ARRAY():
            type = StringType()
            if ctx.BOOLEAN():
                type = BooleanType()
            elif ctx.FLOAT():
                type = FloatType()
            elif ctx.INTEGER():
                type = IntegerType()
            intlist = self.visit(ctx.int_list())
            return ArrayType(intlist, type)
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.STRING():
            return StringType()
        else:
            return AutoType()

    def visitType_vardecl_with_expr(self, ctx: MT22Parser.Type_vardecl_with_exprContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.STRING():
            return StringType()
        else:
            return AutoType()

    def visitType_func(self, ctx: MT22Parser.Type_funcContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        else:
            return VoidType()
    ######################### Types #########################

    ######################### Variable declaration #########################
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if (ctx.vardecl_with_expr()):
            return self.visit(ctx.vardecl_with_expr())
        elif (ctx.vardecl_no_expr()):
            return self.visit(ctx.vardecl_no_expr())
        elif (ctx.arraydecl_with_expr()):
            return self.visit(ctx.arraydecl_with_expr())
        else:
            return self.visit(ctx.arraydecl_no_expr())

    def visitVardecl_with_expr(self, ctx: MT22Parser.Vardecl_with_exprContext):
        idlist = self.visit(ctx.idlist())
        type = self.visit(ctx.type_vardecl_with_expr())
        expression = self.visit(ctx.expression_list())
        return list(map(lambda x, y: VarDecl(x, type, y), idlist, expression))

    def visitVardecl_no_expr(self, ctx: MT22Parser.Vardecl_no_exprContext):
        type = self.visit(ctx.type_vardecl_no_expr())
        idlist = self.visit(ctx.idlist())
        return list(map(lambda x: VarDecl(x, type), idlist))

    ######################### Variable declaration #########################

    ######################### Array declaration #########################
    def visitArraydecl_with_expr(self, ctx: MT22Parser.Arraydecl_with_exprContext):
        idlist = self.visit(ctx.idlist())
        intlist = self.visit(ctx.int_list()) if ctx.int_list() else []
        type = StringType()
        if ctx.BOOLEAN():
            type = BooleanType()
        elif ctx.FLOAT():
            type = FloatType()
        elif ctx.INTEGER():
            type = IntegerType()
        arraytype = ArrayType(intlist, type)
        values = self.visit(ctx.array_expression_list1())
        return [VarDecl(idlist[i], arraytype, values[i]) for i in range(0, len(idlist))]

    def visitArray_expression_list1(self, ctx: MT22Parser.Array_expression_list1Context):
        if ctx.getChildCount() == 3:
            return [ArrayLit(self.visit(ctx.array_expression1()))]
        return [ArrayLit(self.visit(ctx.array_expression1()))]+self.visit(ctx.array_expression_list1())

    def visitArray_expression1(self, ctx: MT22Parser.Array_expression1Context):
        if ctx.COMMA():
            return self.visit(ctx.array_expression1(0))+self.visit(ctx.array_expression1(1))
        elif ctx.LC() and ctx.RC():
            return [ArrayLit(self.visit(ctx.array_expression1(0)))]
        else:
            return self.visit(ctx.expression_list())

    def visitArraydecl_no_expr(self, ctx: MT22Parser.Arraydecl_no_exprContext):
        idlist = self.visit(ctx.idlist())
        intlist = self.visit(ctx.int_list())
        type = StringType()
        if ctx.BOOLEAN():
            type = BooleanType()
        elif ctx.FLOAT():
            type = FloatType()
        elif ctx.INTEGER():
            type = IntegerType()
        arraytype = ArrayType(intlist, type)
        values = self.visit(ctx.array_expression_list2())
        return [VarDecl(idlist[i], arraytype, values[i]) for i in range(0, len(idlist))]

    def visitArray_expression_list2(self, ctx: MT22Parser.Array_expression_list2Context):
        if ctx.getChildCount() == 5:
            return [ArrayLit(self.visit(ctx.array_expression2()))] + self.visit(ctx.array_expression_list2())
        elif ctx.getChildCount() == 3 and ctx.array_expression_list2():
            return [ArrayLit([])] + self.visit(ctx.array_expression_list2())
        elif ctx.getChildCount() == 3 and ctx.array_expression2():
            return [ArrayLit(self.visit(ctx.array_expression2()))]
        else:
            return [ArrayLit([])]

    def visitArray_expression2(self, ctx: MT22Parser.Array_expression2Context):
        if ctx.COMMA():
            return self.visit(ctx.array_expression2(0))+self.visit(ctx.array_expression2(1))
        elif ctx.getChildCount() == 3 and ctx.LC() and ctx.RC():
            return [ArrayLit(self.visit(ctx.array_expression2(0)))]
        elif ctx.EMPTY_BODY() or ctx.getChildCount() == 2:
            return [ArrayLit([])]
        else:
            return self.visit(ctx.expression_list())
    ######################### Array declaration #########################

    ######################### Parameters declaration #########################
    def visitParam_list(self, ctx: MT22Parser.Param_listContext):
        if ctx.param_list():
            return [self.visit(ctx.paramdecl())]+self.visit(ctx.param_list())
        return [self.visit(ctx.paramdecl())]

    def visitParamdecl(self, ctx: MT22Parser.ParamdeclContext):
        inherit = True if ctx.INHERIT() else False
        out = True if ctx.OUT() else False
        name = ctx.ID().getText()
        type = self.visit(ctx.type_vardecl_no_expr())
        return ParamDecl(name, type, out, inherit)
    ######################### Parameters declaration #########################

    ######################### Function declaration #########################
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        name = ctx.ID().getText() if ctx.ID() else ctx.MAIN().getText()
        type = self.visit(ctx.type_func())
        param = self.visit(ctx.param_list()) if ctx.param_list() else []
        inherit = self.visit(ctx.inherit()) if ctx.inherit() else None
        body = self.visit(ctx.block_statement())
        return FuncDecl(name, type, param, inherit, body)

    def visitInherit(self, ctx: MT22Parser.InheritContext):
        return ctx.ID().getText()
    ######################### Function declaration #########################

    ######################### Expressions #########################
    def visitExpression_list(self, ctx: MT22Parser.Expression_listContext):
        if ctx.expression_list():
            return [self.visit(ctx.expression())]+self.visit(ctx.expression_list())
        return [self.visit(ctx.expression())]

    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        return self.visit(ctx.string())

    def visitString(self, ctx: MT22Parser.StringContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.STRING_CONCAT().getText(), self.visit(ctx.relational(0)), self.visit(ctx.relational(1)))
        else:
            return self.visit(ctx.relational(0))

    def visitRelational(self, ctx: MT22Parser.RelationalContext):
        if ctx.getChildCount() == 3:
            if ctx.EQ():
                return BinExpr(ctx.EQ().getText(), self.visit(ctx.logical1(0)), self.visit(ctx.logical1(1)))
            elif ctx.NOT_EQ():
                return BinExpr(ctx.NOT_EQ().getText(), self.visit(ctx.logical1(0)), self.visit(ctx.logical1(1)))
            elif ctx.LESS():
                return BinExpr(ctx.LESS().getText(), self.visit(ctx.logical1(0)), self.visit(ctx.logical1(1)))
            elif ctx.LESS_OR_EQ():
                return BinExpr(ctx.LESS_OR_EQ().getText(), self.visit(ctx.logical1(0)), self.visit(ctx.logical1(1)))
            elif ctx.GREATER():
                return BinExpr(ctx.GREATER().getText(), self.visit(ctx.logical1(0)), self.visit(ctx.logical1(1)))
            else:
                return BinExpr(ctx.GREATER_OR_EQ().getText(), self.visit(ctx.logical1(0)), self.visit(ctx.logical1(1)))
        else:
            return self.visit(ctx.logical1(0))

    def visitLogical1(self, ctx: MT22Parser.Logical1Context):
        if ctx.getChildCount() == 3:
            if ctx.AND():
                return BinExpr(ctx.AND().getText(), self.visit(ctx.logical1()), self.visit(ctx.arithmetic1()))
            else:
                return BinExpr(ctx.OR().getText(), self.visit(ctx.logical1()), self.visit(ctx.arithmetic1()))
        else:
            return self.visit(ctx.arithmetic1())

    def visitArithmetic1(self, ctx: MT22Parser.Arithmetic1Context):
        if ctx.getChildCount() == 3:
            if ctx.ADD():
                return BinExpr(ctx.ADD().getText(), self.visit(ctx.arithmetic1()), self.visit(ctx.arithmetic2()))
            else:
                return BinExpr(ctx.SUB().getText(), self.visit(ctx.arithmetic1()), self.visit(ctx.arithmetic2()))
        else:
            return self.visit(ctx.arithmetic2())

    def visitArithmetic2(self, ctx: MT22Parser.Arithmetic2Context):
        if ctx.getChildCount() == 3:
            if ctx.MUL():
                return BinExpr(ctx.MUL().getText(), self.visit(ctx.arithmetic2()), self.visit(ctx.logical2()))
            elif ctx.DIV():
                return BinExpr(ctx.DIV().getText(), self.visit(ctx.arithmetic2()), self.visit(ctx.logical2()))
            else:
                return BinExpr(ctx.MOD().getText(), self.visit(ctx.arithmetic2()), self.visit(ctx.logical2()))
        else:
            return self.visit(ctx.logical2())

    def visitLogical2(self, ctx: MT22Parser.Logical2Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.NOT().getText(), self.visit(ctx.logical2()))
        else:
            return self.visit(ctx.sign())

    def visitSign(self, ctx: MT22Parser.SignContext):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.SUB().getText(), self.visit(ctx.sign()))
        else:
            return self.visit(ctx.index())

    def visitIndex(self, ctx: MT22Parser.IndexContext):
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.index()), [self.visit(ctx.expression())])
        else:
            return self.visit(ctx.term())

    def visitTerm(self, ctx: MT22Parser.TermContext):
        if ctx.BOOLLIT():
            return BooleanLit(eval(ctx.BOOLLIT().getText().capitalize()))
        elif ctx.INTLIT():
            return IntegerLit(eval(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(eval(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.function():
            return self.visit(ctx.function())
        else:
            return self.visit(ctx.expression())

    def visitFunction(self, ctx: MT22Parser.FunctionContext):
        if ctx.special_function():
            name,arg=self.visit(ctx.special_function())
            return FuncCall(name,arg)
        return FuncCall(ctx.ID().getText(), self.visit(ctx.expression_list()) if ctx.expression_list() else [])
    ######################### Expressions #########################

    ######################### Statements #########################
    def visitStatements(self, ctx: MT22Parser.StatementsContext):
        if ctx.statements():
            return self.visit(ctx.statement())+self.visit(ctx.statements())
        return self.visit(ctx.statement())

    def visitStatement(self, ctx: MT22Parser.StatementContext):
        if ctx.assign():
            return self.visit(ctx.assign())
        elif ctx.if_():
            return self.visit(ctx.if_())
        elif ctx.for_():
            return self.visit(ctx.for_())
        elif ctx.while_():
            return self.visit(ctx.while_())
        elif ctx.do_while():
            return self.visit(ctx.do_while())
        elif ctx.break_():
            return self.visit(ctx.break_())
        elif ctx.continue_():
            return self.visit(ctx.continue_())
        elif ctx.return_():
            return self.visit(ctx.return_())
        elif ctx.block_statement():
            return self.visit(ctx.block_statement())
        else:
            return self.visit(ctx.call())

    def visitAssign(self, ctx: MT22Parser.AssignContext):
        return AssignStmt(Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.index()), self.visit(ctx.expression()))

    def visitIf_(self, ctx: MT22Parser.If_Context):
        exp = self.visit(ctx.expression())
        tstmt = None
        fstmt = None
        if len(ctx.SEMI()) == 1:
            if ctx.getChild(4) is not ctx.SEMI(0):
                tstmt = self.visit(ctx.statement(0))
            elif ctx.ELSE():
                fstmt = self.visit(ctx.statement(0))
        if len(ctx.SEMI()) == 0:
            tstmt = self.visit(ctx.statement(0))
            if ctx.ELSE():
                fstmt = self.visit(ctx.statement(1))
        return IfStmt(exp, tstmt, fstmt)

    def visitFor_(self, ctx: MT22Parser.For_Context):
        return ForStmt(self.visit(ctx.assign()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)), None if ctx.SEMI() else self.visit(ctx.statement()))

    def visitWhile_(self, ctx: MT22Parser.While_Context):
        return WhileStmt(self.visit(ctx.expression()), None if ctx.SEMI() else self.visit(ctx.statement()))

    def visitDo_while(self, ctx: MT22Parser.Do_whileContext):
        return DoWhileStmt(self.visit(ctx.expression()), self.visit(ctx.block_statement()))

    def visitBreak_(self, ctx: MT22Parser.Break_Context):
        return BreakStmt()

    def visitContinue_(self, ctx: MT22Parser.Continue_Context):
        return ContinueStmt()

    def visitReturn_(self, ctx: MT22Parser.Return_Context):
        return ReturnStmt(self.visit(ctx.expression()) if ctx.expression() else None)

    def visitCall(self, ctx: MT22Parser.CallContext):
        if ctx.special_function():
            name,arg=self.visit(ctx.special_function())
            return CallStmt(name,arg)
        return CallStmt(ctx.ID().getText(), self.visit(ctx.expression_list()) if ctx.expression_list() else [])

    def visitMixed(self, ctx: MT22Parser.MixedContext):
        if ctx.getChildCount() == 2:
            if ctx.statement():
                return [self.visit(ctx.statement())]+self.visit(ctx.mixed())
            else:
                return self.visit(ctx.vardecl())+self.visit(ctx.mixed())
        else:
            if ctx.statement():
                return [self.visit(ctx.statement())]
            else:
                return self.visit(ctx.vardecl())

    def visitBlock_statement(self, ctx: MT22Parser.Block_statementContext):
        if ctx.EMPTY_BODY():
            return BlockStmt([])
        else:
            if ctx.mixed():
                return BlockStmt(self.visit(ctx.mixed()))
            return BlockStmt([])
    ######################### Statements #########################

    ######################### Special functions #########################
    def visitSpecial_function(self, ctx: MT22Parser.Special_functionContext):
        if ctx.read_int():
            return self.visit(ctx.read_int())
        elif ctx.read_bool():
            return self.visit(ctx.read_bool())
        elif ctx.read_float():
            return self.visit(ctx.read_float())
        elif ctx.read_string():
            return self.visit(ctx.read_string())
        elif ctx.print_int():
            return self.visit(ctx.print_int())
        elif ctx.print_bool():
            return self.visit(ctx.print_bool())
        elif ctx.print_string():
            return self.visit(ctx.print_string())
        elif ctx.write_float():
            return self.visit(ctx.write_float())
        elif ctx.super_():
            return self.visit(ctx.super_())
        else:
            return self.visit(ctx.prevent_default())

    def visitRead_int(self, ctx: MT22Parser.Read_intContext):
        return 'readInteger', []

    def visitPrint_int(self, ctx: MT22Parser.Print_intContext):
        return 'printInteger', [self.visit(ctx.expression())]

    def visitRead_float(self, ctx: MT22Parser.Read_floatContext):
        return 'readFloat', []

    def visitWrite_float(self, ctx: MT22Parser.Write_floatContext):
        return 'writeFloat', [self.visit(ctx.expression())]

    def visitRead_bool(self, ctx: MT22Parser.Read_boolContext):
        return 'readBoolean', []

    def visitPrint_bool(self, ctx: MT22Parser.Print_boolContext):
        return 'printBoolean', [self.visit(ctx.expression())]

    def visitRead_string(self, ctx: MT22Parser.Read_stringContext):
        return 'readString', []

    def visitPrint_string(self, ctx: MT22Parser.Print_stringContext):
        return 'printString', [self.visit(ctx.expression())]

    def visitSuper_(self, ctx: MT22Parser.Super_Context):
        return 'super', [self.visit(ctx.expression())]

    def visitPrevent_default(self, ctx: MT22Parser.Prevent_defaultContext):
        return 'preventDefault', []
    ######################### Special functions #########################
