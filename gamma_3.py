#!/bin/python3
import pygame, sys,random
from pygame.math import Vector2

class APPLE:
  def __init__(self):
    self.apple_img = pygame.image.load('sprites/apple.png')
    self.rand_placement()

  def draw(self):
    apple_rect = pygame.Rect(self.pos.x * cell_s,self.pos.y * cell_s, cell_s, cell_s)
    self.apple_img = pygame.transform.scale(self.apple_img,(cell_s,cell_s))

    screen.blit(self.apple_img,apple_rect)

   # pygame.draw.rect(screen,pygame.Color('red'),apple_rect)



  def rand_placement(self):
    self.x = random.randint(0, cell_a - 1)
    self.y = random.randint(0, cell_a - 1)
    self.pos = Vector2(self.x, self.y)


class SNACK:
  def __init__(self):
    self.body = [Vector2(6,8),Vector2(6,9),Vector2(6,10)]
    self.direction = Vector2(1,0)
    self.new_block = False

  def draw(self):
    for part in self.body:
      x_pos = int(part.x * cell_s)
      y_pos = int(part.y * cell_s)
      snack_rect = pygame.Rect(x_pos,y_pos,cell_s,cell_s)

      pygame.draw.rect(screen,pygame.Color('green'),snack_rect)

  def move(self):
    if self.new_block:
      body_copy = self.body[:]
    else:
      body_copy = self.body[:-1]
    body_copy.insert(0,body_copy[0] + self.direction)
    self.body = body_copy[:]
    self.new_block = False
    self.head = self.body[0]
    self.tail = self.body[1:]

  def make_me_longer(self):
    self.new_block = True

class MAIN:
  def __init__(self):
    self.snack = SNACK()
    self.apple = APPLE()

  def update(self):
    self.snack.move()
    self.check_endgame()
    self.check_omnomnom()

  def draw(self):
    screen.fill(pygame.Color('black'))
    self.apple.draw()
    self.snack.draw()

  def check_omnomnom(self):
    if self.apple.pos == self.snack.head:
      self.apple.rand_placement()
      self.snack.make_me_longer()

  def check_snack_collision(self):
    for part in self.snack.tail:
      if part == self.snack.body[0]:
        self.you_lost()

  def check_endgame(self):
    head_pos = self.snack.head
    if (head_pos.x not in range(0, cell_a)) or (head_pos.y not in range(0, cell_a)):
      self.you_lost()

    self.check_snack_collision()

  def you_lost(self):
    print('GAME OVER!!!!!!!!!')
    raise SystemExit

pygame.init()

cell_a = 20
cell_s = 40

screen = pygame.display.set_mode((cell_a * cell_s,cell_a * cell_s))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == SCREEN_UPDATE:
      main_game.update()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        main_game.snack.direction = Vector2(0,1)
      if event.key == pygame.K_UP:
        main_game.snack.direction = Vector2(0,-1)
      if event.key == pygame.K_LEFT:
        main_game.snack.direction = Vector2(-1,0)
      if event.key == pygame.K_RIGHT:
        main_game.snack.direction = Vector2(1,0)

  main_game.draw()
  pygame.display.update()
  clock.tick(60)
