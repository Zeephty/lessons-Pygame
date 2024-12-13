import pygame            

if __name__ == '__main__':
    pygame.init()

    s = 200, 200

    run = True

    win = pygame.display.set_mode(s)
    pygame.display.set_caption("Я слежу за тобой")

    count = 1

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.WINDOWMINIMIZED:
                count += 1
                
        win.fill("black")

        text = pygame.font.Font(None, 100).render(f"{count}", True, "red")
        win.blit(text, ((s[0] - text.get_width()) // 2, (s[1] - text.get_height()) // 2))

        pygame.display.flip()
    pygame.quit()