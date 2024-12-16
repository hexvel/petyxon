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


class PythonCodeGenerator:
    def generate(self, node):
        if isinstance(node, Program):
            return "\n".join(self.generate(stmt) for stmt in node.statements)
        elif isinstance(node, Assign):
            return f"{node.name} = {self.generate(node.value)}"
        elif isinstance(node, Print):
            return f"print({self.generate(node.value)})"
        elif isinstance(node, If):
            then_block = self.generate(node.then_block)
            else_block = (
                f"else:\n    {self.generate(node.else_block)}"
                if node.else_block
                else ""
            )
            return (
                f"if {self.generate(node.condition)}:\n    {then_block}\n{else_block}"
            )
        elif isinstance(node, While):
            return f"while {self.generate(node.condition)}:\n    {self.generate(node.block)}"
        elif isinstance(node, FunctionDef):
            params = ", ".join(node.params)
            body = self.generate(node.block)
            return f"def {node.name}({params}):\n    {body}"
        elif isinstance(node, FunctionCall):
            args = ", ".join(self.generate(arg) for arg in node.args)
            return f"{node.name}({args})"
        elif isinstance(node, BinaryOp):
            return f"({self.generate(node.left)} {node.operator} {self.generate(node.right)})"
        elif isinstance(node, Variable):
            return node.name
        elif isinstance(node, Literal):
            return repr(node.value)
        else:
            raise NotImplementedError(f"Неизвестный тип узла: {type(node)}")
