import pygame

if __name__ == '__main__':
    pygame.init()

    size = (300, 300)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Крест")

    pygame.draw.line(screen, (255, 255, 255), (0, 0), (size[0], size[1]), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, size[1]), (size[0], 0), 5)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()