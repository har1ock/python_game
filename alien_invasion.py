import sys
import pygame


class AlieInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""
    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Розпочати головний цикл гри."""

