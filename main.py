import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
font = pygame.font.Font("G7_Segment_7a.ttf", 85)
score_player = 0
score_bot = 0
clock = pygame.time.Clock()
running = True
dt = 0 #delta tiempo para el framerate

#posicion del bot
botx = 1220
boty = 240
bot_sp = 250

#posicion del jugador
playerx = 185
playery = 360

#pelotita
ballx = 640
bally = 320
ball_sp_x = 300
ball_sp_y = 300
ball_sz = 15


while running:
    player_ps= (playerx,playery, 20,80 )
    bot_ps = (botx,boty,20,80)
    ball_ps = (ballx, bally, ball_sz, ball_sz)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #renderizado de la UI
    screen.fill("black")
    pygame.draw.rect(screen,(255,255,255),(640,0,20,1280),40)
    i = 0
    for _ in range(12):
        pygame.draw.rect(screen,(0,0,0),(640,i,20,20),40)
        i += 72 
    pygame.draw.rect(screen,(255,255,255), player_ps,40)
    pygame.draw.rect(screen,(255,255,255),bot_ps,40)
    pygame.draw.rect(screen, (255, 255, 255),ball_ps,20)
    scoreboardplayer = font.render(f"{score_player}",True,(255,255,255))
    screen.blit(scoreboardplayer,(320,80))
    scoreboardbot = font.render(f"{score_bot}",True,(255,255,255))
    screen.blit(scoreboardbot,(960,80))
    

    #movimiento de pedotita
    ballx += ball_sp_x*dt
    bally += ball_sp_y*dt
    if bally >= 1280:
        bally == 1270
    
    
    
    # movimiento del jugador
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        playery -= 300 * dt
    if keys[pygame.K_s]:
        playery += 300 * dt
    if ballx <= playerx +20 and playery < bally < playery +80:
        ball_sp_x *= -1
    
    #movimiento del bot
    if boty < bally:
        boty += bot_sp*dt
    if boty > bally:
        boty -= bot_sp*dt
    if ballx <= botx +20 and boty < bally < boty +80:
        ball_sp_x *= -1
    
    #pointsss
    if ballx <= 0:
        score_bot += 1
        ballx, bally = 640, 360
        botx,boty = 1220,240
        playerx,playery = 185,360

    if ballx >= 1280:
        score_player += 1
        ballx, bally = 640, 360
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()