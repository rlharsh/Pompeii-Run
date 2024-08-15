import pygame
from managers.scene_manager.scene import Scene

class GameScreen(Scene):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                print("QUIT")

    def draw(self, screen):
        screen.fill((255, 0, 0))
