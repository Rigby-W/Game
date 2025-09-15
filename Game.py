import pygame
import random
import time
pygame.font.init()
base_font = pygame.font.SysFont("Arial", 25)
pygame.init()
screen_x_speed=1280
screen_y_speed=720
screen_x=1280
screen_y=720
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)
t0 = time.time()
running = True
dt = 0
score=0
highscore=0
player_size=10
player_pos=pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
display_pos=pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
skin="Normal"
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
class Player(object):
    def __init__(self):
        self.player_pos=player_pos 
        self.player_size=player_size
    def draw_skin1(self):
        pygame.draw.circle(screen, (120,120,120), self.player_pos, player_size)
        pygame.draw.circle(screen, (250,250,250), self.player_pos, player_size/1.5)
    def draw_skin2(self):
        pygame.draw.circle(screen, "white", self.player_pos, player_size)
    def draw_skin3(self):
        pygame.draw.circle(screen, (150,0,0), self.player_pos, player_size)
        pygame.draw.circle(screen, (0,0,0), self.player_pos, player_size/1.5)
    def draw_skin4(self):
        pygame.draw.circle(screen, (50,50,255), self.player_pos, player_size)
        pygame.draw.circle(screen, (255,255,255), self.player_pos, player_size/1.5)
        pygame.draw.circle(screen, (255,153,10), self.player_pos, player_size/2.25)
    def draw_skin5(self):
        pygame.draw.circle(screen, (255,255,255), self.player_pos, player_size)
        pygame.draw.circle(screen, (255,250,105), self.player_pos, player_size/1.5)
        pygame.draw.circle(screen, (255,153,10), self.player_pos, player_size/2.25)
    def draw_skin6(self):
        pygame.draw.circle(screen, (170,250,255), self.player_pos, player_size)
        pygame.draw.circle(screen, (100,0,0), self.player_pos, player_size*0.75)
        pygame.draw.circle(screen, (0,0,100), self.player_pos, player_size*0.5)
        pygame.draw.circle(screen, (255, 120, 120), self.player_pos, player_size*0.25)
class Display_Player(object):
    def __init__(self):
        self.player_pos=display_pos
    def draw_skin1(self):
        pygame.draw.circle(screen, (120,120,120), self.player_pos, display_size)
        pygame.draw.circle(screen, (250,250,250), self.player_pos, display_size/1.5)
    def draw_skin2(self):
        pygame.draw.circle(screen, "white", self.player_pos, display_size)
    def draw_skin3(self):
        pygame.draw.circle(screen, (150,0,0), self.player_pos, display_size)
        pygame.draw.circle(screen, (0,0,0), self.player_pos, display_size/1.5)
    def draw_skin4(self):
        pygame.draw.circle(screen, (50,50,255), self.player_pos, display_size)
        pygame.draw.circle(screen, (255,255,255), self.player_pos, display_size/1.5)
        pygame.draw.circle(screen, (255,153,10), self.player_pos, display_size/2.25)
    def draw_skin5(self):
        pygame.draw.circle(screen, (255,255,255), self.player_pos, display_size)
        pygame.draw.circle(screen, (255,250,105), self.player_pos, display_size/1.5)
        pygame.draw.circle(screen, (255,153,10), self.player_pos, display_size/2.25)
    def draw_skin6(self):
        pygame.draw.circle(screen, (170,250,255), self.player_pos, display_size)
        pygame.draw.circle(screen, (100,0,0), self.player_pos, display_size*0.75)
        pygame.draw.circle(screen, (0,0,100), self.player_pos, display_size*0.5)
        pygame.draw.circle(screen, (255, 120, 120), self.player_pos, display_size*0.25)
