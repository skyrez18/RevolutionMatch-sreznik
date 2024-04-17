# Use - ./a.out - to run in terminal
import sys
import math
import pygame

# initialize pygame and other variables
pygame.init()

# Variables from CLI
filename = sys.argv[1] #passed from c++

# Pygame setup
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
with open(filename, 'r') as file:
    # First line is the number of gears
    MAX_GEAR = file.readline()
    # Fill a vector with all the gear ratios
    gear_ratios = []
    lines_read = 0
    for line in file:
        gear_ratios.append(float(line.strip()))
        lines_read+=1
        if lines_read >= MAX_GEAR:
                break

pygame.display.set_caption("Speeds - " + MAX_GEAR)
font1 = pygame.font.SysFont("Times New Roman", 35)
vehicle_speed = 0
diff_ratio = 0
tire_diam = 0
gear = 0
speed = 0
rpm = (vehicle_speed * diff_ratio * gear_ratios[gear] * 336) / tire_diam



# Initialize colors and locations
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 300
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# TODO: use key inputs to also toggle the current speed of the vehicle


'''
Writes text to the pygame screen
'''
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_tachometer(rpm):
    screen.fill(BLACK)
    # Draw the outline of the tachometer
    pygame.draw.circle(screen, BLACK, (CENTER_X, CENTER_Y), RADIUS, 2)

    # Draw the ticks
    for angle in range(0, 360, 10):
        x1 = CENTER_X + int(RADIUS * math.cos(math.radians(angle)))
        y1 = CENTER_Y + int(RADIUS * math.sin(math.radians(angle)))
        x2 = CENTER_X + int((RADIUS - 10) * math.cos(math.radians(angle)))
        y2 = CENTER_Y + int((RADIUS - 10) * math.sin(math.radians(angle)))
        pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)

    # Draw the needle
    angle = 180 - (rpm / 7000) * 180  # Adjusted angle based on RPM
    x2 = CENTER_X + int((RADIUS - 50) * math.cos(math.radians(angle)))
    y2 = CENTER_Y + int((RADIUS - 50) * math.sin(math.radians(angle)))
    pygame.draw.line(screen, RED, (CENTER_X, CENTER_Y), (x2, y2), 4)

# Game loop variables
running = True
gear = 1
# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses
    # TODO: Prevent 'money shifts'
    keys = pygame.key.get_pressed()
    # Shifting gears
    if keys[pygame.K_UP]:
        # TODO: is this the correct math?
        if gear > MAX_GEAR-1:
            gear += 1
    if keys[pygame.K_DOWN]:
        if gear > MAX_GEAR:
            gear -= 1
    # Accelerating or deccelerating the vehicle
    if keys[pygame.K_a]:
        speed += 1
    if keys[pygame.K_d]:
        if speed <= 0:
            speed = 0
        else:
            speed -= 1

    draw_tachometer(rpm)

    pygame.display.flip() 
    pygame.time.Clock().tick(60)
