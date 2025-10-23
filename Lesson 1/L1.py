# import pygame

# pygame.init()


# class Circle:
#     def __init__(self, color, center, radius):
#         self.color = color
#         self.center = center
#         self.radius = radius
#     def draw(self):
#         pygame.draw.circle(screen, color = self.color, center = self.center, radius=self.radius)

#     def change_size(self):
#         self.radius +=10
# cir1 = Circle("red", (100, 100), 10)
# screen = pygame.display.set_mode((500, 500))
# running = True
# while running:
#     cir1.draw()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running =False
#             break

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print(event.pos, cir1.center)
#             if event.pos[0]>=cir1.center[0]-cir1.radius or event.pos[0]>=cir1.center[0]+cir1.radius:
#                 cir1.change_size()


#     pygame.display.update()

import pygame
import random
pygame.init()
class Circle:
    def __init__(self, color, center, radius): ## constructor
        self.color=color
        self.center=center
        self.radius=radius
    def draw(self):
        pygame.draw.circle(screen, color=self.color, center=self.center, radius=self.radius)
    def change_color(self):
            self.color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
cir1 = Circle("red", (250, 250), 150)
screen= pygame.display.set_mode((500,500))
running=True
while running:
    cir1.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0]>=cir1.center[0]-cir1.radius or event.pos[0]>=cir1.center[0]+cir1.radius:
                cir1.change_color()

    pygame.display.update()
