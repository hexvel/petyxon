from parser.ast import Assign, Print


class Interpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, node):
        if isinstance(node, Assign):
            self.variables[node.name] = self.evaluate(node.value)
        elif isinstance(node, Print):
            print(self.evaluate(node.value))

    def evaluate(self, node):
        if isinstance(node, str):
            return node
        elif isinstance(node, int):
            return node
