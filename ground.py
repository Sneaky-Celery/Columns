import numpy as np

class Ground:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._matrix = np.zeros([width,height], dtype=int)
        self._coordinates = list()