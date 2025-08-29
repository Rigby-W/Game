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
game=0
while running:
    if game==0:
        keys = pygame.key.get_pressed()
        start_text="Press Space to start"
        start_font_x,start_font_y=font.size(start_text)
        start_surface=font.render(start_text, True, (200, 200, 200))
        font_size = 60
        my_font = pygame.font.SysFont("Arial", font_size)
        title_text="Apple Game"
        title_font_x,title_font_y=my_font.size(title_text)
        title_surface=my_font.render(title_text, True, (150, 50, 150))
        screen.fill((0, 0, 100))
        screen.blit(start_surface, ((screen_x/2-start_font_x/2), (screen_y/2-start_font_y/2)))
        screen.blit(title_surface, ((screen_x/2-title_font_x/2), (screen_y/4-title_font_y/2)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #shifting the screens
        if keys[pygame.K_SPACE]:
            game = 1
            t1=time.time()
            t0 =+ t1
        if keys[pygame.K_ESCAPE]:
            game = 2
        pygame.display.flip()
    if game==1:
        keys = pygame.key.get_pressed()
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
            timer_surface = font.render(f"Time: {game_time_min}:0{game_time_sec}", True, (200, 200, 200))
        else:
            timer_surface = font.render(f"Time: {game_time_min}:{game_time_sec}", True, (200, 200, 200))
        player_size_rounded = round(player_size)
        size_surface = font.render(f"Size: {player_size_rounded}", True, (200, 200, 200))
        highscore_surface = font.render(f"Highscore: {highscore}", True, (200, 200, 200))
        score_surface = font.render(f"Score: {score}", True, (200, 200, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #fill the screen first before you put your objects in
        screen.fill((0, 0, 100))
        screen.blit(timer_surface, ((20), (20)))
        screen.blit(score_surface, ((20), (50)))
        screen.blit(highscore_surface, ((20), (80)))
        screen.blit(size_surface, ((20), (110)))
        pygame.draw.circle(screen, "white", player_pos, player_size)
        apple_r.draw_apple()
        apple_g.draw_apple()
        apple_p.draw_apple()
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
        #screen shifting
        if keys[pygame.K_ESCAPE]:
            game = 2
        #red apple being eaten
        if player_pos.x >= (apple_r.apple_pos_x-player_size) and player_pos.x <= (apple_r.apple_pos_x+player_size) and player_pos.y >= (apple_r.apple_pos_y-player_size) and player_pos.y <=(apple_r.apple_pos_y+player_size):
            score += round(player_size*1.5)
            if player_size < 50:
                player_size += 5
            apple_r.eat_apple()
        #green apple being eaten
        if player_pos.x >= (apple_g.apple_pos_x-player_size) and player_pos.x <= (apple_g.apple_pos_x+player_size) and player_pos.y >= (apple_g.apple_pos_y-player_size) and player_pos.y <=(apple_g.apple_pos_y+player_size) and player_size_rounded >= 15:
            score += round(score*0.5)
            player_size =+ 5
            apple_g.eat_apple()
        #purple apple being eaten
        if player_pos.x >= (apple_p.apple_pos_x-player_size) and player_pos.x <= (apple_p.apple_pos_x+player_size) and player_pos.y >= (apple_p.apple_pos_y-player_size) and player_pos.y <=(apple_p.apple_pos_y+player_size):
            #purple apple's "loot table" (a.k.a. what the apple does) 
            chance=random.randint(0,9)
            if chance == 0:
                score += round(player_size*3)
            elif chance == 1:
                score -= round(player_size*2)
            elif chance == 2:
                score += score
            elif chance == 3:
                score -= round(score*0.5)
            elif chance == 4:
                player_size =+ 25
            elif chance == 5:
                if player_size > 15:
                    player_size -= 10
                else:
                    player_size =+ 5
            elif chance == 6:
                if player_size < 40:
                    player_size += 10
                else:
                    player_size =+ 50
            elif chance == 7:
                score += 0
            elif chance == 8:
                apple_r.eat_apple()
                apple_g.eat_apple()
            elif chance == 9:
                player_pos.x = random.randint(round(player_size), round(screen_x-player_size))
                player_pos.y = random.randint(round(player_size), round(screen_y-player_size))
            apple_p.eat_apple()
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    if game == 2:
        keys = pygame.key.get_pressed()
        start_text="Press Space to resume the game"
        line_1_text="Red Apple adds score based on size and increases size"
        line_2_text="Green Apple multiplies score by 1.5 and shrinks you down to the minimum size but you have to be at least size 15"
        line_3_text="Purple Apple does a random effect"
        start_font_x,start_font_y=font.size(start_text)
        line_1_x,line_1_y=font.size(line_1_text)
        line_2_x,line_2_y=font.size(line_2_text)
        line_3_x,line_3_y=font.size(line_3_text)
        start_surface=font.render(start_text, True, (200, 200, 200))
        line_1_surface=font.render(line_1_text, True, (200, 200, 200))
        line_2_surface=font.render(line_2_text, True, (200, 200, 200))
        line_3_surface=font.render(line_3_text, True, (200, 200, 200))
        screen.fill((0, 0, 100))
        screen.blit(start_surface, ((screen_x/2-start_font_x/2), (screen_y/8-start_font_y/2)))
        screen.blit(line_1_surface, ((screen_x/2-line_1_x/2), (screen_y/4+40-line_1_y/2)))
        screen.blit(line_2_surface, ((screen_x/2-line_2_x/2), (screen_y/4+80-line_2_y/2)))
        screen.blit(line_3_surface, ((screen_x/2-line_3_x/2), (screen_y/4+120-line_3_y/2)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        #shifting the screens
        if keys[pygame.K_SPACE]:
            game = 1
pygame.quit()
