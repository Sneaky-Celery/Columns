import numpy as np
import random
import pygame
from gems import Gems
from ground import Ground
from collision_detection import CollisionDetector


#NOTE: Board size is 6 wide and 13 tall

class Board:
    def __init__(self, screen, height=13, width=6):
        self._height = height
        self._width = width
        self._screen = screen
        #self._ground = Ground(width, height)
        #self._collision_detector = CollisionDetector(self, self._ground)
        self._matrix = np.zeros([width, height], dtype=int)
        self._current_tile = None
        self._score = 0
        self._triplet = Gems.generate_triplet()

    def draw(self):
        blockSize = 35
        x_offset = 100
        y_offset = 50
        for x in range (0, self._width):
            for  y in range (0, self._height):
                rect = pygame.Rect(x_offset + x * blockSize, y_offset + y * blockSize, blockSize)
                pygame.draw.rect(self._screen, self._colors[self._matrix[x, y]], rect,
                                 1 if self._matrix[x,y] == 0 else 0)
                
    def update(self, on_timer = True):
        if self._current_tile is None:
            self.create_tile()
        if on_timer:
            self.drop_tile()

        self._matrix[:, :] = 0
        self.draw_tile(self._current_tile)
        self.draw_ground(self._ground)
    
    def drop_tile(self):
        is_locked = self._current_tile.move(0,1)
        if is_locked:
            self._ground.merge(self._current_tile)
            self.score = self.score + self._combos()
            self.create_tile()

    #def create_tile(self):
    #    self._current_tile = Gems(self._collision_detection, )

    def on_key_up(self):
        self._current_tile.rotate(1)
        self.draw()

    def on_key_down(self):
        self._current_tile.move(0,1)
        self.draw()

    def on_key_right(self):
        self._current_tile.move(1,0)
        self.draw()

    def on_key_left(self):
        self._current_tile.move(-1,0)
        self.draw()