import pygame

if __name__ == '__main__':
    pygame.init()

    a, n = 250, 5

    win = pygame.display.set_mode((a, a))
    pygame.display.set_caption("Шахматная клетка")

    for y in range(n):
        for x in range(n):
            pygame.draw.rect(win, "white" if (x + y) % 2 == (n % 2) else "black", 
                             (x * a // n, y * a // n, (x + 1) * a // n, (y + 1) * a // n))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()