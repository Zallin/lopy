def is_procedure(expr):
    return 'lambda' in expr.supported_exprs()


def is_builtin(expr):
    return getattr(expr, 'apply', None) and True


def is_application(expr):
    return 'Application' in expr.supported_exprs()
