import pygame
from managers.scene_manager.scene_manager import SceneManager
from scenes.game_screen import GameScreen

class PompeiiRun:

    def __init__(self, width=384, height=216):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pompeii Run")
        self.clock = pygame.time.Clock()

        self.scene_manager = SceneManager(self.screen)
        self.scene_manager.add_scene("game", GameScreen)
        self.scene_manager.change_scene("game")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self):
        self.scene_manager.update()

    def draw(self):
        self.scene_manager.draw()
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
