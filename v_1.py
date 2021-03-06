import pygame
import sys
import pymunk
import pymunk.pygame_util

#TODO
# Create small course
# Add in friction
# Add in multi-color marbles
# Add in course creator
# Small GUI for screen size? 
# Rotation?
# Touple issues in Create_static_platform()
# Add custom sprites 
# Remove debug_draw? 

# Function for creating marbles on click
def Create_marble(space, pos):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 40)
    space.add(body, shape)
    return shape

# Function for creating the static lines in the game
# L = left (Touple), R = right (Touple), T = thickness (Float)
def Create_static_platform(space, pos, L1, L2, R1, R2, T):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Segment(body, (L1, L2), (R1, R2), T)
    space.add(body, shape)
    return shape

# All Pygame setup    
pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
draw_opt = pymunk.pygame_util.DrawOptions(screen)

# All Pymunk setup
space = pymunk.Space()
space.gravity = (0, 500)

# Creating static platforms
plat = []

plat.append(Create_static_platform(space, (300, 300), -250, 0, 0, -100, 5))

# Holds all created marbles
marble = []

# Core game loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            marble.append(Create_marble(space, event.pos))

    screen.fill((217, 217, 217))
    space.debug_draw(draw_opt)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)