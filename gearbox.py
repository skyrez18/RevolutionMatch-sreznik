# you will need to install cv2
# Run "pip3 install opencv-python" in CLI - DONE

# Use - ./a.out - to run in terminal
import cv2
import sys
import time
import numpy as np
import random
import pygame

# initialize pygame and other variables
pygame.init()
rpm = 900

# Variables from CLI
filename = sys.argv[1] #passed from c++
MAX_GEAR = int(sys.argv[2]) #passed from c++

# TODO: use key inputs to also toggle the current speed of the vehicle


'''
Writes text to the pygame screen
'''
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    game_screen.blit(text_surface, text_rect)

# Pygame setup
WIDTH, HEIGHT = 800, 800
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Speeds - " + MAX_GEAR)
# Citation #2 - Set fonts - https://github.com/search?q=pygame.font.SysFont+language%3APython&type=Code&l=Python
countdown_font = pygame.font.SysFont("Times New Roman", 35)

# Game loop variables
running = True
gear = 1
# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Dont record score


    # Check for key presses
    # TODO: Prevent 'money shifts'
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        # TODO: Check there is a higher gear
        if gear > MAX_GEAR:
            # TODO: Change the gear number
            gear += 1
            time.sleep(.12)
    if keys[pygame.K_DOWN]:
        # TODO: Check there is a lower gear
        if gear > MAX_GEAR:
            # TODO: Change the gear number
            gear -= 1
            time.sleep(.12)


    pygame.display.flip() 
    pygame.time.Clock().tick(60)
