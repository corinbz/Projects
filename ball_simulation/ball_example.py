import pygame

# Initialize all imported pygame modules
pygame.init()

# Set up the drawing window
reso = [500, 500]       # width x height in pixels, starting from top left corner
screen = pygame.display.set_mode(reso)

t = 0                   # start time = 0 seconds
dt = 0.1                # simulation change in time per loop (seconds)
g = 0.00381             # acceleration (rate of change of speed)
v_y = -0.0001           # starting speed in y direction
x = 250                 # starting x_position
y = 0                   # starting y_position

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 20)
    v_y += g * dt
    y += v_y * dt

    # Check if ball is still in the screen
    # If not, change position and velocity to original values
    if y >= 500 or y <= 0:
        y = 0
        v_y = -0.0001

    # Flip the display
    # Update the full display Surface to the screen
    pygame.display.flip()

# Done! Time to quit and close the window.
pygame.quit()
