import re
import settings
import dynamic_import as di


class Parser:

    def __init__(self):
        self.atom = self._load_module_classes_as_map(
            settings.ATOM_EXPR_MOD_NAME)
        self.special = self._load_module_classes_as_map(
            settings.SPEC_EXPR_MOD_NAME)
        self.application = self._load_module_classes_as_map(
            settings.APPL_EXPR_MOD_NAME)

    def parse(self, raw_src):
        tokens = self._tokenize(raw_src)
        return [self._parse(token) for token in tokens]

    def _load_module_classes_as_map(self, mod_name):
        mod_classes = di.import_module_classes(mod_name)
        return {name: ClassObj
                for ClassObj in mod_classes
                for name in ClassObj.supported_exprs()}

    def _parse(self, expr):
        if not isinstance(expr, list):
            return self._create_atom(expr)
        op = expr[0]
        raw_operands = expr[1:]
        parsed_operands = [self._parse(o) for o in raw_operands]
        if not isinstance(op, list) and op in self.special:
            cons = self.special[op]
            return cons(*parsed_operands)
        else:
            cons = self.application['Application']
            return cons(self._parse(op), *parsed_operands)

    def _create_atom(self, atom):
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
