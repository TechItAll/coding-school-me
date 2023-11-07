import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size to the maximum available resolution
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Set the font and font size
font = pygame.font.SysFont(None, 48)

# Set the text to display
text = font.render("Im board", True, (255, 255, 255))

# Set the initial position and velocity of the text
x = 0
y = 0
vel_x = 1
vel_y = 1

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the text
    x += vel_x
    y += vel_y

    # Bounce the text off the edges of the screen
    if x < 0 or x + text.get_width() > screen.get_width():
        vel_x = -vel_x
    if y < 0 or y + text.get_height() > screen.get_height():
        vel_y = -vel_y

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the text
    screen.blit(text, (x, y))

    # Update the screen
    pygame.display.update()
