#Abstract Classes: contain one or more abstract methods
#Abstract classes can not be instantiated.
from abc import ABC, abstractmethod #we imported ABC

class Shape(ABC):
    @abstractmethod #abstraction
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side

#myshape = Shape() #we can not instantiate the abstract class.
mysquare = Square() #we can not instantiate the abstract class, it gives error.