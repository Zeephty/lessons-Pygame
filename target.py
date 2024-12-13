import pygame

if __name__ == '__main__':
    pygame.init()

    w, n = 2, 100
    s = w * n * 2

    win = pygame.display.set_mode((s, s))
    pygame.display.set_caption("Мишень")

    rgb = ["red", "green", "blue"]
    for i, j in enumerate(range(n - 1, -1, -1)):
        pygame.draw.ellipse(win, rgb[j % 3], (w * i, w * i, 2 * (n - i) * w, 2 * (n - i) * w))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()