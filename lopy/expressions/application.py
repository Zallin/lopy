import inspect_expr as ins

from lopy_abc import Expression


class Application(Expression):

    def __init__(self, op, *args):
        self.op = op
        self.op_args = args

    def eval(self, env):
        args = [arg.eval(env) for arg in self.op_args]
        if ins.is_procedure(self.op):
            res = self.op.eval(env)
            return self.apply(res, args)
        proc = self.op.eval(env)
        if ins.is_builtin(proc):
            return proc.apply(*args)
        else:
            return self.apply(proc, args)

    def apply(self, proc, args):
        env = proc.environment()
        appl_env = env.extend()
        for i, a_name in enumerate(proc.arg_list()):
            appl_env.set_binding(a_name, args[i])
        return proc.eval(appl_env)

    def name(self):
        return self.op.name()

    def operands_names(self):
        # TO FIX
        # should work correctly when args are not
        # variable lookups
        return [a.name() for a in self.op_args]

    @staticmethod
    def supported_exprs():
        return ['Application']
