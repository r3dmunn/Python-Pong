import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
font = pygame.font.Font("G7_Segment_7a.ttf", 85)
score_player = 0
score_bot = 0
clock = pygame.time.Clock()
running = True
dt = 0 #delta tiempo para el framerate

class player:
    def __init__(self):
        self.rect= pygame.Rect(60,240,20,80)
        self.sp = 300
        self.score = 0
    
    def move(self,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 300 * dt
        if keys[pygame.K_s]:
            self.rect.y += 300 * dt
    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255), self.rect)

class bot:
    def __init__(self):
        self.rect=pygame.Rect(1220,240,20,80)
        self.sp = 300
        self.score = 0
    def move(self,dt,ball):
        if self.rect.y < ball.rect.y:
            self.rect.y += self.sp*dt
        if self.rect.y > ball.rect.y:
            self.rect.y -= self.sp*dt
    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255), self.rect)

class ball:
    def __init__(self):
        self.rect= pygame.Rect(640,320,20,20)
        self.sp_x = 300
        self.sp_y = 300
    def move(self,dt):
        self.rect.y += self.sp_y*dt
        self.rect.x += self.sp_x*dt
    def collisionbox(self):
       if self.rect.top <= 0 or self.rect.bottom >= 720:
           self.sp_y *= -1
    def collision(self,player,bot):
        if self.rect.colliderect(player) or self.rect.colliderect(bot):
            self.sp_x *=-1
    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255), self.rect)
        
#crear instancias
player_ob = player()
bot_ob = bot()
ball_ob = ball()        



def point():
    global score_bot, score_player #global sirve para que Python no busque las variables dentro de la función, sino en todo el código
    if ball_ob.rect.x <= 0:
        score_bot += 1
        ball_ob.rect.x, ball_ob.rect.y = 640, 360
        bot_ob.rect.x,bot_ob.rect.y = 1220,240
        player_ob.rect.x,player_ob.rect.y = 185,360

    if ball_ob.rect.x >= 1280:
        score_player += 1
        ball_ob.rect.x, ball_ob.rect.y = 640, 360




#juegito
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #renderizado de la UI (fondo)
    screen.fill("black")
    pygame.draw.rect(screen,(255,255,255),(640,0,20,1280),40)
    i = 0
    for _ in range(12):
        pygame.draw.rect(screen,(0,0,0),(640,i,20,20),40)
        i += 72
    scoreboardplayer = font.render(f"{score_player}",True,(255,255,255))
    scoreboardbot = font.render(f"{score_bot}",True,(255,255,255))
    screen.blit(scoreboardplayer,(320,80))
    screen.blit(scoreboardbot,(960,80))
    
#se dibujan las entidades
    player_ob.draw(screen)
    bot_ob.draw(screen)
    ball_ob.draw(screen)
#enable movement
    player_ob.move(dt)
    bot_ob.move(dt,ball_ob)
    ball_ob.move(dt)
#enable collisions
    ball_ob.collisionbox()
    ball_ob.collision(player_ob,bot_ob)
    
    point()
    
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()