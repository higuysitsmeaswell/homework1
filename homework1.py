import pygame,sys
import os
pygame.font.init()
pygame.init()
WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()
pygame.display.set_caption("Space invaders")
WHITE = (255,255,255)
black = (0,0,0)
RED_COLOR = (255,0,0)
YELLOW_COLOR = (255,255,0)
Border = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)
HEALTHFONT = pygame.font.SysFont("arial",40)
WINNERFONT = pygame.font.SysFont("arial",100)
BULLET_VEL = 7 
MAX_BULLETS = 3
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
FPS = 60
VEL = 3
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 40
YELLOW_IMAGE = pygame.image.load(os.path.join("Assets","PlayerRocketyellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
SPACE_IMAGE = pygame.image.load(os.path.join("Assets","Space.png"))
SPACE = pygame.transform.scale(SPACE_IMAGE,(WIDTH,HEIGHT))
RED_IMAGE = pygame.image.load(os.path.join("Assets","PlayerRocketred.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
RED_HEALTH = 10
YELLOW_HEALTH = 10
def draw_window(RED_HEALTH,YELLOW_HEALTH,RED_BULLETS,YELLOW_BULLETS,RED,YELLOW):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,black,Border)
    RED_HEALTH_TEXT = HEALTHFONT.render("Health: "+str(RED_HEALTH),1,WHITE)
    YELLOW_HEALTH_TEXT = HEALTHFONT.render("Health: "+str(YELLOW_HEALTH),1,WHITE)
    WIN.blit(RED_HEALTH_TEXT,(WIDTH-RED_HEALTH_TEXT.get_width()-10,10))
    WIN.blit(YELLOW_HEALTH_TEXT,(WIDTH-YELLOW_HEALTH_TEXT.get_width()-10,10))

    WIN.blit(YELLOW_SPACESHIP,(YELLOW.x,YELLOW.y))
    WIN.blit(RED_SPACESHIP,(RED.x,RED.y))

    for bullet in RED_BULLETS:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in YELLOW_BULLETS:
        pygame.draw.rect(WIN,YELLOW,bullet)
    pygame.display.update()


def yellow_move(keys_pressed,YELLOW):
    if keys_pressed[pygame.K_a] and YELLOW.x - VEL > 0:
        YELLOW.x -= VEL
    if keys_pressed[pygame.K_d] and YELLOW.x + VEL + YELLOW.width < WIDTH:
        YELLOW.x += VEL
    if keys_pressed[pygame.K_w] and YELLOW.y - VEL > 0:
        YELLOW.y -= VEL
    if keys_pressed[pygame.K_s] and YELLOW.y + VEL + YELLOW.height < HEIGHT:
        YELLOW.y += VEL

def red_move(keys_pressed, RED):
    if keys_pressed[pygame.K_LEFT] and RED.x - VEL > 0:
        RED.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and RED.x + VEL + RED.width < WIDTH:
        RED.x += VEL
    if keys_pressed[pygame.K_UP] and RED.y - VEL > 0:
        RED.y -= VEL
    if keys_pressed[pygame.K_DOWN] and RED.y + VEL + RED.height < HEIGHT:
        RED.y += VEL

def main():
    RED = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    YELLOW = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    RED_BULLETS = []
    YELLOW_BULLETS = []
    RED_HEALTH = 10
    YELLOW_HEALTH = 10
    run = True
    pygame.display.update()
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        key_pressed = pygame.key.get_pressed()
        yellow_move(key_pressed,YELLOW)
        red_move(key_pressed,RED)
        draw_window(RED,YELLOW,RED_BULLETS,YELLOW_BULLETS,RED_HEALTH,YELLOW_HEALTH)

if __name__ == '__main__':
    main()
    