# Use - ./a.out - to run in terminal
import sys
import math
import pygame
import time

# initialize pygame and other variables
pygame.init()

# Variables from CLI
filename = sys.argv[1] #passed from c++

# Pygame setup
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, 402))
with open(filename, 'r') as file:
    # First line is the number of gears
    MAX_GEAR = int(file.readline().strip())
    # Fill a vector with all the gear ratios
    gear_ratios = []
    lines_read = 0
    for line in file:
        gear_ratios.append(float(line.strip()))
        lines_read+=1
        if lines_read >= MAX_GEAR:
                break
    diff_ratio = float(file.readline().strip())
    tire_diam = float(file.readline().strip())
    red_line = int(file.readline().strip())

pygame.display.set_caption(filename + " | Speeds - " + str(MAX_GEAR))
font1 = pygame.font.SysFont("Times New Roman", 35)
vehicle_speed = 6 # MPH
gear = 0 # 1st gear

# Initialize colors and locations
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 300
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

'''
Writes text to the pygame screen
'''
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)
'''
Calculated the radian value of where the redline should start based on the input
Equation from https://mycurvefit.com/
'''
def calc_redline(red_line):
    rl = -9.081194 + (3.06383 - -9.081194)/(1 + (red_line/24092.42)**1.234789)
    return rl
'''
Draws the tachometer to the pygame screen
'''
def draw_tachometer(rpm, redline):
    screen.fill(BLACK)
    # Draw the outline of the tachometer
    pygame.draw.circle(screen, WHITE, (CENTER_X, CENTER_Y), RADIUS, 4)
    pygame.draw.arc(screen, RED, (CENTER_X-RADIUS, CENTER_Y-RADIUS, RADIUS*2, RADIUS*2), 6.28, calc_redline(red_line), 4)

    # Draw the ticks
    for angle in range(0, 360, 10):
        x1 = CENTER_X + int(RADIUS * math.cos(math.radians(angle)))
        y1 = CENTER_Y + int(RADIUS * math.sin(math.radians(angle)))
        x2 = CENTER_X + int((RADIUS - 10) * math.cos(math.radians(angle)))
        y2 = CENTER_Y + int((RADIUS - 10) * math.sin(math.radians(angle)))
        if angle > ((redline*180)/10000)+180 or angle == 0:
            pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 4)
        else:
            pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 4)

    # Draw the needle
    angle = 180 + (rpm/55.555)  # Adjusting angle based on RPM
    x2 = CENTER_X + int((RADIUS - 50) * math.cos(math.radians(angle)))
    y2 = CENTER_Y + int((RADIUS - 50) * math.sin(math.radians(angle)))
    pygame.draw.line(screen, RED, (CENTER_X, CENTER_Y), (x2, y2), 4)

    # Draw the needle base
    pygame.draw.circle(screen, WHITE, (CENTER_X, CENTER_Y+1), 4, 4)

'''
Calculates the current revolutions per minute of the engine
'''
def calculate_rpm(vehicle_speed, diff_ratio, gear_ratios, gear, tire_diam):
    rpm = (vehicle_speed * diff_ratio * gear_ratios[gear] * 336) / tire_diam
    return int(rpm)

'''
Writing the vehicle speed on the pygame screen
'''
def draw_speed(number):
    text_surface = font1.render(str(number) + " MPH", True, WHITE)
    screen.blit(text_surface, (10, 10)) 

'''
Writing the engine speed in (RPM) the pygame screen
'''
def draw_rpm(number):
    text_surface = font1.render(str(number) + " RPM", True, WHITE)
    screen.blit(text_surface, (325, 10)) 

'''
Writing current gear number the pygame screen
'''
def draw_gear(number):
    text_surface = font1.render("GEAR " + str(number+1), True, WHITE)
    screen.blit(text_surface, (670, 10)) 

# Game loop variables
running = True
gear = 0
# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses
    keys = pygame.key.get_pressed()
    # Shifting gears
    if keys[pygame.K_UP]:
        if gear < MAX_GEAR-1:
            gear += 1
            time.sleep(.3)
    if keys[pygame.K_DOWN]:
        if gear > 0:
            gear -= 1
            time.sleep(.3)
    # Accelerating or deccelerating the vehicle
    if keys[pygame.K_a]:
        if calculate_rpm((vehicle_speed+1), diff_ratio, gear_ratios, gear, tire_diam) < red_line + 200:
            vehicle_speed += .15
    if keys[pygame.K_d]:
        if vehicle_speed <= 0:
            vehicle_speed = 0
            time.sleep(.15)
        else:
            vehicle_speed -= .2

    # Stall
    if calculate_rpm(vehicle_speed, diff_ratio, gear_ratios, gear, tire_diam) < 300:
        running = False
    
    # Bad downshift
    if calculate_rpm(vehicle_speed, diff_ratio, gear_ratios, gear, tire_diam) > red_line + 300:
        vehicle_speed -= .2
    
    # Rev limiter
    if calculate_rpm(vehicle_speed, diff_ratio, gear_ratios, gear, tire_diam) > red_line:
        time.sleep(.06)
        vehicle_speed -=.05*(gear+1)
            
    # Updated and re-draw everything
    draw_tachometer(calculate_rpm(vehicle_speed, diff_ratio, gear_ratios, gear, tire_diam), red_line)
    draw_speed(int(vehicle_speed))
    draw_rpm(calculate_rpm(vehicle_speed, diff_ratio, gear_ratios, gear, tire_diam))
    draw_gear(gear)
    pygame.display.flip() 
    pygame.time.Clock().tick(60)