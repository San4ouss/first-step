class Check:
    def __init__(self, b):
        self.a = 10
        self.b = b

    def __str__(self):
        return f'{self.a}, {self.b}'


c = Check(20)
print(c)
