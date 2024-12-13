import pygame

if __name__ == '__main__':
    pygame.init()

    w, h = 30, 15
    d = 2
    s = 300, 200
    n = s[0] // w + 1, s[1] // h + 1

    win = pygame.display.set_mode(s)
    pygame.display.set_caption("Кирпичи")

    win.fill((255, 255, 255))

    for y in range(n[1]):
        for x in range(n[0]):
            pygame.draw.rect(win, "red", (x * (w + d) - (w // 2) * (y % 2), y * (h + d), w, h))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()