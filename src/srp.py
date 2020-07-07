"""
Single Responsibility Principle
-------------------------------
A class should have one and only one reason to change, 
meaning that a class should have only one job.
"""
import functools

class Circle:
    """
    A Circle class that has a radius
    """

    def __init__(self, radius):
        self.radius = radius


class Square:
    """
        A Square class that has a length of the sides
    """

    def __init__(self, length):
        self.length = length


class AreaCalculator:
    """
        An AreaCalculator class that takes in a list of shapes
    """

    def __init__(self, shapes):
        self.shapes = shapes
    
    def sum(self):
        """
            The sum function calculates the area of the shapes in self.shapes,
            and returns the total sum of the areas
        """
        # logic to sum the areas of the shapes
        area = []
        for shape in self.shapes:
            if isinstance(shape, Circle):
                area.append((3.142 * (shape.radius ** 2)))
            elif isinstance(shape, Square):
                area.append(shape.length ** 2)

        return functools.reduce(lambda a,b : a + b, area)

    def __str__(self):
        """
            return an output of the sum method in a string format
        """
        
        return f"Sum of the areas of provided shapes: {self.sum()}"



shapes = [Circle(4), Square(5), Square(6)]

areas = AreaCalculator(shapes)

print(areas)
