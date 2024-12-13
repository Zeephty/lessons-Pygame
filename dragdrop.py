import pygame


class Rect:
    def __init__(self, win, x, y, w, color):
        self.x, self.y = x, y
        self.w = w
        self.win = win
        self.color = color

        self.flag = False

        self.v = 100
        self.vect = [-1, -1]

        self.mv = (0, 0)

        self.clock = pygame.time.Clock()

    def draw(self): 
        pygame.draw.rect(self.win, self.color, (self.x - self.mv[0], self.y - self.mv[1], self.w, self.w))
    
    def moveYN(self, x, y, t):
        if self.collision(x, y) and t != self.flag:
            if not self.flag:
                self.mv = (x - self.x, y - self.y)
            else:
                self.x, self.y = self.x - self.mv[0], self.y - self.mv[1]
                self.mv = (0, 0)
            self.flag = t
    
    def collision(self, x, y):
        return self.x <= x < self.x + self.w and self.y <= y < self.y + self.w
    
    def move(self, x, y):
        if self.flag:
            self.x, self.y = x, y
            

if __name__ == '__main__':
    pygame.init()

    s = 300, 300

    run = True

    win = pygame.display.set_mode(s)
    pygame.display.set_caption("Перетаскивание")

    square = Rect(win, 0, 0, 100, "green")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    x, y = event.pos
                    square.moveYN(x, y, 1)
                    square.move(x, y)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    x, y = event.pos
                    square.moveYN(x, y, 0)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                square.move(x, y)
                
        win.fill("black")

        square.draw() 

        pygame.display.flip()
    pygame.quit()