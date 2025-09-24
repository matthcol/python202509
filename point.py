from dataclasses import dataclass
from math import dist


@dataclass
class Point:
    """ Represents a 2D point with its coordinates x and y

    Example:
        p1 = Point(1.0, 23.5)
        p2 = Point(x=1.0, y=23.5)
    """
    
    x: float = 0
    y: float = 0

    # surcharge l'opérateur "+"
    def __add__(self, other):
        # TODO: accept int and float and add param to both self.x and self.y
        if not isinstance(other, Point):
            return NotImplemented
        return Point(x=self.x + other.x, y=self.y + other.y)
    
    # implémenter 
    def __len__(self):
        return 2

    def distance(self, other: 'Point') -> float:
        """ Compute the distance between this point and another one
        """
        return dist((self.x, self.y), (other.x, other.y))