import pygame
from sys import exit
import random
projectile_lst = []

enemy_lst = []
enemy2_lst = []

enemy_shoot_lst = []

gameover = False

WIDTH , HEIGHT = 1200 , 700

side = "left"

color_lst = ["red" , "green" , "blue" , "orange" , "purple"]

map1 = [[1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
        [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
        [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
        [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
        [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1]]

index = len(map1[0]) - 1
class Player:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT - 50
        
        self.player_surface = pygame.Surface( (50 , 50) )
        self.player_surface.fill("white")
        
        self.goingright = False
        self.goingleft = False
        
    def draw(self):
        if self.goingright and self.x + 25 < WIDTH:
            self.x += 4
        if self.goingleft and self.x - 25 > 0:
            self.x -= 4
            
        self.player_surface_rect = self.player_surface.get_rect(center = (self.x , self.y))
        screen.blit(self.player_surface , self.player_surface_rect)

class Projectile:
    def __init__(self , x , y , color):
        self.x = x
        self.y = y
        self.color = color
        self.projectile_surface = pygame.Surface( (5 , 10) )
        self.projectile_surface.fill(color)
    
    def draw(self , side):
        if side == "firend":
            self.y -= 7
        else:
            self.y += 3
        
        self.projectile_surface_rect = self.projectile_surface.get_rect(center = (self.x , self.y))
        screen.blit(self.projectile_surface , self.projectile_surface_rect)
        
class Enemy:
    def __init__(self , x , y , color):
        self.x = x
        self.y = y
        self.color = color
        self.enemy_surface = pygame.Surface( (40 , 40) )
        self.enemy_surface.fill(color)

    def shoot(self):
        enemy_shoot_lst.append(Projectile(self.x , self.y , self.color))

    def draw(self):
        
        self.enemy_surface_rect = self.enemy_surface.get_rect(center = (self.x , self.y))
        screen.blit(self.enemy_surface , self.enemy_surface_rect)

def create_enemy():
    unitx = WIDTH / (len(map1[0])+1)
    unity = 70
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            enemy_lst.append(Enemy(unitx * (j + 1) - 40 , unity * (-1) * (i + 1) - 40 , color_lst[i]))
            enemy2_lst.append(Enemy(unitx * (j + 1) - 40 , unity * (-1) * (i + 1) - 40 , color_lst[i]))
        
create_enemy()
dis = enemy_lst[0].x
def enemy_move(counter):
    global side
    global index
    if counter < 210:
        for enemy in enemy_lst:
            enemy.y += 2
    else:
        if side == "left" and enemy2_lst[index].x <= WIDTH - dis:
            for enemy in enemy_lst:
                enemy.x += 1
            for enemy in enemy2_lst:
                enemy.x += 1
            if enemy2_lst[index].x >= WIDTH - dis:
                side = "down"
        elif side == "down":
            for enemy in enemy_lst:
                enemy.y += 20
            for enemy in enemy2_lst:
                enemy.y += 20
            if enemy2_lst[0].x <= 0 + dis+5:   
                side = "left"
            else:
                side = "right"
        elif side == "right" and enemy2_lst[0].x >= 0 + dis:
            for enemy in enemy_lst:
                enemy.x -= 1
            for enemy in enemy2_lst:
                enemy.x -= 1
            if enemy2_lst[0].x <= 0 + dis:
                side = "down"
        if counter % 60 == 0:
            random.choice(enemy_lst).shoot()     
            
def check():
    global gameover
    for pro in projectile_lst:
        for enemy in enemy_lst:
            if pro.projectile_surface.get_rect(center = (pro.x , pro.y)).colliderect(enemy.enemy_surface_rect):
                projectile_lst.remove(pro)
                enemy_lst.remove(enemy)
                break
            
    for enemy in enemy_lst:
        if player.player_surface.get_rect(center = (player.x , player.y)).colliderect(enemy.enemy_surface_rect):
            gameover = True
    for shoot in enemy_shoot_lst:
        if shoot.projectile_surface.get_rect(center = (shoot.x , shoot.y)).colliderect(player.player_surface_rect):
            gameover = True
            
def draw():
    screen.fill("black")
    player.draw()

    for projectile in projectile_lst:
        if projectile.y < 0:
            projectile_lst.remove(projectile)
        projectile.draw("firend")
    
    for shoot in enemy_shoot_lst:
        shoot.draw("enemy")
    
    for enemy in enemy_lst:
        enemy.draw()
        
pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )
clock = pygame.time.Clock()

player = Player()

counter = 0

while not gameover:
    pygame.display.set_caption(f"Space invaders  FPS : {round(clock.get_fps())}")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_LEFT:
                player.goingleft = True
            if event.key == pygame.K_RIGHT:
                player.goingright = True
            if event.key == pygame.K_SPACE:
                projectile_lst.append(Projectile(player.x , player.y , "white"))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goingleft = False
            if event.key == pygame.K_RIGHT:
                player.goingright = False
    enemy_move(counter)
    draw()
    check() 
    counter += 1
    pygame.display.update()
    clock.tick(60)