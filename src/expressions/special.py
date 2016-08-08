from src.expressions.expression_abc import Expression


class Quote(Expression):

    def __init__(self, *args):
        pass

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['quote']


class Assignment(Expression):

    def __init__(self, name, expr):
        pass

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['set!']


class Definition(Expression):

    def __init__(self, name, expr):
        pass

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['define']


class IfCondition(Expression):

    def __init__(self, pred, conseq, alt):
        pass

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['if']


class Lambda(Expression):

    def __init__(self, args, body):
        pass

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['lambda']


class BeginExpr(Expression):

    def __init__(self, *args):
        pass

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['begin']


class Cond(Expression):

    def __init__(self, *args):
        pass

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['cond']
