import re
import inspect
import importlib

from pathlib import Path


class Parser:

    def __init__(self):
        package_path = 'src.expressions.'
        self.atom = self._load_module_classes_as_map(package_path + 'atom')
        self.special = self._load_module_classes_as_map(
            package_path + 'special')
        self.application = self._load_module_classes_as_map(
            package_path + 'application')

    def parse(self, raw_src):
        tokens = self._tokenize(raw_src)
        exprs = []
        for token in tokens:
            expr = self._parse(token)
            exprs.append(expr)
        return exprs

    def _load_module_classes_as_map(self, mod_name):
        mod = importlib.import_module(mod_name)
        class_map = {}
        for _, obj in mod.__dict__.items():
            if inspect.isclass(obj) and obj.__module__ == mod_name:
                for name in obj.supported_exprs():
                    class_map[name] = obj
        return class_map

    def _parse(self, expr):
        if not isinstance(expr, list):
            return self._create_atom(expr)
        op = expr[0]
        if isinstance(op, list):
            op = self._parse(op)
        raw_operands = expr[1:]
        parsed_operands = []
        for o in raw_operands:
            parsed_operands.append(self._parse(o))
        if op in self.special:
            cons = self.special[op]
            return cons(*parsed_operands)
        else:
            cons = self.application['Application']
            return cons(op, *parsed_operands)

    def _create_atom(self, atom):
        expr_type = None
        try:
            int(atom)
            expr_type = 'Number'
        except ValueError:
            expr_type = 'Variable'
        return self.atom[expr_type](atom)

    def _tokenize(self, raw_src):
        raw_tokens = re.sub(
            '\(', ' ( ', re.sub('\)', ' ) ', raw_src)).split()
        tokens = []
        while len(raw_tokens) > 0:
            tokens.append(self._extract_tokens(raw_tokens))
        return tokens

    def _extract_tokens(self, raw_tokens):
        cur_token = raw_tokens.pop(0)
        if cur_token == '(':
            expr = []
            while raw_tokens[0] != ')':
                expr.append(self._extract_tokens(raw_tokens))
            raw_tokens.pop(0)
            return expr
        else:
            if cur_token == '\'':
                raw_tokens.insert(1, 'quote')
                return self._extract_tokens(raw_tokens)
            elif cur_token[0] == '\'':
                cur_token = ['quote', cur_token[1:]]
            return cur_token


class Interpreter:

    def __init__(self):
        self.global_env = self._init_global_env()
        self.parser = Parser()

    def eval(self, raw_src):
        exprs = self.parser.parse(raw_src)
        for exp in exprs:
            res = self._eval(exp, self.global_env)  # ?
        return res

    @staticmethod
    def _init_global_env():
        pass

    def _eval(self, exp, env):
        pass
