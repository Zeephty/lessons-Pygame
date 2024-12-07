import pygame

if __name__ == '__main__':
    pygame.init()

    size = 300, 300

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Прямоугольник")

    pygame.draw.rect(screen, "red", (1, 1, size[0] - 1, size[1] - 1))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()