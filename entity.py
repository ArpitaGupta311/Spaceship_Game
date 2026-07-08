from re import X
from turtle import speed
import pygame

class Spaceship:
    def __init__(self):
        self.x = 470
        self.y = 600
        self.width = 100
        self.height = 100
        self.speed = 5
        self.image = pygame.image.load("assets/spaceship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.width, self.height))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, keys, WIDTH, HEIGHT):
        if keys[pygame.K_LEFT] and self.x >0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 400:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.width = 5
        self.height = 50
        self.speed = 50
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        print(self.image.get_size())

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= self.speed 

class UFO:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        self.radius= 40
        self.speed = 1
        self.health = 4  
        self.points = 10
        self.image = pygame.image.load("assets/ufo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.radius*2, self.radius*2))

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Asteroid:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = 35
        self.speed = 1

    def move(self):
        self.y += self.speed
    
    def draw(self, screen):
        pygame.draw.circle(screen, (136, 150, 200), (self.x,self.y), self.radius)

class Explosion():
        def __init__(self,x,y):
                self.x = x
                self.y = y
                self.radius = 10
                self.max_radius = 80
                self.growth_speed = 4

        def update(self):
                self.radius +=self.growth_speed
        
        def draw(self, screen):
                pygame.draw.circle(screen, (136,150,200), (self.x,self.y), self.radius)
