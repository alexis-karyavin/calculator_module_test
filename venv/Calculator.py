class Calculator:
    def __init__(self, system = 10):
        self.system = system

    def add(self, a, b):
        if (self.system == 10):
            return int(a, 10) + int(b, 10)
        if (self.system == 16):
            return int(a, 16) + int(b, 16)

    def sub(self, a, b):
        if (self.system == 10):
            return int(a, 10) - int(b, 10)
        if (self.system == 16):
            return int(a, 16) - int(b, 16)

    def mul(self, a, b):
        if (self.system == 10):
            return int(a, 10) * int(b, 10)
        if (self.system == 16):
            return int(a, 16) * int(b, 16)

    def div(self, a, b):
        if (self.system == 10):
            return int(a, 10) / int(b, 10)
        if (self.system == 16):
            return int(a, 16) / int(b, 16)

    def process(self, result):
        result.replace(" ", "")
        if (len(result.split('+')) == 2):
            prms = result.split('+')
            return self.add(prms[0], prms[1])
        if (len(result.split('-')) == 2):
            prms = result.split('-')
            return self.sub(prms[0], prms[1])
        if (len(result.split('*')) == 2):
            prms = result.split('*')
            return self.mul(prms[0], prms[1])
        if (len(result.split('/')) == 2):
            prms = result.split('/')
            return self.div(prms[0], prms[1])