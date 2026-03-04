import pygame
import os

pygame.font.init()
pygame.mixer.init()
WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space invaders")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED_COLOR = (255,0,0)
YELLOW_COLOR = (255,255,0)
Border = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)
HEALTHFONT = pygame.font.SysFont("comicsans",40)
WINNERFONT = pygame.font.SysFont("comicsans",100)
FPS = 60
VEL = 5
BULLET_VEL = 7 
MAX_BULLETS = 3
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 50,40
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
YELLOW_IMAGE = pygame.image.load(os.path.join("Assets","PlayerRocketyellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_IMAGE = pygame.image.load(os.path.join("Assets","PlayerRocketred.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
SPACE_IMAGE = pygame.image.load(os.path.join("Assets","Space.png"))
SPACE = pygame.transform.scale(SPACE_IMAGE,(WIDTH,HEIGHT))

def draw_window(RED_HEALTH,YELLOW_HEALTH,RED_BULLETS,YELLOW_BULLETS,RED,YELLOW):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN, BLACK, Border)
    RED_HEALTH_TEXT = HEALTHFONT.render("Health: "+str(RED_HEALTH),1,WHITE)
    YELLOW_HEALTH_TEXT = HEALTHFONT.render("Health: "+str(YELLOW_HEALTH),1,WHITE)
    WIN.blit(RED_HEALTH_TEXT,(WIDTH-RED_HEALTH_TEXT.get_width()-10,10))
    WIN.blit(YELLOW_HEALTH_TEXT,(10,10))
    WIN.blit(YELLOW_SPACESHIP,(YELLOW.x,YELLOW.y))
    WIN.blit(RED_SPACESHIP,(RED.x,RED.y))
    for bullet in RED_BULLETS:
        pygame.draw.rect(WIN,RED_COLOR,bullet)
    for bullet in YELLOW_BULLETS:
        pygame.draw.rect(WIN,YELLOW_COLOR,bullet)
    pygame.display.update()

def yellow_movement(keys_pressed,YELLOW):
    if keys_pressed[pygame.K_a] and YELLOW.x - VEL > 0:
        YELLOW.x -= VEL
    if keys_pressed[pygame.K_d] and YELLOW.x + VEL + YELLOW.width < WIDTH:
        YELLOW.x += VEL
    if keys_pressed[pygame.K_w] and YELLOW.y - VEL > 0:
        YELLOW.y -= VEL
    if keys_pressed[pygame.K_s] and YELLOW.y + VEL + YELLOW.height < HEIGHT:
        YELLOW.y += VEL

def red_movement(keys_pressed, RED):
    if keys_pressed[pygame.K_LEFT] and RED.x - VEL > 0:
        RED.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and RED.x + VEL + RED.width < WIDTH:
        RED.x += VEL
    if keys_pressed[pygame.K_UP] and RED.y - VEL > 0:
        RED.y -= VEL
    if keys_pressed[pygame.K_DOWN] and RED.y + VEL + RED.height < HEIGHT:
        RED.y += VEL

def draw_winner(text):
    winnertext = WINNERFONT.render(text,1,WHITE)
    WIN.blit(winnertext,(WIDTH/2 - winnertext.get_width()/2,HEIGHT/2 - winnertext.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def handle_bullets(RED_BULLETS,YELLOW_BULLETS,YELLOW,RED):
    for bullet in YELLOW_BULLETS.copy():
        bullet.x += BULLET_VEL
        if RED.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            if bullet in YELLOW_BULLETS:
                YELLOW_BULLETS.remove(bullet)
        elif bullet.x > WIDTH:
            if bullet in YELLOW_BULLETS:
                YELLOW_BULLETS.remove(bullet)
    for bullet in RED_BULLETS.copy():
        bullet.x -= BULLET_VEL
        if YELLOW.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            if bullet in RED_BULLETS:
                RED_BULLETS.remove(bullet)
        elif bullet.x < 0:
            if bullet in RED_BULLETS:
                RED_BULLETS.remove(bullet)

def main():
    RED = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    YELLOW = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    RED_BULLETS = []
    YELLOW_BULLETS = []
    RED_HEALTH = 10
    YELLOW_HEALTH = 10
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(YELLOW_BULLETS) < MAX_BULLETS:
                    bullet = pygame.rect(YELLOW.x + YELLOW.width, YELLOW.y + YELLOW.height//2 - 2, 10,5)
                    YELLOW_BULLETS.append(bullet)
                if event.key == pygame.K_RCTRL and len(RED_BULLETS) < MAX_BULLETS:
                    bullet = pygame.Rect(RED.x,RED.y + RED.height//2 - 2, 10, 5)
                    RED_BULLETS.append(bullet)
            if event.type == RED_HIT:
                RED_HEALTH -= 1
            if event.type == YELLOW_HIT:
                YELLOW_HEALTH -= 1
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed,YELLOW)
        red_movement(keys_pressed,RED)
        handle_bullets(RED_BULLETS,YELLOW_BULLETS,YELLOW,RED)
        draw_window(RED_HEALTH,YELLOW_HEALTH,RED_BULLETS,YELLOW_BULLETS,RED,YELLOW)
        winner_text = ""
        if RED_HEALTH <= 0:
            winner_text = "Yellow Wins!"
        if YELLOW_HEALTH <= 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            run = False
            return

if __name__ == '__main__':
    main()


