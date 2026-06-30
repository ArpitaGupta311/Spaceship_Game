from re import X
from turtle import speed
import pygame

class Spaceship:
    def __init__(self):
        self.x = 470
        self.y = 600
        self.width = 60
        self.height = 60
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (255,139,70), (self.x, self.y, self.width, self.height))

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
        self.height = 10
        self.speed = 10

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.width, self.height))

    def move(self):
        self.y -= self.speed 

class UFO:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        self.radius= 25
        self.speed = 1
        self.health = 4  
        self.points = 10

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (0,255,0), (self.x,self.y), self.radius)

class Asteroid:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = 30
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