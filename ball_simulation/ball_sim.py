import pygame as pg

pg.init()
screen = pg.display.set_mode((500, 500))
GREEN = (123, 182, 97)
RED = (227, 38, 54)
pg.display.set_caption("Ball simulation")
running = True

t = 0  # Time start
dt = 0.01  # Time step
vy = -10  # Starting speed
y = 400  # Start altitude
G = 9.81  # Acceleration
x = 100  # y position
m = 2  # mass
F = m * G  # Force
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    Keys = pg.key.get_pressed()
    if Keys[pg.K_RETURN] and y <= 400:
        a = F * dt
        vy += a * dt
        y += vy * dt
    screen.fill((173, 216, 230))
    pg.draw.rect(screen, GREEN, (0, 400, 500, 100))
    pg.draw.circle(screen, RED, (int(x), int(y)), 10)

    print(y)

    pg.display.flip()

pg.quit()