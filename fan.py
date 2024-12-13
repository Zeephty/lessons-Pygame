import pygame     
from math import cos, sin, radians


class Fan:
    def __init__(self, win, x, y, r, color):
        self.x, self.y = x, y
        self.win = win
        self.color = color
        self.r = r
        self.v = 50
        self.vect = 0
        self.clock = pygame.time.Clock()
        self.blade = 70

        self.ungle = 0

    def __call__(self):
        self.draw()
        self.run()

    def draw(self):
        pygame.draw.ellipse(self.win, self.color, (self.x - self.r, self.y- self.r, self.r * 2, self.r * 2))
        pygame.draw.polygon(self.win, self.color, ((self.x, self.y), 
                                                   (self.x + self.blade * sin(radians(15 + self.ungle)), 
                                                    self.y - self.blade * cos(radians(15 + self.ungle))),
                                                   (self.x - self.blade * sin(radians(15 - self.ungle)), 
                                                    self.y - self.blade * cos(radians(15 - self.ungle)))))
        pygame.draw.polygon(self.win, self.color, ((self.x, self.y), 
                                                   (self.x + self.blade * sin(radians(135 + self.ungle)), 
                                                    self.y - self.blade * cos(radians(135 + self.ungle))),
                                                   (self.x - self.blade * sin(radians(-105 - self.ungle)), 
                                                    self.y - self.blade * cos(radians(-105 - self.ungle)))))
        pygame.draw.polygon(self.win, self.color, ((self.x, self.y), 
                                                   (self.x + self.blade * sin(radians(-105 + self.ungle)), 
                                                    self.y - self.blade * cos(radians(-105 + self.ungle))),
                                                   (self.x - self.blade * sin(radians(135 - self.ungle)), 
                                                    self.y - self.blade * cos(radians(135 - self.ungle)))))                                         

    def redact(self, n):
        self.vect += n

    def run(self):
        self.ungle += self.v * self.vect * self.clock.tick() / 1000

        
if __name__ == '__main__':
    pygame.init()

    s = 201, 201

    run = True

    win = pygame.display.set_mode(s)
    pygame.display.set_caption("Вентилятор")

    fan = Fan(win, 100, 100, 10, (255, 255, 255))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    fan.redact(1)
                if event.button == pygame.BUTTON_RIGHT:
                    fan.redact(-1)
                
        win.fill("black")

        fan()

        pygame.display.flip()
    pygame.quit()