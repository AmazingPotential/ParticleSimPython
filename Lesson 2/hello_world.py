x = 250
vx = -50
radius = 10
rate = 60 # frames per second
dt = 1/rate # Time step between frames
space_size = 500
color = (255, 255, 255)

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([space_size, space_size])

clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, color, (x, 250), radius)

    if ((x - radius) < 0) or ((x + radius) > space_size):
        vx = -vx

    # Flip the display
    pygame.display.flip()

    x = x + vx*dt

    # Limit frame rate to desired number of frames per second
    clock.tick(rate)

# Done! Time to quit.
pygame.quit()