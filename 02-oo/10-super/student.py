from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self): ...

    @property
    @abstractmethod
    def perimeter(self): ...


class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def area(self):
        return self.__length * self.__width

    @property
    def perimeter(self):
        return 2 * (self.__length + self.__width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.__side = side

    @property
    def side(self):
        return self.__side


class Ellipse(Shape):
    def __init__(self, major_radius, minor_radius):
        self.__major_radius = major_radius
        self.__minor_radius = minor_radius

    @property
    def major_radius(self):
        return self.__major_radius

    @property
    def minor_radius(self):
        return self.__minor_radius

    @property
    def area(self):
        return pi * self.__major_radius * self.__minor_radius

    @property
    def perimeter(self):
        raise NotImplementedError()


class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def perimeter(self):
        return 2 * pi * self.__radius
