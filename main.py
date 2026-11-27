
import pygame
import random

pygame.init()

# Game Window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Balloon Burst")

clock = pygame.time.Clock()

# Balloon Colors
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


# Draw Clouds
def draw_cloud(x, y):
    pygame.draw.circle(screen, (220, 240, 255), (x, y), 22)
    pygame.draw.circle(screen, (255, 255, 255), (x + 25, y - 12), 28)
    pygame.draw.circle(screen, (255, 255, 255), (x + 55, y), 22)
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 55, 20))


# Draw Background
def draw_background():

    # Sky Gradient
    for y in range(600):
        color = (80, 180 + y // 15, 255)
        pygame.draw.line(screen, color, (0, y), (800, y))

    # Sun
    pygame.draw.circle(screen, (255, 225, 100), (690, 115), 45)

    # Clouds
    draw_cloud(100, 150)
    draw_cloud(570, 200)
    draw_cloud(350, 330)

    # Green Hills
    pygame.draw.ellipse(
        screen, (100, 205, 100),
        (-100, 510, 500, 180)
    )

    pygame.draw.ellipse(
        screen, (60, 180, 90),
        (350, 510, 600, 180)
    )


# Create Balloon
def create_balloon():

    x = random.randint(40, 760)
    y = 630
    color = random.choice(colors)
    speed = random.randint(1, 3)

    balloons.append([x, y, color, speed])


# Draw Balloon
def draw_balloon(x, y, color):

    # Balloon Shadow
    pygame.draw.ellipse(
        screen, (70, 100, 140),
        (x - 22, y - 27, 46, 60)
    )

    # Balloon Body
    pygame.draw.ellipse(
        screen, color,
        (x - 23, y - 30, 46, 60)
    )

    # Balloon Border
    pygame.draw.ellipse(
        screen, (255, 255, 255),
        (x - 23, y - 30, 46, 60), 2
    )

    # Light Shine
    pygame.draw.ellipse(
        screen, (255, 255, 255),
        (x - 13, y - 18, 9, 17)
    )

    pygame.draw.circle(
        screen, (255, 255, 255),
        (x - 8, y - 20), 4
    )

    # Balloon Knot
    pygame.draw.polygon(
        screen, color,
        [(x - 5, y + 28),
         (x + 5, y + 28),
         (x, y + 38)]
    )

    # Balloon String
    pygame.draw.line(
        screen, (255, 255, 255),
        (x, y + 38),
        (x + 3, y + 70), 2
    )


# Game Loop
running = True
last_balloon = 0

while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Background
    draw_background()

    # Game Title
    title = font.render(
        "BALLOON BURST",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (260, 25))

    # Create Balloons
    current_time = pygame.time.get_ticks()

    if current_time - last_balloon > 900:
        create_balloon()
        last_balloon = current_time

    # Move and Draw Balloons
    for balloon in balloons:

        balloon[1] -= balloon[3]

        draw_balloon(
            balloon[0],
            balloon[1],
            balloon[2]
        )

    # Remove Old Balloons
    balloons = [
        b for b in balloons
        if b[1] > -80
    ]

    pygame.display.update()
    clock.tick(60)


pygame.quit()