apple_p=Apple_Purple()
apple_r=Apple_Red()
apple_g=Apple_Green()
player=Player()
display=Display_Player()
max_speed=200
game=0
while running:
    if game==0:
        mouse_pos_x, mouse_pos_y=pygame.mouse.get_pos()
        title_font_size = 60
        title_font = pygame.font.SysFont("Arial", title_font_size)
        keys = pygame.key.get_pressed()
        start_text="Press Space to start"
        start_font_x,start_font_y=base_font.size(start_text)
        start_surface=base_font.render(start_text, True, (200, 200, 200))
        title_text="Orbs and Apples"
        title_font_x,title_font_y=title_font.size(title_text)
        title_surface=title_font.render(title_text, True, (175, 75, 175))
        hint_text="Hint"
        hint_font_x,hint_font_y=base_font.size(hint_text)
        hint_surface=base_font.render(hint_text, True, (100, 75, 75))
        screen.fill((0, 0, 100))
        screen.blit(start_surface, ((screen_x/2-start_font_x/2), (screen_y/2-start_font_y/2)))
        screen.blit(title_surface, ((screen_x/2-title_font_x/2), (screen_y/4-title_font_y/2)))
        screen.blit(hint_surface, ((45), (45)))
        pygame.draw.circle(screen, (100, 100, 100), (screen_x/2,screen_y/3+20), 25)
        mouse=pygame.mouse.get_pressed(num_buttons=3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_x, screen_y = event.size
                screen = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)
        #shifting the screens
        if keys[pygame.K_SPACE]:
            game = 1
            t1=time.time()
            t0 =+ t1
            apple_r.eat_apple()
            apple_g.eat_apple()
            apple_p.eat_apple()
        if (mouse_pos_x<(45+hint_font_x) and mouse_pos_x>(45) and mouse_pos_y<(45+hint_font_y) and mouse_pos_y>(45) and mouse[0]):
            game = 2
        if (mouse_pos_x>(screen_x/2-25) and mouse_pos_x<(screen_x/2+25) and mouse_pos_y>(screen_y/3-5) and mouse_pos_y<(screen_y/3+45) and mouse[0]):
            game = 3
            t1=time.time()
            t0 =+ t1
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
        score==0
        highscore==0
        if game_time_sec < 10:
            timer_surface =base_font.render(f"Time: {game_time_min}:0{game_time_sec}", True, (200, 200, 200))
        else:
            timer_surface =base_font.render(f"Time: {game_time_min}:{game_time_sec}", True, (200, 200, 200))
        player_size_rounded = round(player_size)
        size_surface =base_font.render(f"Size: {player_size_rounded}", True, (200, 200, 200))
        highscore_surface =base_font.render(f"Highscore: {highscore}", True, (200, 200, 200))
        score_surface =base_font.render(f"Score: {score}", True, (200, 200, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_x, screen_y = event.size
                screen = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)
        #fill the screen first before you put your objects in
        screen.fill((0, 0, 100))
        screen.blit(timer_surface, ((20), (20)))
        screen.blit(score_surface, ((20), (45)))
        screen.blit(highscore_surface, ((20), (70)))
        screen.blit(size_surface, ((20), (95)))
        if skin=="Normal":
            player.draw_skin1()
        elif skin=="Classic":
            player.draw_skin2()
        elif skin=="Dark":
            player.draw_skin3()
        elif skin=="Kevin":
            player.draw_skin4()
        elif skin=="Egg":
            player.draw_skin5()
        elif skin=="Mentor":
            player.draw_skin6()
        apple_r.draw_apple()
        apple_g.draw_apple()
        apple_p.draw_apple()
        #movement
        if (keys[pygame.K_w]  or keys[pygame.K_UP]):
            if player_pos.y>(0):
                player_pos.y -= speed * dt / (player_size/10) * (screen_y/screen_y_speed)
                if player_size > 5:
                    player_size -= 0.05*(player_size-5)*dt*(speed/200)
            else:
                player_pos.y =+ (screen_y)
                if player_size > 5:
                    player_size -= 0.05*(player_size-5)*dt*(speed/200)
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]): 
            if player_pos.y<(screen_y):
                player_pos.y += speed * dt / (player_size/10) * (screen_y/screen_y_speed)
                if player_size > 5:
                    player_size -= 0.05*(player_size-5)*dt*(speed/200)
            else:
                player_pos.y =+ 0
                if player_size > 5:
                    player_size -= 0.05*(player_size-5)*dt*(speed/200)
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]): 
            if player_pos.x>(0):
                player_pos.x -= speed * dt / (player_size/10) * (screen_x/screen_x_speed)
                if player_size > 5:
                    player_size -= 0.05*(player_size-5)*dt*(speed/200)
            else: 
                player_pos.x =+ (screen_x)
                if player_size > 5:
                    player_size -= 0.05*(player_size-5)*dt*(speed/200)
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]): 
            if player_pos.x<(screen_x):
                player_pos.x += speed * dt / (player_size/10) * (screen_x/screen_x_speed)
                if player_size > 5:
                    player_size -= 0.05*(player_size-5)*dt*(speed/200)
            else:        
                player_pos.x =+ 0
                if player_size > 5:
                    player_size -= 0.05*(player_size-5)*dt*(speed/200)
        #slowdown mechanic for when you go too fast
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] or (keys[pygame.K_LSHIFT] and keys[pygame.K_RSHIFT]):
            speed =+ (max_speed/3)
        if not (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] or (keys[pygame.K_LSHIFT] and keys[pygame.K_RSHIFT])):  
            speed =+ max_speed
        #reset mechanic
        if keys[pygame.K_r]:
            score=+0
            player_pos=+pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
            player_size =+ 10
            t0 = t1
            player.__init__()
        #screen shifting
        if keys[pygame.K_ESCAPE]:
            game = 0
        #red apple being eaten
        if player_pos.x >= (apple_r.apple_pos_x-player_size) and player_pos.x <= (apple_r.apple_pos_x+player_size) and player_pos.y >= (apple_r.apple_pos_y-player_size) and player_pos.y <=(apple_r.apple_pos_y+player_size):
            score += round(player_size*1.5)
            player_size += 5*(player_size/10)
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
                score += round(score*player_size/10)
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
                player_size += player_size
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
        start_text="Press Escape to Exit to Main Menu"
        line_1_text="Red Apple: adds score based on size and increases size"
        line_2_text="Green Apple: 1.5x score and lowers size if size is more than or at 15"
        line_3_text="Purple Apple: does a random effect"
        line_4_text="Arrows or WASD to move"
        line_5_text="Shift to Slowdown (doesnt slow the timer)"
        line_6_text="You lose size when you move"
        line_7_text="More size = More points"
        line_8_text="Less size = More speed"
        line_9_text="Get as many points as you can and aim for a high score"
        start_font_x,start_font_y=base_font.size(start_text)
        line_1_x,line_1_y=base_font.size(line_1_text)
        line_2_x,line_2_y=base_font.size(line_2_text)
        line_3_x,line_3_y=base_font.size(line_3_text)
        line_4_x,line_4_y=base_font.size(line_4_text)
        line_5_x,line_5_y=base_font.size(line_5_text)
        line_6_x,line_6_y=base_font.size(line_6_text)
        line_7_x,line_7_y=base_font.size(line_7_text)
        line_8_x,line_8_y=base_font.size(line_8_text)
        line_9_x,line_9_y=base_font.size(line_9_text)
        start_surface=base_font.render(start_text, True, (200, 200, 200))
        line_1_surface=base_font.render(line_1_text, True, (200, 200, 200))
        line_2_surface=base_font.render(line_2_text, True, (200, 200, 200))
        line_3_surface=base_font.render(line_3_text, True, (200, 200, 200))
        line_4_surface=base_font.render(line_4_text, True, (200, 200, 200))
        line_5_surface=base_font.render(line_5_text, True, (200, 200, 200))
        line_6_surface=base_font.render(line_6_text, True, (200, 200, 200))
        line_7_surface=base_font.render(line_7_text, True, (200, 200, 200))
        line_8_surface=base_font.render(line_8_text, True, (200, 200, 200))
        line_9_surface=base_font.render(line_9_text, True, (200, 200, 200))
        screen.fill((0, 0, 100))
        screen.blit(start_surface, ((screen_x/2-start_font_x/2), (screen_y/8-start_font_y/2)))
        screen.blit(line_1_surface, ((screen_x/2-line_1_x/2), (screen_y/4+(30*1)-line_1_y/2)))
        screen.blit(line_2_surface, ((screen_x/2-line_2_x/2), (screen_y/4+(30*2)-line_2_y/2)))
        screen.blit(line_3_surface, ((screen_x/2-line_3_x/2), (screen_y/4+(30*3)-line_3_y/2)))
        screen.blit(line_4_surface, ((screen_x/2-line_4_x/2), (screen_y/4+(30*4)-line_4_y/2)))
        screen.blit(line_5_surface, ((screen_x/2-line_5_x/2), (screen_y/4+(30*5)-line_5_y/2)))
        screen.blit(line_6_surface, ((screen_x/2-line_6_x/2), (screen_y/4+(30*6)-line_6_y/2)))
        screen.blit(line_7_surface, ((screen_x/2-line_7_x/2), (screen_y/4+(30*7)-line_7_y/2)))
        screen.blit(line_8_surface, ((screen_x/2-line_8_x/2), (screen_y/4+(30*8)-line_8_y/2)))
        screen.blit(line_9_surface, ((screen_x/2-line_9_x/2), (screen_y/4+(30*9)-line_9_y/2)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_x, screen_y = event.size
                screen = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)
        pygame.display.flip()
        #shifting the screens
        if keys[pygame.K_ESCAPE]:
            game = 0
    if game==3:
        display_size=+30
        display_pos=pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        keys = pygame.key.get_pressed()
        mouse_pos_x, mouse_pos_y=pygame.mouse.get_pos()
        mouse=pygame.mouse.get_pressed(num_buttons=3)
        screen.fill((0, 0, 100))
        line_1_text="Press Escape to Exit to Main Menu"
        line_1_x,line_1_y=base_font.size(line_1_text)
        line_1_surface=base_font.render(line_1_text, True, (200, 200, 200))
        screen.blit(line_1_surface, ((screen_x/2-line_1_x/2), (screen_y/8+(30*1)-line_1_y/2)))
        line_2_text=f"Speed={max_speed}"
        line_2_x,line_2_y=base_font.size(line_2_text)
        line_2_surface=base_font.render(line_2_text, True, (200, 200, 200))
        screen.blit(line_2_surface, ((screen_x/2-line_2_x/2), (screen_y/4+(30*1)-line_2_y/2)))
        speed_1_text="Slow"
        speed_1_x,speed_1_y=base_font.size(speed_1_text)
        speed_1_surface=base_font.render(speed_1_text, True, (200, 200, 200))
        screen.blit(speed_1_surface, ((screen_x/2-speed_1_x/2-80), (screen_y/4+(30*2)-speed_1_y/2)))
        speed_2_text="Medium"
        speed_2_x,speed_2_y=base_font.size(speed_2_text)
        speed_2_surface=base_font.render(speed_2_text, True, (200, 200, 200))
        screen.blit(speed_2_surface, ((screen_x/2-speed_2_x/2), (screen_y/4+(30*2)-speed_2_y/2)))
        speed_3_text="Fast"
        speed_3_x,speed_3_y=base_font.size(speed_3_text)
        speed_3_surface=base_font.render(speed_3_text, True, (200, 200, 200))
        screen.blit(speed_3_surface, ((screen_x/2-speed_3_x/2+80), (screen_y/4+(30*2)-speed_3_y/2)))
        if mouse_pos_x<=(screen_x/2-speed_1_x/2-40) and mouse_pos_x>=(screen_x/2-speed_1_x/2-80) and mouse_pos_y>=(screen_y/4+(30*2)-speed_2_y/2) and mouse_pos_y<=(screen_y/4+(30*2)-speed_2_y/2+20) and mouse[0]:
            max_speed=100
        if mouse_pos_x<=(screen_x/2-speed_2_x/2+70) and mouse_pos_x>=(screen_x/2-speed_2_x/2) and mouse_pos_y>=(screen_y/4+(30*2)-speed_2_y/2) and mouse_pos_y<=(screen_y/4+(30*2)-speed_2_y/2+20) and mouse[0]:
            max_speed=200
        if mouse_pos_x<=(screen_x/2-speed_3_x/2+120) and mouse_pos_x>=(screen_x/2-speed_3_x/2+80) and mouse_pos_y>=(screen_y/4+(30*2)-speed_2_y/2) and mouse_pos_y<=(screen_y/4+(30*2)-speed_2_y/2+20) and mouse[0]:
            max_speed=400
        line_3_text=f"Skin Selector"
        line_3_x,line_3_y=base_font.size(line_3_text)
        line_3_surface=base_font.render(line_3_text, True, (200, 200, 200))
        screen.blit(line_3_surface, ((screen_x/2-line_3_x/2), (screen_y/4+(30*3)-line_3_y/2)))
        left_arrow_text="<"
        left_arrow_x,left_arrow_y=base_font.size(left_arrow_text)
        left_arrow_surface=base_font.render(left_arrow_text, True, (200, 200, 200))
        screen.blit(left_arrow_surface, ((screen_x/2-left_arrow_x/2-80), (screen_y/4+(30*4)-left_arrow_y/2)))
        skin_text=f"{skin}"
        skin_x,skin_y=base_font.size(skin_text)
        skin_surface=base_font.render(skin_text, True, (200, 200, 200))
        screen.blit(skin_surface, ((screen_x/2-skin_x/2), (screen_y/4+(30*4)-skin_y/2)))
        right_arrow_text=">"
        right_arrow_x,right_arrow_y=base_font.size(right_arrow_text)
        right_arrow_surface=base_font.render(right_arrow_text, True, (200, 200, 200))
        screen.blit(right_arrow_surface, ((screen_x/2-right_arrow_x/2+80), (screen_y/4+(30*4)-right_arrow_y/2)))
        if mouse_pos_x<=(screen_x/2-left_arrow_x/2-68) and mouse_pos_x>=(screen_x/2-left_arrow_x/2-80) and mouse_pos_y>=(screen_y/4+(30*4)-left_arrow_y/2) and mouse_pos_y<=(screen_y/4+(30*4)-left_arrow_y/2+20) and mouse[0] and not_press == True:
            not_press = False
            if skin=="Normal":
                skin="Normal"
            elif skin=="Classic":
                skin="Normal"
            elif skin=="Dark":
                skin="Classic"
            elif skin=="Kevin":
                skin="Dark"
            elif skin=="Egg":
                skin="Kevin"
            elif skin=="Mentor":
                skin="Egg"
        if mouse_pos_x<=(screen_x/2-right_arrow_x/2+92) and mouse_pos_x>=(screen_x/2-right_arrow_x/2+80) and mouse_pos_y>=(screen_y/4+(30*4)-right_arrow_y/2) and mouse_pos_y<=(screen_y/4+(30*4)-right_arrow_y/2+20) and mouse[0] and not_press == True:
            not_press = False
            if skin=="Normal":
                skin="Classic"
            elif skin=="Classic":
                skin="Dark"
            elif skin=="Dark":
                skin="Kevin"
            elif skin=="Kevin":
                skin="Egg"
            elif skin=="Egg":
                skin="Mentor"
            elif skin=="Mentor":
                skin="Mentor"
        if not mouse[0]:
            not_press = True
        if skin=="Normal":
            display.draw_skin1()
        elif skin=="Classic":
            display.draw_skin2()
        elif skin=="Dark":
            display.draw_skin3()
        elif skin=="Kevin":
            display.draw_skin4()
        elif skin=="Egg":
            display.draw_skin5()
        elif skin=="Mentor":
            display.draw_skin6()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_x, screen_y = event.size
                screen = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE)
        pygame.display.flip()
        #shifting the screens
        if keys[pygame.K_ESCAPE]:
            game=0
pygame.quit()
