from parser.ast import (
    Assign,
    BinaryOp,
    FunctionCall,
    FunctionDef,
    If,
    Literal,
    Print,
    Program,
    Variable,
    While,
)

from lark import Transformer


class ASTTransformer(Transformer):
    def start(self, statements):
        return Program(statements)

    def assign(self, args):
        return Assign(args[0], args[1])

    def print(self, args):
        return Print(args[0])

    def if_block(self, args):
        condition = args[0]
        then_block = args[1]
        else_block = args[2] if len(args) > 2 else None
        return If(condition, then_block, else_block)

    def while_block(self, args):
        return While(args[0], args[1])

    def function_def(self, args):
        name = args[0]
        params = args[1] if args[1] else []
        block = args[2]
        return FunctionDef(name, params, block)

    def function_call(self, args):
        name = args[0]
        args = args[1] if len(args) > 1 else []
        return FunctionCall(name, args)

    def add(self, args):
        return BinaryOp(args[0], "+", args[1])

    def sub(self, args):
        return BinaryOp(args[0], "-", args[1])

    def mul(self, args):
        return BinaryOp(args[0], "*", args[1])

    def div(self, args):
        return BinaryOp(args[0], "/", args[1])

    def grouped_expr(self, args):
        return args[0]

    def number(self, args):
        return Literal(int(args[0]))

    def string(self, args):
        return Literal(args[0][1:-1])

    def variable(self, args):
        return Variable(args[0])
