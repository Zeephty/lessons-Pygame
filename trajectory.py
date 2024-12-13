import pygame     


class Circle:
    def __init__(self, win, x, y, r, color):
        self.x, self.y = x, y
        self.win = win
        self.color = color
        self.r = r
        self.v = 40
        self.vect = [0, 0]
        self.clock = pygame.time.Clock()

        self.traj = x, y

    def __call__(self):
        self.draw()
        self.move()

    def draw(self):
        pygame.draw.ellipse(self.win, self.color, (int(self.x) - self.r, int(self.y)- self.r, self.r * 2, self.r * 2))
    
    def move(self):
        if int(self.x) == self.traj[0]:
            self.vect[0] = 0
        elif int(self.x) < self.traj[0]:
            self.vect[0] = 1
        else:
            self.vect[0] = -1
        if int(self.y) == self.traj[1]:
            self.vect[1] = 0
        elif int(self.y) < self.traj[1]:
            self.vect[1] = 1
        else:
            self.vect[1] = -1

        self.x += self.v * self.vect[0] / 1000
        self.y += self.v * self.vect[1] / 1000

    def rep(self, x, y):
        self.traj = x, y

        
if __name__ == '__main__':
    pygame.init()

    s = 501, 501

    run = True

    win = pygame.display.set_mode(s)
    pygame.display.set_caption("К щелчку")

    ball = Circle(win, 250, 250, 20, "red")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.rep(*event.pos)
                
        win.fill("black")

        ball()

        pygame.display.flip()
    pygame.quit()