"""
Single Responsibility Principle
-------------------------------
A class should have one and only one reason to change, 
meaning that a class should have only one job.
"""
import functools

class ShapeInterface:
    """
        The ShapeInterface enforces implementation of the area method
        inputs: none
        outputs: Error
    """
    def area(self):
        raise NotImplementedError()


class SolidShapeInterface:
    """
        The SolidShapeInterface enforces implementation of the volume method
        inputs: none
        outputs: Error
    """
    def volume(self):
        raise NotImplementedError()



class Circle(ShapeInterface):
    """
    A Circle class that has a radius
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.142 * (self.radius ** 2))

class Square(ShapeInterface):
    """
        A Square class that has a length of the sides
    """

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


class Cube(ShapeInterface, SolidShapeInterface):
    """
        A Cube class that has a length of the sides
    """

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def volume(self):
        return self.length ** 3



class Squiggle(ShapeInterface):
    """
        A Squigle class that is a made up shape
    """
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * 9


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
            area.append(shape.area())
            # if isinstance(shape, Circle):
            #     area.append((3.142 * (shape.radius ** 2))) # pi r squared
            # elif isinstance(shape, Square):
            #     area.append(shape.length ** 2) # square the length of the shape

        return functools.reduce(lambda a,b : a + b, area)

    def __str__(self):
        """
            return an output of the sum method in a string format
        """
        
        return f"Sum of the areas of provided shapes: {self.sum()}"


class VolumeCalculator(AreaCalculator):

    def __init__(self, shapes):
        super.__init__(shapes)
    
    def sum(self):
        """
            The sum function calculates the volume of the shapes in self.shapes,
            and returns the total sum of the volumes
        """
        # logic to sum the volume of the shapes
        volumes = []
        for shape in self.shapes:
            volumes.append(shape.volume())


        return functools.reduce(lambda a, b: a + b, volumes)
        
    def __str__(self):
        """
            return an output of the sum method in a string format
        """
        
        return f"Sum of the volumes of provided shapes: {self.sum()}"


shapes = [Circle(4), Square(5), Square(6), Squiggle(10)]
solid_shapes = [Cube(10), Cube(20)]
areas = AreaCalculator(shapes)
volumes = VolumeCalculator(solid_shapes)

print(areas)

print(volumes)




# Inversions

class DBConnectionInterface:
    def connect(self):
        raise NotImplementedError()

class MySQLConnection(DBConnectionInterface):
    def connect(self):
        return "this is my mysql connection!!"


class PGSQLConnection(DBConnectionInterface):
    def connect(self):
        return "this is my PG SQL connection!!"




class PasswordReminder:
    def __init__(self, dbConnection):
        self.dbConnection = dbConnection

    def connection(self):
        return self.dbConnection.connect()
