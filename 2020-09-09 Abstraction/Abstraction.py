#Abstract Classes: contain one or more abstract methods
#Abstract classes can not be instantiated.
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side

myshape = Shape() #we instantiated
