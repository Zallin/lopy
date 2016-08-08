from src.expressions.expression_abc import Expression


class Application(Expression):

    def __init__(self, op, *args):
        pass

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['Application']
