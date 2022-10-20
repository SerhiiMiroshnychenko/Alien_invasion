import sys

import pygame

from settings import Settings


class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Створює вікно, у якому будуть показуватися графічні елементи забавки.
        # Аргумент (self.settings.screen_width, self.settings.screen_height) - це кортеж, що позначає розміри вікна
        # завширшки та заввишки в пікселях.
        # Це "поверхня" (surface) - частина екрана, де показується елемент гри.
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Розпочати головний цикл гри."""
        while True:
            # Слідкувати за подіями миші та клавіатури.
            for event in pygame.event.get():  # Змінна event - це якась дія гравця. Цей цикл for - це диспетчер подій,
                # що сприймає події та виконує відповідні дії. Функція pygame.event.get() повертає список подій, що
                # сталися після її останнього виклику.
                if event.type == pygame.QUIT:  # Якщо гравець зачиняє вікно:
                    sys.exit()                 # Вихід з гри.

            # Наново перемалювати екран на кожній ітерації циклу.
            self.screen.fill(self.settings.bg_color)

            # Показати останній намальований екран.
            pygame.display.flip()


if __name__ == '__main__':
    # Створити екземпляр гри та запустити гру.
    ai = AlienInvasion()
    ai.run_game()
