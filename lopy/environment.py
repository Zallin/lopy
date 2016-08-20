class Environment:

    def __init__(self, enclosing=None):
        self.env = {}
        self.enclosing = enclosing

    def set_binding(self, name, obj):
        self.env[name] = obj

    def find(self, name):
        if name in self.env:
            return self.env[name]
        if self.enclosing:
            return self.enclosing.find(name)

    def extend(self):
        return type(self)(enclosing=self)
