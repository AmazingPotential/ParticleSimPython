# Particle 1
x1 = 125
vx1 = -50
r1 = 10
m1 = 1
c1 = (255, 0, 0)

# Particle 2
x2 = 375
vx2 = -50
r2 = 100
m2 = 100
c2 = (0, 0, 255)

# Simulation parameters
rate = 60 # frames per second
dt = 1/rate # Time step between frames
space_size = 500

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

    # Fill the background with black
    screen.fill((0, 0, 0))

    # Draw a solid white circle in the center for particle 1
    pygame.draw.circle(screen, c1, (x1, 250), r1)

    # Draw a solid white circle in the center for particle 2
    pygame.draw.circle(screen, c2, (x2, 250), r2)

    # Handling particle-to-particle collisions
    if (abs(x2-x1) < (r1+r2)):
        ux1, ux2 = vx1, vx2
        
        vx1 = ux1 * (m1 - m2)/(m1 + m2) + 2 * ux2 * m2/(m1 + m2)
        vx2 = 2 * ux1 * m1/(m1 + m2) + ux2 * (m2 - m1)/(m1 + m2)

    # Handling wall collisions for particle 1
    if ((x1 - r1) < 0) or ((x1 + r1) > space_size):
        vx1 = -vx1

    # Handling wall collisions for particle 2
    if ((x2 - r2) < 0) or ((x2 + r2) > space_size):
        vx2 = -vx2

    # Flip the display
    pygame.display.flip()

    # Dynamics for particle 1
    x1 = x1 + vx1*dt

    # Dynamics for particle 2
    x2 = x2 + vx2*dt

    # Limit frame rate to desired number of frames per second
    clock.tick(rate)

# Done! Time to quit.
pygame.quit()