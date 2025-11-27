import pygame
pygame.init()
screen=pygame.display.set_mode((2000, 1200))
bg=screen.fill("black")
center_x=screen.get_width() //2
pygame.Rect((500,600), (50,50))

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
        self.rect=self.image1.get_rect(center=(self.x, self.y))
        self.rect=self.image2.get_rect(center=(self.x, self.y))

    def draw(self):
        if self.player==1:
            screen.blit(self.image1, (self.rect.topleft))
        elif self.player==2:
            screen.blit(self.image2, (self.rect.topleft))
        pygame.draw.line(screen,(255,255,255) ,(center_x, 0), (center_x, 1200), 5)

    def bullet(self):
        pygame.Rect((500,600), (50,50))
        pygame.draw.rect(screen, colour, (20,10))
        
    def movements(self):
        keys=pygame.key.get_pressed()
        if self.player==1:
            if self.rect.x<=850:
                if keys[pygame.K_d]: self.rect.x +=self.speed_x
            if keys[pygame.K_w]: self.rect.y -=self.speed_y
            if keys[pygame.K_s]: self.rect.y +=self.speed_y
            if keys[pygame.K_a]: self.rect.x -=self.speed_x
        if self.player==2:
            if self.rect.x>=1000:
                if keys[pygame.K_LEFT]: self.rect.x -=self.speed_x
            if keys[pygame.K_UP]: self.rect.y -=self.speed_y
            if keys[pygame.K_DOWN]: self.rect.y +=self.speed_y
            if keys[pygame.K_RIGHT]: self.rect.x +=self.speed_x

class Bullet:
    def __init__(self, colour, position):
        self.colour=colour
        self.rect=pygame.Rect((position), (15,10))

    def draw(self):
        pygame.draw.rect(screen, self.colour, self.rect)

    
        
p1=Spaceship(1)
p2=Spaceship(2)
running=True
while running:
    screen.fill("black")
    p1.draw()
    p2.draw()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
                break
            if event.key == pygame.K_e:
                red_b=Bullet("red",  )
    p1.movements()
    p2.movements()
    pygame.display.update()