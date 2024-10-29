from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self, radius):
        return 3.14 * radius * radius

class Rectangle(Shape):
    def calculate_area(self,length, width):
        return length * width

class Triangle(Shape):

    def calculate_area(self,base, height):
        return 0.5 * base * height



