import abc
from typing import Final, List

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from moto.stepfunctions.parser.asl.antlr.runtime.ASLLexer import ASLLexer
from moto.stepfunctions.parser.asl.antlr.runtime.ASLParser import ASLParser
from moto.stepfunctions.parser.asl.component.program.program import Program
from moto.stepfunctions.parser.asl.parse.preprocessor import Preprocessor


class SyntaxErrorListener(ErrorListener):
    errors: Final[List[str]]

    def __init__(self):
        super().__init__()
        self.errors = list()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        log_parts = [f"line {line}:{column}"]
        if offendingSymbol is not None and offendingSymbol.text:
            log_parts.append(f"at {offendingSymbol.text}")
        if msg:
            log_parts.append(msg)
        error_log = ", ".join(log_parts)
        self.errors.append(error_log)


class ASLParserException(Exception):
    errors: Final[List[str]]

    def __init__(self, errors: List[str]):
        self.errors = errors

    def __str__(self):
        return repr(self)

    def __repr__(self):
        if not self.errors:
            error_str = "No error details available"
        elif len(self.errors) == 1:
            error_str = self.errors[0]
        else:
            error_str = str(self.errors)
        return f"ASLParserException {error_str}"


class AmazonStateLanguageParser(abc.ABC):
    @staticmethod
    def parse(src: str) -> Program:
        # Attempt to build the AST and look out for syntax errors.
        syntax_error_listener = SyntaxErrorListener()

        input_stream = InputStream(src)
        lexer = ASLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ASLParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(syntax_error_listener)
        tree = parser.state_machine()

        errors = syntax_error_listener.errors
        if errors:
            raise ASLParserException(errors=errors)

        # Attempt to preprocess the AST into evaluation components.
        preprocessor = Preprocessor()
        program = preprocessor.visit(tree)

        return program
