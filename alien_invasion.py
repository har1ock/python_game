import sys
import pygame


class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""
    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Задати колір фону
        self.bg.color = (230, 230, 230)

    def run_game(self):
        """Розпочати головний цикл гри."""
        while True:
            # Слідкувати зп подіями миші та клавіатури.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Показати останій намальований екран.
            pygame.display.flip()

if __name__ == '__main__':
    # Створити екземпляр гри та запустити гру.
    ai = AlienInvasion()
    ai.run_game()

