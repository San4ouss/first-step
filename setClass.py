class Point:
    def __init__(self, x):
        self.__x = x

    @property
    def coord(self):
        return self.__x

    @coord.setter
    def coord(self, x):
        self.__x = x


p = Point(5)
print(p.coord)
p.coord = 10
print(p.coord)
print(p._Point__x)
print(p.__dict__)
