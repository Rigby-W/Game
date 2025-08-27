import pygame
import random
import time
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)
pygame.init()
screen_x=1280
screen_y=720
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_x, screen_y))
t0 = time.time()
running = True
dt = 0
player_size=10
score=0
highscore=0
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
class Apple_Purple(object):
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
        pygame.draw.circle(screen, "purple", (self.apple_pos_x,self.apple_pos_y) ,10)
apple_p=Apple_Purple()
apple_r=Apple_Red()
apple_g=Apple_Green()
speed=200
while running:
    t1=time.time()
    game_time = t1-t0
    game_time_min = round(game_time//60)
    game_time_sec = round(game_time%60)
    if highscore < score:
        highscore =+ score
    else:
        highscore += 0
    player_size==10
    score==0
    highscore==0
    if game_time_sec < 10:
        timer_surface = font.render(f"Time: {game_time_min}:0{game_time_sec}", True, (0, 0, 0))
    else:
        timer_surface = font.render(f"Time: {game_time_min}:{game_time_sec}", True, (0, 0, 0))
    highscore_surface = font.render(f"Highscore: {highscore}", True, (50, 50, 50))
    score_surface = font.render(f"Score: {score}", True, (50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #fill the screen first before you put your objects in
    screen.fill("blue")
    screen.blit(timer_surface, ((20), (15)))
    screen.blit(score_surface, ((20), (40)))
    screen.blit(highscore_surface, ((20), (65)))
    pygame.draw.circle(screen, "white", player_pos, player_size)
    apple_r.draw_apple()
    apple_g.draw_apple()
    apple_p.draw_apple()
    keys = pygame.key.get_pressed()
    #movement
    if (keys[pygame.K_w]  or keys[pygame.K_UP]) and player_pos.y>(player_size):
        player_pos.y -= speed * dt / (player_size/10)
        if player_size > 5:
            player_size -= 0.5*dt*(speed/200)
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player_pos.y<(screen_y-player_size):
        player_pos.y += speed * dt / (player_size/10)
        if player_size > 5:
            player_size -= 0.5*dt*(speed/200)
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_pos.x>(player_size):
        player_pos.x -= speed * dt / (player_size/10)
        if player_size > 5:
            player_size -= 0.5*dt*(speed/200)
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_pos.x<(screen_x-player_size):
        player_pos.x += speed * dt / (player_size/10)
        if player_size > 5:
            player_size -= 0.5*dt*(speed/200)
    #slowdown mechanic for when you go too fast
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] or (keys[pygame.K_LSHIFT] and keys[pygame.K_RSHIFT]):
        speed =+ 100
    if not (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] or (keys[pygame.K_LSHIFT] and keys[pygame.K_RSHIFT])):  
        speed =+ 200
    #reset mechanic
    if keys[pygame.K_r]:
        score=+0
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        player_size =+ 10
        t0 = t1
    #red apple being eaten
    if player_pos.x >= (apple_r.apple_pos_x-player_size) and player_pos.x <= (apple_r.apple_pos_x+player_size) and player_pos.y >= (apple_r.apple_pos_y-player_size) and player_pos.y <=(apple_r.apple_pos_y+player_size):
        score += round(player_size*2)
        if player_size < 50:
            player_size += 5
        apple_r.eat_apple()
    #green apple being eaten
    if player_pos.x >= (apple_g.apple_pos_x-player_size) and player_pos.x <= (apple_g.apple_pos_x+player_size) and player_pos.y >= (apple_g.apple_pos_y-player_size) and player_pos.y <=(apple_g.apple_pos_y+player_size) and player_size >= 15:
        score += round(score*0.25)
        player_size =+ 5
        apple_g.eat_apple()
    #purple apple being eaten
    if player_pos.x >= (apple_p.apple_pos_x-player_size) and player_pos.x <= (apple_p.apple_pos_x+player_size) and player_pos.y >= (apple_p.apple_pos_y-player_size) and player_pos.y <=(apple_p.apple_pos_y+player_size):
        #purple apple's "loot table" (a.k.a. what the apple does) 
        chance=random.randint(0,9)
        if chance == 0:
            score += round(player_size*2)
        elif chance == 1:
            score -= round(player_size*1.5)
        elif chance == 2:
            score += round(score*0.5)
        elif chance == 3:
            score -= round(score*0.5)
        elif chance == 4:
            player_size =+ 25
        elif chance == 5:
            if player_size > 10:
                player_size -= 5
            else:
                player_size =+ 5
        elif chance == 6:
            if player_size < 50:
                player_size += 5
            else:
                player_size =+ 50
        elif chance == 7:
            score += 0
        elif chance == 8:
            player_pos.x = random.randint(round(player_size), round(screen_x-player_size))
            player_pos.y = random.randint(round(player_size), round(screen_y-player_size))
            apple_r.eat_apple()
            apple_g.eat_apple()
        elif chance == 9:
            player_pos.x = random.randint(round(player_size), round(screen_x-player_size))
            player_pos.y = random.randint(round(player_size), round(screen_y-player_size))
        apple_p.eat_apple()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
