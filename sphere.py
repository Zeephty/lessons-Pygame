import pygame

if __name__ == '__main__':
    pygame.init()

    n = 15
    s = 300
    w = s // (2 * n)

    win = pygame.display.set_mode((s, s))
    pygame.display.set_caption("Сфера")

    for i in range(n):
        pygame.draw.ellipse(win, (255, 255, 255), (i * w, 0, 2 * (n - i) * w, s), 1)

    for i in range(n):
        pygame.draw.ellipse(win, (255, 255, 255), (0, i * w, s, 2 * (n - i) * w), 1)

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()