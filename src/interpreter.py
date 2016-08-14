from parser import Parser


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
