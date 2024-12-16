class ASTNode:
    pass


class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements


class Assign(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Print(ASTNode):
    def __init__(self, value):
        self.value = value


class If(ASTNode):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block


class While(ASTNode):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block


class FunctionDef(ASTNode):
    def __init__(self, name, params, block):
        self.name = name
        self.params = params
        self.block = block


class FunctionCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args


class BinaryOp(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Variable(ASTNode):
    def __init__(self, name):
        self.name = name


class Literal(ASTNode):
    def __init__(self, value):
        self.value = value
