import pygame


class Circle:
    def __init__(self, win, x, y, color):
        self.x, self.y = x, y
        self.w = 0
        self.win = win
        self.color = color
        self.v = 10

        self.clock = pygame.time.Clock()

    def draw(self):   
        pygame.draw.ellipse(self.win, self.color, (self.x - self.w // 2, 
                                                   self.y - self.w // 2, 
                                                   int(self.w), int(self.w)))
    
    def event(self):
        self.w += self.v * self.clock.tick() / 1000


if __name__ == '__main__':
    pygame.init()

    s = 500, 400

    run = True

    win = pygame.display.set_mode(s)
    pygame.display.set_caption("Жёлтый круг")

    circle = None

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                circle = Circle(win, x, y, "yellow")
        win.fill("blue")

        if circle is not None:
            circle.draw()
            circle.event()
        
        pygame.display.flip()
    pygame.quit()