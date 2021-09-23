#!/bin/python3

import pygame
import sys
import time

def main():

  pygame.init()

  pygame.display.set_caption(sys.argv[0])

  screen = pygame.display.set_mode((800,600))
  running = True

  green = 0
  while running:
    for event in pygame.event.get():

      pygame.draw.rect(screen, (0,green,0), pygame.Rect(30,30,100,200))
      pygame.display.flip()

      green += 1
      if green == 255:
        green = 0

      if event.type == pygame.QUIT:
        running = False


if __name__ == '__main__':
  main()
