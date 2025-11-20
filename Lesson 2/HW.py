import pygame
pygame.init()
screen=pygame.display.set_mode((2000, 1200))
bg=screen.fill("black")
center_x=screen.get_width() //2

class Spaceship:
    def __init__(self, player):
        self.player=player
        self.speed_x=2
        self.speed_y=2
        if self.player==1:
            self.y, self.x=600,100
        elif self.player==2:
            self.y, self.x=600,1900
        self.image1=pygame.image.load("Lesson 2\s1.png")
        self.image2=pygame.image.load("Lesson 2\s2.png")

    def draw(self):
        if self.player==1:
            screen.blit(self.image1, (self.x,self.y))
        elif self.player==2:
            screen.blit(self.image2, (self.x,self.y))
        pygame.draw.line(screen,(255,255,255) ,(center_x, 0), (center_x, 1200), 5)

    def movements(self):
        keys=pygame.key.get_pressed()
        if self.player==1:
            if self.x<=1000:
                if keys[pygame.K_a]: self.x -=self.speed_x
            if keys[pygame.K_w]: self.y -=self.speed_y
            if keys[pygame.K_s]: self.y +=self.speed_y
            if keys[pygame.K_d]: self.x +=self.speed_x
        if self.player==2:
            if self.x>=1000:
                if keys[pygame.K_LEFT]: self.x -=self.speed_x
            if keys[pygame.K_UP]: self.y -=self.speed_y
            if keys[pygame.K_DOWN]: self.y +=self.speed_y
            if keys[pygame.K_RIGHT]: self.x +=self.speed_x
p1=Spaceship(1)
p2=Spaceship(2)
running=True
while running:
    screen.fill("black")
    p1.draw()
    p2.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
    p1.movements()
    p2.movements()
    pygame.display.update()
