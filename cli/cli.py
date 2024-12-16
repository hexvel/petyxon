import argparse
import sys
from parser.parser import ASTTransformer

from lark import Lark, exceptions

from codegen.generator import PythonCodeGenerator
from interpreter.interpreter import Interpreter


def get_parser():
    """
    Создает объект Lark-парсера из грамматики.
    """
    with open("parser/grammar.lark", "r", encoding="utf-8") as grammar_file:
        grammar = grammar_file.read()
    return Lark(grammar, parser="lalr", start="start")


def compile_to_python(source_code, lark_parser):
    """
    Компилирует код на Petyxon в Python.
    """
    try:
        parse_tree = lark_parser.parse(source_code)
    except exceptions.LarkError as e:
        raise SyntaxError(f"Ошибка парсинга: {e}")

    transformer = ASTTransformer()
    ast = transformer.transform(parse_tree)

    generator = PythonCodeGenerator()
    python_code = generator.generate(ast)

    return python_code


def execute_interpreter(source_code, lark_parser):
    """
    Выполняет код на Petyxon через интерпретатор AST.
    """
    try:
        parse_tree = lark_parser.parse(source_code)
    except exceptions.LarkError as e:
        raise SyntaxError(f"Ошибка парсинга: {e}")

    transformer = ASTTransformer()
    ast = transformer.transform(parse_tree)

    interpreter = Interpreter()
    interpreter.execute(ast)


def main():
    """
    CLI для работы с Petyxon.
    """
    parser = argparse.ArgumentParser(description="Petyxon CLI")
    parser.add_argument("file", help="Путь к файлу с кодом на Petyxon (.yp)")
    parser.add_argument(
        "--compile",
        help="Компилировать код в Python и вывести результат",
        action="store_true",
    )
    parser.add_argument(
        "--run",
        help="Запустить код через интерпретатор Petyxon",
        action="store_true",
    )

    args = parser.parse_args()

    # Чтение исходного кода
    try:
        with open(args.file, "r", encoding="utf-8") as file:
            source_code = file.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {args.file} не найден.")
        sys.exit(1)

    # Создаем парсер Lark
    lark_parser = get_parser()

    if args.compile:
        try:
            python_code = compile_to_python(source_code, lark_parser)
            print(python_code)
        except Exception as e:
            print(f"Ошибка компиляции: {e}")
            sys.exit(1)
    elif args.run:
        try:
            execute_interpreter(source_code, lark_parser)
        except Exception as e:
            print(f"Ошибка выполнения: {e}")
            sys.exit(1)
    else:
        print("Укажите один из флагов: --compile или --run")
        sys.exit(1)


if __name__ == "__main__":
    main()
