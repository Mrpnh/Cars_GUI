# Importing and intializing pygame

import pygame
import random
pygame.init()
pygame.mixer.init()

# Game variables

screenW=500
screenH=640
van_size_x=60
van_size_y=120
van_size=(van_size_x,van_size_y)
exit_game=False
game_over=False
lives=3

# Window intialization

gameWindow=pygame.display.set_mode((screenW,screenH))
pygame.mixer.music.load("tokyo_drift.mp3")
pygame.mixer.music.play(-1)
clock=pygame.time.Clock()


# Loading Images

pygame.display.set_caption("Cars")
bg = pygame.image.load("Road.png").convert()
welcome = pygame.image.load("welcome.jpg").convert()
bg=pygame.transform.scale(bg,(500,640))
player=pygame.image.load("player.png")
player=pygame.transform.scale(player,van_size)

# Rendering Text
def textRender(text,color,x,y,text_size):
     font=pygame.font.SysFont(None,text_size)
     screenText=font.render(text,True,color)
     gameWindow.blit(screenText,(x,y))

# Welcome loop
def welcome_note():
    global exit_game
    global game_over
    i=3
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
                break
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_over=False
                    gameLoop()
               
        gameWindow.blit(welcome,(0,0))
        textRender("Cars",(0,0,0),150,80,55)
        textRender("by",(0,0,0),230,120,35)
        textRender("Mrpnh",(255,0,0),260,150,55)
        textRender("Press Space to Play",(0,0,0),160,220,25)
        pygame.display.update()
    pygame.quit()
    quit()

# Game loop
def gameLoop():
    enemies=[pygame.transform.scale(pygame.image.load("police_car.png"),(van_size_x,105)),pygame.transform.scale(pygame.image.load("truck.png"),van_size),pygame.transform.scale(pygame.image.load("van.png"),van_size),pygame.transform.scale(pygame.image.load("van_2.png"),(van_size_x,140))]
    enemy_x=[110,220,330]
    enemy_vel=[8,6,7]
    current_enemy=enemies[0]
    current_enemy_pos=110
    current_enemy_vel=7
    i=0
    bg_y=3
    enemy_y=-100
    player_y=500
    score=0
    global exit_game
    global lives
    global game_over
    y=0
    player_x=200
    player_val=7
    while not game_over:
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
               exit_game=True
               break
        control=pygame.key.get_pressed()
        if control[pygame.K_RIGHT] and player_x<=340 :
              player_x+=player_val 
        if control[pygame.K_LEFT] and player_x>=100:
              player_x-=player_val 
    
        y_final= y% bg.get_height()
        gameWindow.blit(bg,(0,y_final))
        y+=bg_y
        gameWindow.blit(bg,(0,y_final-bg.get_height()))
        gameWindow.blit(player,(player_x,player_y))
        gameWindow.blit(current_enemy,(current_enemy_pos,enemy_y))
        enemy_y+=current_enemy_vel
    
        if i==100:
           score+=1
           i=0
        i+=1
        textRender("Score: "+ str(score),(255,0,0),0,5,25)

        if score%25==0 and score<1000 and score!=0:
           score+=1
           bg_y+=1
        if enemy_y>=700:
           current_enemy=random.choice(enemies)
           current_enemy_pos=random.choice(enemy_x)
           current_enemy_vel=random.choice(enemy_vel)
           enemy_y=-100
        
        if abs(player_x-current_enemy_pos)<60 and abs(player_y-enemy_y)<100:
            if lives==1:
                lives=3
                game_over=True
            else:
                lives-=1
                gameLoop()
                
        textRender("Lives: "+ str(lives),(0,0,0),432,5,25)
        pygame.display.update()
        clock.tick(100)

if __name__ == '__main__':
    welcome_note()
    
