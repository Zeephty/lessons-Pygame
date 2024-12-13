import pygame


class Cube:
    def __init__(self, win, x, y, w, hue):
        self.x, self.y = x, y
        self.w = w
        self.win = win

        self.col_1 = pygame.Color(255, 255, 255)
        self.col_2 = pygame.Color(255, 255, 255)
        self.col_3 = pygame.Color(255, 255, 255)

        hsv_1 = self.col_1.hsva
        hsv_2 = self.col_2.hsva
        hsv_3 = self.col_3.hsva

        self.col_1.hsva = (hue, hsv_2[1] + 100, hsv_2[2], hsv_2[3])
        self.col_2.hsva = (hue, hsv_1[1] + 100, hsv_1[2] - 25, hsv_1[3])
        self.col_3.hsva = (hue, hsv_3[1] + 100, hsv_3[2] - 50, hsv_3[3])

    def draw(self):   
        pygame.draw.rect(self.win, self.col_1, (self.x, self.y + self.w // 2, self.w, self.w))
        pygame.draw.polygon(self.win, self.col_2, ((self.x, self.y + self.w // 2), 
                                                   (self.x + self.w // 2, self.y),
                                                   (self.x + self.w * 3 // 2, self.y), 
                                                   (self.x + self.w, self.y + self.w // 2)))
        pygame.draw.polygon(self.win, self.col_3, ((self.x + self.w, self.y + self.w // 2),
                                                   (self.x + (self.w * 3) // 2, self.y),
                                                   (self.x + (self.w * 3) // 2, self.y + self.w),
                                                   (self.x + self.w, self.y + self.w * 3 // 2)))


if __name__ == '__main__':
    pygame.init()

    w = 80
    s = 300, 300
    hue = 73

    win = pygame.display.set_mode(s)
    pygame.display.set_caption("Куб")

    cube = Cube(win, 90, 90, w, hue)
    cube.draw()

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()