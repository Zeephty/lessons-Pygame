import pygame


class Circle:
    def __init__(self, win, x, y, w, color):
        self.x, self.y = x, y
        self.w = w
        self.win = win
        self.color = color

        self.v = 100
        self.vect = [-1, -1]

        self.clock = pygame.time.Clock()

    def draw(self): 
        pygame.draw.ellipse(self.win, self.color, (int(self.x) - self.w // 2, 
                                                   int(self.y) - self.w // 2, 
                                                   self.w, self.w))
    
    def event(self):
        wx, wy = win.get_size()
        v = self.v * self.clock.tick() / 1000
        x, y = self.x + v * self.vect[0], self.y + v * self.vect[1]
        if 0 + self.w // 2 <= x <= wx - self.w // 2:
            self.x = x
        else:
            self.vect[0] *= -1
        if 0 + self.w // 2 <= y <= wy - self.w // 2:
            self.y = y
        else:
            self.vect[1] *= -1


class Box:
    def __init__(self):
        self.objs = set()

    def __iadd__(self, *args):
        self.objs |= set(args)
        return self
    
    def __call__(self):
        for obj in self.objs:
            obj.draw()
            obj.event()


if __name__ == '__main__':
    pygame.init()

    s = 500, 350

    run = True

    win = pygame.display.set_mode(s)
    pygame.display.set_caption("Шарики")

    box = Box()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    x, y = event.pos
                    box += Circle(win, x, y, 20, (255, 255, 255))

        win.fill("black")

        box()
        
        pygame.display.flip()
    pygame.quit()