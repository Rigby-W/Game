import pygame
import random
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)
pygame.init()
screen_x=1280
screen_y=720
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
running = True
dt = 0
player_size=10
score=0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
class Apple_Red(object):
    def eat_apple(self):
        self.eaten = True
        self.spawn_apple()
        self.eaten = False
    def __init__(self):
        self.eaten = False
        self.spawn_apple()
    def spawn_apple(self):
        self.apple_pos_x=random.randint(8,(screen_x-8))
        self.apple_pos_y=random.randint(8,(screen_y-8))
    def draw_apple(self):
        pygame.draw.circle(screen, "red", (self.apple_pos_x,self.apple_pos_y) ,8)
class Apple_Green(object):
    def eat_apple(self):
        self.eaten = True
        self.spawn_apple()
        self.eaten = False
    def __init__(self):
        self.eaten = False
        self.spawn_apple()
    def spawn_apple(self):
        self.apple_pos_x=random.randint(8,(screen_x-8))
        self.apple_pos_y=random.randint(8,(screen_y-8))
    def draw_apple(self):
        pygame.draw.circle(screen, "green", (self.apple_pos_x,self.apple_pos_y) ,12)
apple_r=Apple_Red()
apple_g=Apple_Green()
while running:
    start_time = pygame.time.get_ticks()
    game_time_sec = round(start_time/1000)%60
    game_time_min = round(start_time/1000)//60
    if game_time_sec < 10:
        timer_surface = font.render(f"Time: {game_time_min}:0{game_time_sec}", True, (0, 0, 0))
    else:
        timer_surface = font.render(f"Time: {game_time_min}:{game_time_sec}", True, (0, 0, 0))
    player_size==10
    score==0
    score_surface = font.render(f"Score: {score}", True, (50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("blue")
    screen.blit(timer_surface, ((20), (15)))
    screen.blit(score_surface, ((20), (40)))
    pygame.draw.circle(screen, "white", player_pos, player_size)
    apple_r.draw_apple()
    apple_g.draw_apple()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y>(player_size) or keys[pygame.K_UP] and player_pos.y>(player_size):
        player_pos.y -= 200 * dt / (player_size/10)
        if player_size > 5:
            player_size -= 0.5*dt
    if keys[pygame.K_s] and player_pos.y<(screen_y-player_size) or keys[pygame.K_DOWN] and player_pos.y<(screen_y-player_size):
        player_pos.y += 200 * dt / (player_size/10)
        if player_size > 5:
            player_size -= 0.5*dt
    if keys[pygame.K_a] and player_pos.x>(player_size) or keys[pygame.K_LEFT] and player_pos.x>(player_size):
        player_pos.x -= 200 * dt / (player_size/10)
        if player_size > 5:
            player_size -= 0.5*dt
    if keys[pygame.K_d] and player_pos.x<(screen_x-player_size) or keys[pygame.K_RIGHT] and player_pos.x<(screen_x-player_size):
        player_pos.x += 200 * dt / (player_size/10)
        if player_size > 5:
            player_size -= 0.5*dt
    if keys[pygame.K_z] and player_size > 5:
        player_size -= 5*dt
    if keys[pygame.K_x] and player_size < 50:
        player_size += 5*dt
    if player_pos.x >= (apple_r.apple_pos_x-player_size) and player_pos.x <= (apple_r.apple_pos_x+player_size) and player_pos.y >= (apple_r.apple_pos_y-player_size) and player_pos.y <=(apple_r.apple_pos_y+player_size):
        score += round(player_size*2)
        if player_size < 50:
            player_size += 5
        apple_r.eat_apple()
    if player_pos.x >= (apple_g.apple_pos_x-player_size) and player_pos.x <= (apple_g.apple_pos_x+player_size) and player_pos.y >= (apple_g.apple_pos_y-player_size) and player_pos.y <=(apple_g.apple_pos_y+player_size) and player_size >= 15:
        score += round(score*0.25)
        player_size =+ 5
        apple_g.eat_apple()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
