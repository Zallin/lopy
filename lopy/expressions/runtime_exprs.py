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
