import pygame
import random

class Player:
    def __init__(self, image, x , y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.x_change = 0
        self.y_change = 0
        self.score = 0
        self.existence = True

    def kinhsh(self):
        if self.x > 0 and self.x < 700 or (self.x == 0 and self.x_change > 0) or (self.x == 700 and self.x_change < 0):
            self.x = self.x + self.x_change
        else:
            self.x = self.x

        if self.y > 0 and self.y < 520 or (self.y == 0 and self.y_change > 0) or (self.y == 520 and self.y_change < 0):
            self.y = self.y + self.y_change
        else:
            self.y = self.y

    def show(self):
        if self.existence:
            screen.blit(self.image,(self.x,self.y))
    
    def controls_down(self, left, right, up, down,event):
        if event.key == up: 
            self.y_change = -1
                    
        elif event.key == left:
            self.x_change = -1
                
        elif event.key == down:
            self.y_change = 1
                
        elif event.key == right:
            self.x_change = 1
    
    def controls_up(self, left, right, up, down, event):
        if event.key == up or event.key == down:
            self.y_change = 0
        elif event.key == left or event.key == right:
            self.x_change = 0

class Mezedes:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('mezes.png')
        self.existence = True
    def show(self):
        if self.existence == True:
            screen.blit(self.image,(self.x,self.y))

mezes_one = Mezedes(500,300) 

def collision(playera,mezes):
    if abs(playera.x - mezes.x)<50 and abs(playera.y - mezes.y)<50 and mezes.existence:
        mezes.existence = False
        playera.score += 1
        print(playera.score)
        mezes.x = random.randint(50, 750)
        mezes.y = random.randint(50, 550)
        mezes.existence = True

class Enemies:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('enemy.png')
    
    def show(self):
        screen.blit(self.image,(self.x,self.y))
    
    def motion(self, playerc):
        if playerc.x-self.x < 0:
            self.x -= 0.3
        else:
            self.x += 0.3
        
        if playerc.y-self.y < 0:
            self.y -= 0.3
        else:
            self.y += 0.3

def collision_w_enemy(playerb, enemyb):
    if abs(playerb.x-enemyb.x)<50 and abs(playerb.y-enemyb.y)<50 and playerb.existence:
        playerb.existence = False
        print('game over')

enemy = Enemies(20,20)

pygame.init()
screen = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("first_game")
player_one = Player("player.png",200,300)

running = True
while running:
    screen.fill((50,50,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN: 
            player_one.controls_down(pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,event)

        if event.type == pygame.KEYUP:
            player_one.controls_up(pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,event)
    
    player_one.kinhsh()
    player_one.show()
    mezes_one.show()
    enemy.show()
    enemy.motion(player_one)
    collision(player_one,mezes_one)
    collision_w_enemy(player_one,enemy)
    pygame.display.update()

pygame.quit()
quit()
