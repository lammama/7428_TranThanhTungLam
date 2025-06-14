import pygame
pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
gravity = 0
player_y = 300
jumping = False

while True:
    screen.fill((135, 206, 235))  # màu trời

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and not jumping:
            if event.key == pygame.K_SPACE:
                gravity = -15
                jumping = True

    gravity += 1
    player_y += gravity
    if player_y >= 300:
        player_y = 300
        jumping = False

    pygame.draw.rect(screen, (255, 0, 0), (100, player_y, 50, 50))  # hình đại diện Mario
    pygame.display.update()
    clock.tick(60)
