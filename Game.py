# Example file showing a circle moving on screen
import pygame
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)
# pygame setup
pygame.init()
screen_x=1280
screen_y=720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_size=10
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    start_time = pygame.time.get_ticks()
    game_time_sec = round(start_time/1000)%60
    game_time_min = round(start_time/1000)//60
    text_surface = font.render(f"{game_time_min}Minutes:{game_time_sec}Seconds", True, (0, 0, 0))
    player_size==10
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")
    screen.blit(text_surface, ((screen_x/2), (15)))
    pygame.draw.circle(screen, "white", player_pos, player_size)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y>32 or keys[pygame.K_UP] and player_pos.y>(player_size):
        player_pos.y -= 200 * dt / (player_size/10)
    if keys[pygame.K_s] and player_pos.y<690 or keys[pygame.K_DOWN] and player_pos.y<(screen_y-player_size):
        player_pos.y += 200 * dt / (player_size/10)
    if keys[pygame.K_a] and player_pos.x>32 or keys[pygame.K_LEFT] and player_pos.x>(player_size):
        player_pos.x -= 200 * dt / (player_size/10)
    if keys[pygame.K_d] and player_pos.x<1250 or keys[pygame.K_RIGHT] and player_pos.x<(screen_x-player_size):
        player_pos.x += 200 * dt / (player_size/10)
    if keys[pygame.K_z] and player_size > 5:
        player_size -= 0.1
    if keys[pygame.K_x] and player_size < 50:
        player_size += 0.1
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()
