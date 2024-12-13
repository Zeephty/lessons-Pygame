import pygame

if __name__ == '__main__':
    pygame.init()

    w = 35
    s = (300, 300)
    n = (s[0] // w, s[1] // w)

    win = pygame.display.set_mode(s)
    pygame.display.set_caption("Ромбики")

    win.fill("yellow")

    for y in range(n[1]):
        for x in range(n[0]):
            pygame.draw.polygon(win, "orange", ((w // 2 + w * x, y * w), 
                                                ((x + 1) * w, w // 2 + y * w), 
                                                (w // 2 + w * x, (y + 1) * w),
                                                (x * w, w // 2 + w * y)))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()