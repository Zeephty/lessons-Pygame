import pygame

if __name__ == '__main__':
    pygame.init()

    s = input("Напишите размер окна в формате (w * h)\n Как пример {300 300}: ").split()
    if len(s) >= 2 and s[0].isdigit() and s[1].isdigit():
        size = (int(s[0]), int(s[1]))

        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Крест")

        pygame.draw.line(screen, (255, 255, 255), (0, 0), (size[0], size[1]), 5)
        pygame.draw.line(screen, (255, 255, 255), (0, size[1]), (size[0], 0), 5)

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    else:
        print("Неправильный формат ввода")