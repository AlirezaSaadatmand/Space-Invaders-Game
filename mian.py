import pygame
from sys import exit

projectile_lst = []

WIDTH , HEIGHT = 1000 , 700

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
        self.y -= 5
        
        self.projectile_surface_rect = self.projectile_surface.get_rect(center = (self.x , self.y))
        screen.blit(self.projectile_surface , self.projectile_surface_rect)
        
def draw():
    screen.fill("black")
    player.draw()

    for projectile in projectile_lst:
        if projectile.y < 0:
            projectile_lst.remove(projectile)
        projectile.draw()
    
        
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