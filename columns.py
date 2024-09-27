import pygame.display
from board import Board

class Columns:

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((720, 920))
        self._clock = pygame.time.Clock()
        self._running = True
        self._speed = 40
        self._board = Board(self._screen)
        pygame.font.init()
        self._score_font = pygame.font.SysFont('Arial', 30)
        self.run()

    def run(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            self._screen.fill("black")
            self._board.draw()
            pygame.display.flip()
            self._clock.tick(40)
            text_surface = self._score_font.render('Score: ' + str(self._board._score), False, (255,255,255))
            self._screen.blit(text_surface, (500,150))
        pygame.quit()

