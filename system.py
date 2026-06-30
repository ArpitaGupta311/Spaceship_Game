import pygame
WHITE = (255,255,255)
BLACK =(0,0,0)

def Game_over_part(screen,score, elapsed_seconds, font):
        final_score = score
        final_time = elapsed_seconds
        game_over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text,(400,300))
        final_score_text = font.render(f"FINAL SCORE: {final_score}", True, WHITE)
        screen.blit(final_score_text,(380,330))
        time_text = font.render(f"Time Played: {final_time}s", True, WHITE)
        screen.blit(time_text, (750,20))
        Reset_text = font.render("PRESS 'R' TO RESTART", True, WHITE)
        screen.blit(Reset_text,(340,660))

def Check_collision(bullet, ufo):
    bullet_x = bullet.x + bullet.width/2
    bullet_y = bullet.y + bullet.height/2

    dx = bullet_x - ufo.x
    dy = bullet_y - ufo.y
    return dx*dx + dy*dy <= ufo.radius*ufo.radius

def ufoXplayer_collision(player, ufo):
    player_rect = pygame.Rect(player.x,player.y,player.width,player.height)
    ufo_rect = pygame.Rect(ufo.x-ufo.radius, ufo.y-ufo.radius, 2*ufo.radius, 2*ufo.radius)
    return player_rect.colliderect(ufo_rect)

