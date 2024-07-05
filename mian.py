import pygame
from sys import exit

projectile_lst = []

enemy_lst = []

WIDTH , HEIGHT = 1200 , 700

color_lst = ["red" , "green" , "blue" , "orange" , "purple"]

map1 = [[1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
        [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
        [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
        [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
        [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1]]

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
            self.x += 3
        if self.goingleft and self.x - 25 > 0:
            self.x -= 3
            
        self.player_surface_rect = self.player_surface.get_rect(center = (self.x , self.y))
        screen.blit(self.player_surface , self.player_surface_rect)

class Projectile:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        
        self.projectile_surface = pygame.Surface( (5 , 10) )
        self.projectile_surface.fill("white")
    
    def draw(self):
        self.y -= 6
        
        self.projectile_surface_rect = self.projectile_surface.get_rect(center = (self.x , self.y))
        screen.blit(self.projectile_surface , self.projectile_surface_rect)
        
class Enemy:
    def __init__(self , x , y , color):
        self.x = x
        self.y = y
        self.enemy_surface = pygame.Surface( (30 , 30) )
        self.enemy_surface.fill(color)
    
    def draw(self):
        self.enemy_surface_rect = self.enemy_surface.get_rect(center = (self.x , self.y))
        screen.blit(self.enemy_surface , self.enemy_surface_rect)

def create_enemy():
    unitx = WIDTH / 11
    unity = 70
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            enemy_lst.append(Enemy(unitx * (j + 1), unity * (i + 1) , color_lst[i]))
        
create_enemy()

def draw():
    screen.fill("black")
    player.draw()

    for projectile in projectile_lst:
        if projectile.y < 0:
            projectile_lst.remove(projectile)
        projectile.draw()
    
    for enemy in enemy_lst:
        enemy.draw()
        
pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )
clock = pygame.time.Clock()

player = Player()

while True:
    pygame.display.set_caption(f"Space invaders  FPS : {round(clock.get_fps())}")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goingleft = True
            if event.key == pygame.K_RIGHT:
                player.goingright = True
            if event.key == pygame.K_SPACE:
                projectile_lst.append(Projectile(player.x , player.y))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goingleft = False
            if event.key == pygame.K_RIGHT:
                player.goingright = False
        
    draw()
    pygame.display.update()
    clock.tick(60)