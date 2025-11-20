# import pygame
# pygame.init()
# screen=pygame.display.set_mode((600,600))
# clock=pygame.time.Clock()

# bg=pygame.image.load("Lesson 2/background (1).png")
# rocket=pygame.image.load("Lesson 2\character.png")

# rocket_y=300
# rocket_x=300
# moves={"up":False, "right": False, "left":False}

# running=True
# while running:
#     screen.blit(bg, (0,0))
#     screen.blit(rocket, (rocket_x,rocket_y))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running=False
#             break

#         if event.type ==pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 moves["up"]=True
#             if event.key == pygame.K_RIGHT:
#                 moves["right"]=True
#             if event.key == pygame.K_LEFT:
#                 moves["left"]=True

#         if event.type ==pygame.KEYUP:
#             if event.key == pygame.K_UP:
#                 moves["up"]=False
#             if event.key == pygame.K_RIGHT:
#                 moves["right"]=False
#             if event.key == pygame.K_LEFT:
#                 moves["left"]=False

#     if moves["up"]: rocket_y -=4
#     if moves["left"]: rocket_x -=4
#     if moves["right"]: rocket_x +=4
#     rocket_y+=2



#     clock.tick(60)
#     pygame.display.update()

    
# git init
# git add .
# git commit -m "message"
# git push

##Homework
import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
bg=pygame.image.load("Lesson 2/background (1).png")
moves={"Up": False, "Down": False, "Right":False, "Left":False}

class Astronaut:
    def __init__(self,x, y, speed_x, speed_y, player):
        self.x=x
        self.y=y
        self.speed_x=speed_x
        self.speed_y=speed_y
        self.player = player
    def draw(self):
        self.image=pygame.image.load("Lesson 2/astronaut.png")
        screen.blit(self.image, (self.x, self.y))
    def movements(self):
        keys = pygame.key.get_pressed()
        if self.player == "1": 
            if keys[pygame.K_UP]: self.y -=self.speed_y
            if keys[pygame.K_DOWN]: self.y +=self.speed_y
            if keys[pygame.K_RIGHT]: self.x +=self.speed_x
            if keys[pygame.K_LEFT]: self.x -=self.speed_x

        


astro1=Astronaut(300, 300, 2, 2, "1")
running=True
while running:
    screen.blit(bg, (0,0))
    astro1.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
    astro1.movements()
    pygame.display.update()