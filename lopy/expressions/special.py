import inspect_expr as ins

from lopy_abc import Expression


class Quote(Expression):

    def __init__(self, *args):
        pass

    def eval(self, env):
        pass

    @staticmethod
    def supported_exprs():
        return ['quote']


class Definition(Expression):

    def __init__(self, var, *args):
        self.name = var.name()
        self.param_names = var.operands_names() if ins.is_application(var) else None
        self.exprs = args

    def eval(self, env):
        if self.param_names:
            lambda_obj = Lambda(self.param_names, *self.exprs)
            expr_res = lambda_obj.eval(env)
        else:
            expr = self.exprs[0]
            expr_res = expr.eval(env)
        env.set_binding(self.name, expr_res)

    @staticmethod
    def supported_exprs():
        return ['define', 'set!']


class IfCondition(Expression):

    def __init__(self, pred, conseq, alt):
        self.pred = pred
        self.conseq = conseq
        self.alt = alt

    def eval(self, env):
        res = self.pred.eval(env)
        if res:
            return self.conseq.eval(env)
        else:
            return self.alt.eval(env)

    @staticmethod
    def supported_exprs():
        return ['if']


class Lambda(Expression):

    def __init__(self, args_obj, *args):
        # TO FIX
        # args_obj should be list of args, not application instance
        if isinstance(args_obj, list):
            self.args = args_obj
        else:
            self.args = [args_obj.name()]
            self.args.extend(args_obj.operands_names())
        self.body = args

    def eval(self, env):
        return RuntimeLambda(self.args, self.body, env)

    @staticmethod
    def supported_exprs():
        return ['lambda']


class RuntimeLambda:

    def __init__(self, args, body, env):
        self.args = args
        self.body = body
        self.env = env

    def eval(self, new_env):
        return [expr.eval(new_env) for expr in self.body][-1]

    def environment(self):
        return self.env

    def arg_list(self):
        return self.args

    # TO FIX
    # move to different module
    @staticmethod
    def supported_exprs():
        return []


class BeginExpr(Expression):

    def __init__(self, *args):
        self.exprs = args

    def eval(self, env):
        return [expr.eval(env) for expr in self.exprs][-1]

    @staticmethod
    def supported_exprs():
        return ['begin']


class Cond(Expression):

    def __init__(self, *args):
        self.cond_seq = args

    def eval(self, env):
        for cond in self.cond_seq:
            if cond.name() == 'else':
                return cond.op_args[0].eval(env)
            pred_res = cond.op.eval(env)
            if pred_res:
                return cond.op_args[0].eval(env)
        return None

    @staticmethod
    def supported_exprs():
        return ['cond']
