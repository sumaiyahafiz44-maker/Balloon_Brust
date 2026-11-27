
import pygame
import random

pygame.init()

# Game Window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Balloon Burst")

clock = pygame.time.Clock()

colors = [
    (255, 55, 75),
    (255, 190, 30),
    (40, 140, 255),
    (70, 210, 100),
    (210, 80, 255),
    (255, 90, 170),
    (255, 130, 30)
]

balloons = []

font = pygame.font.SysFont("Arial", 38, bold=True)

def draw_cloud(x, y):
    pygame.draw.circle(screen, (220, 240, 255), (x, y), 22)
    pygame.draw.circle(screen, (255, 255, 255), (x + 25, y - 12), 28)
    pygame.draw.circle(screen, (255, 255, 255), (x + 55, y), 22)
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 55, 20))

def draw_background():

    
    for y in range(600):
        color = (80, 180 + y // 15, 255)
        pygame.draw.line(screen, color, (0, y), (800, y))

   
    pygame.draw.circle(screen, (255, 225, 100), (690, 115), 45)

    draw_cloud(100, 150)
    draw_cloud(570, 200)
    draw_cloud(350, 330)

   
    pygame.draw.ellipse(
        screen, (100, 205, 100),
        (-100, 510, 500, 180)
    )

    pygame.draw.ellipse(
        screen, (60, 180, 90),
        (350, 510, 600, 180)
    )


def create_balloon():

    x = random.randint(40, 760)
    y = 630
    color = random.choice(colors)
    speed = random.randint(1, 3)

    balloons.append([x, y, color, speed])


def draw_balloon(x, y, color):

    pygame.draw.ellipse(
        screen, (70, 100, 140),
        (x - 22, y - 27, 46, 60)
    )

    pygame.draw.ellipse(
        screen, color,
        (x - 23, y - 30, 46, 60)
    )

  
    pygame.draw.ellipse(
        screen, (255, 255, 255),
        (x - 23, y - 30, 46, 60), 2
    )

    pygame.draw.ellipse(
        screen, (255, 255, 255),
        (x - 13, y - 18, 9, 17)
    )

    pygame.draw.circle(
        screen, (255, 255, 255),
        (x - 8, y - 20), 4
    )

    pygame.draw.polygon(
        screen, color,
        [(x - 5, y + 28),
         (x + 5, y + 28),
         (x, y + 38)]
    )

  
    pygame.draw.line(
        screen, (255, 255, 255),
        (x, y + 38),
        (x + 3, y + 70), 2
    )



running = True
last_balloon = 0

while running:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    draw_background()

    title = font.render(
        "BALLOON BURST",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (260, 25))


    current_time = pygame.time.get_ticks()

    if current_time - last_balloon > 900:
        create_balloon()
        last_balloon = current_time

    for balloon in balloons:

        balloon[1] -= balloon[3]

        draw_balloon(
            balloon[0],
            balloon[1],
            balloon[2]
        )

    balloons = [
        b for b in balloons
        if b[1] > -80
    ]

    pygame.display.update()
    clock.tick(60)


pygame.quit()
