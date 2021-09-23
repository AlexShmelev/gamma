#!/bin/python3
# GAME BOUT PULSING RECTANGLE


import pygame
import sys
import time

def main():

  pygame.init()

  pygame.display.set_caption(sys.argv[0])

  screen = pygame.display.set_mode((800,600))
  running = True

  while running:
    for event in pygame.event.get():

      for green in range(1,255):
        pygame.draw.rect(screen, (0,green,0), pygame.Rect(30,30,100,200))
        pygame.display.flip()
        time.sleep(0.01)
        if event.type == pygame.QUIT:
          running = False


if __name__ == '__main__':
  main()
