# Simple pong game in Python3
# By @aritrasur

import pygame
import winsound

pygame.init()

win = pygame.display.set_mode((650, 550))
pygame.display.set_caption('PongGame by @aritrasur47')

# rgb
white = (255, 255, 255)
black = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.dx = 1
        self.dy = 1


paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 615
paddle2.rect.y = 225

paddle_speed = 20

pong = Ball()
pong.rect.x = 325
pong.rect.y = 275

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, pong)


def redraw():
    win.fill(black)
    # Title Font
    font = pygame.font.SysFont('Comic Sans MS', 20)
    text = font.render('** PONG **', False, white)
    text_rect = text.get_rect()
    text_rect.center = (615 // 2, 25)
    win.blit(text, text_rect)

    # Player1 Score
    p1_score = font.render(str(paddle1.points), False, white)
    p1_rect = p1_score.get_rect()
    p1_rect.center = (50, 50)
    win.blit(p1_score, p1_rect)

    # Player2 Score
    p2_score = font.render(str(paddle2.points), False, white)
    p2_rect = p2_score.get_rect()
    p1_rect.center = (600, 50)
    win.blit(p2_score, p1_rect)

    all_sprites.draw(win)
    pygame.display.update()


# main_loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y += -paddle_speed
    if key[pygame.K_s]:
        paddle1.rect.y += paddle_speed
    if key[pygame.K_UP]:
        paddle2.rect.y += -paddle_speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddle_speed

    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    if pong.rect.y > 525:
        pong.dy = -1
    if pong.rect.x > 630:
        pong.rect.x, pong.rect.y = 325, 275
        pong.dx = -1
        paddle1.points += 1
    if pong.rect.y < 10:
        pong.dy = 1
    if pong.rect.x < 10:
        pong.rect.x, pong.rect.y = 325, 275
        pong.dx = 1
        paddle2.points += 1

    if paddle1.rect.colliderect(pong.rect):
        pong.dx = 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if paddle2.rect.colliderect(pong.rect):
        pong.dx = -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    redraw()

pygame.quit()
