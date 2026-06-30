from pickle import FALSE
from entity import Asteroid, Explosion, Spaceship, Bullet, UFO
from system import Game_over_part, Check_collision, ufoXplayer_collision
import random
import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 700
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
bullet_width = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hehehehhehe")
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

font = pygame.font.SysFont(None,36)

bullets = []
ufos = []
player = Spaceship()
running = True
ufo_radius = 25
last_spawn_interval = 0
asteroid_spawn=0
spawn_interval = 1000
score = 0
game_over = False
asteroids = []
asteroid_radius = 30
explosions =[]

def spawn_ufo():
    random_x = random.randint(ufo_radius, WIDTH - ufo_radius)
    random_y = random.randint(ufo_radius,200)
    ufo = UFO(random_x, random_y)
    ufos.append(ufo)

def spawn_asteroid():
    random_x = random.randint(asteroid_radius, WIDTH - asteroid_radius)
    random_y = random.randint(asteroid_radius,200)
    asteroid = Asteroid(random_x, random_y)
    asteroids.append(asteroid)

def reset_game():
    global bullets, ufos, score, game_over, player, start_time

    bullets = []
    ufos =[]
    score = 0
    game_over = False
    player = Spaceship()
    start_time = pygame.time.get_ticks()

while running:
    #Handle Event
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet((player.x + player.width/2 - bullet_width/2), player.y) 
                bullets.append(bullet)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    #Update    
    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH, HEIGHT)
    current_time = pygame.time.get_ticks()

    if current_time - last_spawn_interval > spawn_interval:
        spawn_ufo()
        last_spawn_interval = current_time

    if current_time - asteroid_spawn > spawn_interval*5:
        spawn_asteroid()
        asteroid_spawn = current_time

    for ufo in ufos:
        ufo.move()

    for bullet in bullets:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)

    for asteroid in asteroids:
        asteroid.move()
        if bullet.y > HEIGHT - asteroid.radius:
            bullets.remove(bullet)
        
    for bullet in bullets[:]:
        for ufo in ufos[:]:
            if Check_collision(bullet, ufo):
                bullets.remove(bullet)
                ufos.remove(ufo)
                score += 10
                break

    for bullet in bullets[:]:
        for asteroid in asteroids[:]:
            if Check_collision(bullet, asteroid):
                bullets.remove(bullet)
                asteroids.remove(asteroid)
                explosion = Explosion(asteroid.x,asteroid.y)
                explosions.append(explosion)
                for explosion in explosions:
                    explosion.update()
                    if explosion.radius >= explosion.max_radius:
                        explosions.remove(explosion)
                        game_over = True
                        break
                break

    for ufo in ufos:
        if ufoXplayer_collision(player, ufo):
            game_over = True

    for asteroid in asteroids:
        if ufoXplayer_collision(player, asteroid):
            explosion = Explosion(asteroid.x,asteroid.y)
            explosions.append(explosion)
            for explosion in explosions:
                    explosion.update()
                    if explosion.radius >= explosion.max_radius:
                        explosions.remove(explosion)
                        game_over = True
                        break

    if not game_over:
        elapsed_time = current_time - start_time
        elapsed_seconds= elapsed_time//1000
    
    #Render
    screen.fill(BLACK)
    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for ufo in ufos:
        ufo.draw(screen)

    for asteroid in asteroids:
        asteroid.draw(screen)

    for explosion in explosions:
        explosion.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text,(20,20))

    if game_over:
        Game_over_part(screen, score, elapsed_seconds, font)

    if not game_over:
        time_text = font.render(f"Time Played: {elapsed_seconds}s", True, WHITE)
        screen.blit(time_text, (750,20))
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()

