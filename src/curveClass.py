import math as m
import numpy as np


def midpoints(array):
    """ helper function returns array of half distances between points in array""" 
    return (array[1:] + array[:-1])/2

class curve:
    """ A curve parametrized on the interval t = [0, 1].
    Curves define the geometry of the billiard as a set of functions. 
    To construct a curve one must provide the following functions:
    - r(t, **params) -> (x,y) returns the x and y coordinates of the curve at t as a tuple (or any array like object).
    - normal(t, **params) -> (nx, ny) returns the normal vector of the curve at t as a tuple. 
    - arc_length(t, **params) -> l returns the arc length of the curve up to t.
    Additional curve parameters may be provided as a dictionary of key-word arguments params. 
    """
    def __init__(self, r, normal, arc_length, **parameters):
        self.r = lambda t: r(t, **parameters) #lambda is used to fix parameters
        self.normal = lambda t: normal(t, **parameters)
        self.arc_length = lambda t: arc_length(t, **parameters)
        self.params = parameters
        self.length = self.arc_length(1)
    
    def evaluate(self, M):
        """Evaluate all the curve functions on a equidistant grid on the interval t = [0,1).
        - M is the number of grid points
        Returns one-dimensional numpy arrays:
        - x values of x coordinates
        - y values of y coordinates
        - nx values of normal coordinates in the x direction
        - ny values of normal coordinates in the y direction
        - s values of arc lenght coordinates
        """
        t_values = np.linspace(0, 1, M)
        x, y = np.array([self.r(t) for t in t_values]).transpose()
        nx, ny = np.array([self.normal(t) for t in t_values]).transpose()
        s = np.array([self.arc_length(t) for t in t_values])
        return x, y, nx, ny, s
